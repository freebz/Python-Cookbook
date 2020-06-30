# 6.7 네임스페이스로 XML 문서 파싱

from xml.etree.ElementTree import parse
doc = parse('ns2.xml')

# 동작하는 쿼리
doc.findtext('author')
# 'David Beazley'
doc.find('content')
# <Element 'content' at 0x7ff0010cdd18>

# 네임스페이스 관련 쿼리(동작하지 않음)
doc.find('content/html')

# 조건에 맞는 경우에만 동작
doc.find('content/{http://www.w3.org/1999/xhtml}html')
# <Element '{http://www.w3.org/1999/xhtml}html' at 0x7ff0010cd818>

# 동작하지 않음
doc.findtext('content/{http://www.w3.org/1999/xhtml}html/head/title')

# 조건에 일치함
doc.findtext('content/{http://www.w3.org/1999/xhtml}html/'
 '{http://www.w3.org/1999/xhtml}head/{http://www.w3.org/1999/xhtml}title')
# 'Hello World'


class XMLNamespaces:
    def __init__(self, **kwargs):
        self.namespaces = {}
        for name, uri in kwargs.items():
            self.register(name, uri)
    def register(self, name, uri):
        self.namespaces[name] = '{'+uri+'}'
    def __call__(self, path):
        return path.format_map(self.namespaces)


ns = XMLNamespaces(html='http://www.w3.org/1999/xhtml')
doc.find(ns('content/{html}html'))
# <Element '{http://www.w3.org/1999/xhtml}html' at 0x7ff0010cd818>
doc.findtext(ns('content/{html}html/{html}head/{html}title'))
# 'Hello World'


# 토론

from xml.etree.ElementTree import iterparse
for evt, elem in iterparse('ns2.xml', ('end', 'start-ns', 'end-ns')):
    print(evt, elem)

# end <Element 'author' at 0x7ff0010cde58>
# start-ns ('', 'http://www.w3.org/1999/xhtml')
# end <Element '{http://www.w3.org/1999/xhtml}title' at 0x7ff0010cd368>
# end <Element '{http://www.w3.org/1999/xhtml}head' at 0x7ff0010cd3b8>
# end <Element '{http://www.w3.org/1999/xhtml}h1' at 0x7ff0010cd2c8>
# end <Element '{http://www.w3.org/1999/xhtml}body' at 0x7ff0010cd318>
# end <Element '{http://www.w3.org/1999/xhtml}html' at 0x7ff0010cd408>
# end-ns None
# end <Element 'content' at 0x7ff0010cdea8>
# end <Element 'top' at 0x7ff0010cdbd8>
elem    # 최상단 요소
# <Element 'top' at 0x7ff0010cdbd8>
