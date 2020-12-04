# 10.11 임포트 후크로 원격 머신에서 모듈 불러오기

testcode/
    spam.py
    fib.py
    grok/
        __init__.py
        blah.py


# spam.py
print("I'm spam")

def hello(name):
    print('Hello %s' % name)

# fib.py
print("I'm fib")

def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# grok/__init__.py
print("I'm grok.__init__")

# grok/blah.py
print("I'm grok.blah")


from urllib.request import urlopen
u = urlopen('http://localhost:15000/fib.py')
data = u.read().decode('utf-8')
print(data)
# # fib.py
# print("I'm fib")

# def fib(n):
#     if n < 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)


import imp
import urllib.request
import sys

def load_module(url):
    u = urllib.request.urlopen(url)
    source = u.read().decode('utf-8')
    mod = sys.modules.setdefault(url, imp.new_module(url))
    code = compile(source, url, 'exec')
    mod.__file__ = url
    mod.__package__ = ''
    exec(code, mod.__dict__)
    return mod


fib = load_module('http://localhost:15000/fib.py')
# I'm fib
fib.fib(10)
# 89
spam = load_module('http://load_module:15000/spam.py')
# I'm spam
spam.hello('Guido')
# Hello Guido
fib
# <module 'http://localhost:15000/fib.py' from 'http://localhost:15000/fib.py'>
spam
# <module 'http://localhost:15000/spam.py' from 'http://localhost:15000/spam.py'>


# urlimport.py

import sys
import importlib.abc
import imp
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from html.parser import HTMLParser

# 디버깅
import logging
log = logging.getLogger(__name__)

# 주어진 URL에서 링크 얻기
def _get_links(url):
    class LinkParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag == 'a':
                attrs = dict(attrs)
                links.add(attrs.get('href').rstrip('/'))

    links = set()
    try:
        log.debug('Getting links from %s' % url)
        u = urlopen(url)
        parser = LinkParser()
        parser.feed(u.read().decode('utf-8'))
    except Exception as e:
        log.debug('Could not get links. %s', e)
    log.debug('links: %r', links)
    return links

class UrlMetaFinder(importlib.abc.MetaPathFinder):
    def __init__(self, baseurl):
        self._baseurl = baseurl
        self._links   = { }
        self._loaders = { baseurl : UrlModuleLoader(baseurl) }

    def find_module(self, fullname, path=None):
        log.debug('find_module: fullname=%r, path=%r', fullname, path)
        if path is None:
            baseurl = self._baseurl
        else:
            if not path[0].startswith(self._baseurl):
                return None
            baseurl = path[0]

        parts = fullname.split('.')
        basename = parts[-1]
        log.debug('find_module: baseurl=%r, basename=%r', baseurl, basename)

        # 링크 캐시 확인
        if basename not in self._links:
            self._links[baseurl] = _get_links(baseurl)

        # 패키지인지 확인
        if basename in self._links[baseurl]:
            log.debug('find_module: trying package %r', fullname)
            fullurl = self._baseurl + '/' + basename
            # __init__.py에 접근하는 패키지 불러오기 시도
            loader = UrlPackageLoader(fullurl)
            try:
                loader.load_module(fullname)
                self._links[fullurl] = _get_links(fullurl)
                self._loaders[fullurl] = UrlModuleLoader(fullurl)
                log.debug('find_module: package %r loaded', fullname)
            except ImportError as e:
                log.debug('find_module: package failed. %s', e)
                loader = None
            return loader

        # 일반 모듈
        filename = basename + '.py'
        if filename in self._links[baseurl]:
            log.debug('find_module: module %r found', fullname)
            return self._loaders[baseurl]
        else:
            log.debug('find_module: module %r not found', fullname)
            return None

    def invalidate_caches(self):
        log.debug('invalidating link cache')
        self._links.clear()
        
# URL 모듈 로더
class UrlModuleLoader(importlib.abc.SourceLoader):
    def __init__(self, baseurl):
        self._baseurl = baseurl
        self._source_cache = {}

    def module_repr(self, module):
        return '<urlmodule %r from %r>' % (module.__name__, module.__file__)

    # 필요 메소드
    def load_module(self, fullname):
        code = self.get_code(fullname)
        mod = sys.modules.setdefault(fullname, imp.new_module(fullname))
        mod.__file__ = self.get_filename(fullname)
        mod.__loader__ = self
        mod.__package__ = fullname.rpartition('.')[0]
        exec(code, mod.__dict__)
        return mod

    # 추가적 확장
    def get_code(self, fullname):
        src = self.get_source(fullname)
        return compile(src, self.get_filename(fullname), 'exec')

    def get_data(self, path):
        pass

    def get_filename(self, fullname):
        return self._baseurl + '/' + fullname.split('.')[-1] + '.py'

    def get_source(self, fullname):
        filename = self.get_filename(fullname)
        log.debug('loader: reading %r', filename)
        if filename in self._source_cache:
            log.debug('loader: cached %r', filename)
            return self._source_cache[filename]
        try:
            u = urlopen(filename)
            source = u.read().decode('utf-8')
            log.debug('loader: %r loaded', filename)
            self._source_cache[filename] = source
            return source
        except (HTTPError, URLError) as e:
            log.debug('loader: %r. %s', filename, e)
            raise ImportError("Can't load %s" % filename)

    def is_package(self, fullname):
        return False
    
# URL 패키지 로더
class UrlPackageLoader(UrlModuleLoader):
    def load_module(self, fullname):
        mod = super().load_module(fullname)
        mod.__path__ = [ self._baseurl ]
        mod.__package__ = fullname

    def get_filename(self, fullname):
        return self._baseurl + '/' + '__init__.py'

    def is_package(self, fullname):
        return True

# 로더 설치/제거를 위한 유틸리티 함수
_installed_meta_cache = { }
def install_meta(address):
    if address not in _installed_meta_cache:
        finder = UrlMetaFinder(address)
        _installed_meta_cache[address] = finder
        sys.meta_path.append(finder)
        log.debug('%r installed on sys.meta_path', finder)

def remove_meta(address):
    if address in _installed_meta_cache:
        finder = _installed_meta_cache.pop(address)
        sys.meta_path.remove(finder)
        log.debug('%r removed from sys.meta_path', finder)


# 현재는 임포트에 실패
import fib
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ModuleNotFoundError: No module named 'fib'


# 임포터를 불러오고 재시도(동작한다.)
import urlimport
urlimport.install_meta('http://localhost:15000')
import fib
# I'm fib
import spam
# I'm spam
import grok.blah
# I'm grok.__init__
# I'm grok.blah
grok.blah.__file__
# 'http://localhost:15000/grok/blah.py'


# urlimport.py

# ... 기존 코드를 넣는다 ...


# URL을 위한 경로 찾기 클래스
class UrlPathFinder(importlib.abc.PathEntryFinder):
    def __init__(self, baseurl):
        self._links = None
        self._loader = UrlModuleLoader(baseurl)
        self._baseurl = baseurl

    def find_loader(self, fullname):
        log.debug('find_loader: %r', fullname)
        parts = fullname.split('.')
        basename = parts[-1]
        # 링크 캐시 확인
        if self._links is None:
            self._links = []     # 토큰을 본다.
            self._links = _get_links(self._baseurl)

        # 패키지인지 확인
        if basename in self._links:
            log.debug('find_loader: trying package %r', fullname)
            fullurl = self._baseurl + '/' + basename
            # __init__.py에 접근하는 패키지 불러오기 시도
            loader = UrlPackageLoader(fullurl)
            try:
                loader.load_module(fullname)
                log.debug('find_loader: package %r loaded', fullname)
            except ImportError as e:
                log.debug('find_loader: %r is a namespace package', fullname)
                loader = None
            return (loader, [fullurl])

        # 일반 모듈
        filename = basename + '.py'
        if filename in self._links:
            log.debug('find_loader: module %r found', fullname)
            return (self._loader, [])
        else:
            log.debug('find_loader: module %r not found', fullname)
            return (None, [])

    def invalidate_caches(self):
        log.debug('invalidating link cache')
        self._links = None

# URL과 같은지 경로 확인
_url_path_cache = {}
def handle_url(path):
    if path.startswith(('http://', 'https://')):
        log.debug('Handle path? %s. [Yes]', path)
        if path in _url_path_cache:
            finder = _url_path_cache[path]
        else:
            finder = UrlPathFinder(path)
            _url_path_cache[path] = finder
        return finder
    else:
        log.debug('Handle path? %s. [No]', path)

def install_path_hook():
    sys.path_hooks.append(handle_url)
    sys.path_importer_cache.clear()
    log.debug('Installing handle_url')

def remove_path_hook():
    sys.path_hooks.remove(handle_url)
    sys.path_importer_cache.clear()
    log.debug('Installing handle_url')


# 초기 임포트는 실패한다.
import fib
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ModuleNotFoundError: No module named 'fib'

# 경로 후크 설치
import urlimport
urlimport.install_path_hook()

# 여전히 임포트에 실패한다.
import fib
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ModuleNotFoundError: No module named 'fib'

# sys.path에 엔트리를 추가하고 동작하는지 확인한다.
import sys
sys.path.append('http://localhost:15000')
import fib
# I'm fib
import grok.blah
# I'm grok.__init__
# I'm grok.blah
grok.blah.__file__
# 'http://localhost:15000/grok/blah.py'


fib
# <urlmodule 'fib' from 'http://localhost:15000/fib.py'>
fib.__name__
# 'fib'
fib.__file__
# 'http://localhost:15000/fib.py'
import inspect
print(inspect.getsource(fib))
# # fib.py
# print("I'm fib")

# def fib(n):
#     if n < 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)



# 토론

import imp
m = imp.new_module('spam')
m
# <module 'spam'>
m.__name__
# 'spam'


import sys
import imp
m = sys.modules.setdefault('spam', imp.new_module('spam'))
m
# <module 'spam'>


import math
m = sys.modules.setdefault('math', imp.new_module('math'))
m
# <module 'math' (built-in)>
m.sin(2)
# 0.9092974268256817
m.cos(2)
# -0.4161468365471424


from pprint import pprint
pprint(sys.meta_path)
# [<class '_frozen_importlib.BuiltinImporter'>,
#  <class '_frozen_importlib.FrozenImporter'>,
#  <class '_frozen_importlib_external.PathFinder'>,
#  <six._SixMetaPathImporter object at 0x7fc9676948e0>]


class Finder:
    def find_module(self, fullname, path):
        print('Looking for', fullname, path)
        return None

import sys
sys.meta_path.insert(0, Finder()) # 첫 번째 엔트리 삽입
import math
# Looking for math None
import types
# Looking for types None
import threading
# Looking for threading None
# Looking for time None
# Looking for traceback None
# Looking for linecache None
# Looking for tokenize None
# Looking for token None


import xml.etree.ElementTree
# Looking for xml None
# Looking for xml.etree ['/usr/lib/python3.8/xml']
# Looking for xml.etree.ElementTree ['/usr/lib/python3.8/xml/etree']
# Looking for xml.etree.ElementPath ['/usr/lib/python3.8/xml/etree']
# Looking for _elementtree None


del sys.meta_path[0]
sys.meta_path.append(Finder())
import urllib.request
import datetime


import fib
# Looking for fib None
# Looking for cStringIO None
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ModuleNotFoundError: No module named 'fib'
import xml.superfast
# Looking for xml.superfast ['/usr/lib/python3.8/xml']
# Looking for cStringIO None
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ModuleNotFoundError: No module named 'xml.superfast'


from pprint import pprint
import sys
pprint(sys.path)
# ['',
#  '/usr/lib/python38.zip',
#  '/usr/lib/python3.8',
#  '/usr/lib/python3.8/lib-dynload',
#  '/home/fx/.local/lib/python3.8/site-packages',
#  '/usr/local/lib/python3.8/dist-packages',
#  '/usr/lib/python3/dist-packages',
#  'http://localhost:15000']


pprint(sys.path_importer_cache)
# {'.': FileFinder('.'),
#  '/usr/lib/python3.8': FileFinder('/usr/lib/python3.8'),
#  '/usr/lib/python3.8/collections': FileFinder('/usr/lib/python3.8/collections'),
#  '/usr/lib/python3.8/email': FileFinder('/usr/lib/python3.8/email'),
#  '/usr/lib/python3.8/email/mime': FileFinder('/usr/lib/python3.8/email/mime'),
#  '/usr/lib/python3.8/encodings': FileFinder('/usr/lib/python3.8/encodings'),
#  '/usr/lib/python3.8/html': FileFinder('/usr/lib/python3.8/html'),
#  '/usr/lib/python3.8/http': FileFinder('/usr/lib/python3.8/http'),
#  '/usr/lib/python3.8/importlib': FileFinder('/usr/lib/python3.8/importlib'),
#  '/usr/lib/python3.8/json': FileFinder('/usr/lib/python3.8/json'),
#  '/usr/lib/python3.8/lib-dynload': FileFinder('/usr/lib/python3.8/lib-dynload'),
#  '/usr/lib/python3.8/urllib': FileFinder('/usr/lib/python3.8/urllib'),
#  '/usr/lib/python3.8/xml': FileFinder('/usr/lib/python3.8/xml'),
#  '/usr/lib/python3.8/xml/dom': FileFinder('/usr/lib/python3.8/xml/dom'),
#  '/usr/lib/python3.8/xml/etree': FileFinder('/usr/lib/python3.8/xml/etree'),
#  '/usr/lib/python3.8/xml/parsers': FileFinder('/usr/lib/python3.8/xml/parsers'),
#  '/usr/lib/python38.zip': None,
#  'http://localhost:15000': None}


class Finder:
    def find_loader(self, name):
        print('Looking for', name)
        return (None, [])

import sys
# 임포터 캐시에 "debug" 엔트리 추가
sys.path_importer_cache['debug'] = Finder()
# sys.path에 "debug" 디력터리 추가
sys.path.insert(0, 'debug')
import threading
# Looking for threading
# Looking for time
# Looking for traceback
# Looking for linecache
# Looking for tokenize
# Looking for token


sys.path_importer_cache.clear()
def check_path(path):
    print('Checking', path)
    raise ImportError()

sys.path_hooks.insert(0, check_path)
import fib
# Checked debug
# Checking .
# Checking /usr/local/lib/python33.zip
# Checking /usr/local/lib/python3.3
# Checking /usr/local/lib/python3.3/plat-darwin
# Checking /usr/local/lib/python3.3/lib-dynload
# Checking /Users/beazley/.local/lib/python3.3/site-packages
# Checking /usr/local/lib/python3.3/site-packages
# Looking for fib
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ModuleNotFoundError: No module named 'fib'


def check_url(path):
    if path.startswith('http://'):
        return Finder()
    else:
        raise ImportError()

sys.path.append('http://localhost:15000')
sys.path_hooks[0] = check_url
import fib
# Looking for fib             # 파인더 출력!
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ModuleNotFoundError: No module named 'fib'

# sys.path_importer_cache에 Finder가 설치되었다.
sys.path_importer_cache['http://localhost:15000']
# <__main__.Finder object at 0x10064c850>


import xml.etree.ElementTree
xml.__path__
# ['/usr/lib/python3.8/xml']
xml.etree.__path__
# ['/usr/lib/python3.8/xml/etree']


# 링크 캐시 확인
if self._links is None:
    self._links = []     # 토론 참고
    self._links = _get_links(self._baseurl)


import logging
logging.basicConfig(level=logging.DEBUG)
import urlimport
urlimport.install_path_hook()
# DEBUG:urlimport:Installing handle_url
# import fib
# DEBUG:urlimport:Handle path? /usr/local/lib/python33.zip. [No]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ModuleNotFoundError: No module named 'fib'
import sys
sys.path.append('http://localhost:15000')
import fib
# DEBUG:urlimport:Handle path? http://localhost:15000. [Yes]
# DEBUG:urlimport:Getting links from http://localhost:15000
# DEBUG:urlimport:links: {'spam.py', 'fib.py', 'grok'}
# DEBUG:urlimport:find_loader: 'fib'
# DEBUG:urlimport:find_loader: module 'fib' found
# DEBUG:urlimport:loader: reading 'http://localhost:15000/fib.py'
# DEBUG:urlimport:loader: 'http://localhost:15000/fib.py' loaded
# I'm fib
