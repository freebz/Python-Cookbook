# 8.25 캐시 인스턴스 생성

import logging
a = logging.getLogger('foo')
b = logging.getLogger('bar')
a is b
# False
c = logging.getLogger('foo')
a is c
# True


# 문제에 나온 클래스
class Spam:
    def __init__(self, name):
        self.name = name

# 캐시 지원
import weakref
_spam_cache = weakref.WeakValueDictionary()

def get_spam(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s
    else:
        s = _spam_cache[name]
    return s


a = get_spam('foo')
b = get_spam('bar')
a is b
# False
c = get_spam('foo')
a is c
# True



# 토론

# 주의: 이 코드는 제대로 동작하지 않는다.
import weakref

class Spam:
    _spam_cache = weakref.WeakValueDictionary()
    def __new__(cls, name):
        if name in cls._spam_cache:
            return cls._spam_cache[name]
        else:
            self = super().__new__(cls)
            cls._spam_cache[name] = self
            return self

    def __init__(self, name):
        print('Initializing Spam')
        self.name = name


s = Spam('Dave')
# Initializing Spam
t = Spam('Dave')
# Initializing Spam
s is t
# True


a = get_spam('foo')
b = get_spam('bar')
c = get_spam('foo')
list(_spam_cache)
# ['foo', 'bar']
del a
del c
list(_spam_cache)
# ['bar']
del b
list(_spam_cache)
# []


import weakref

class CachedSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()
    def get_spam(self, name):
        if name not in self._cache:
            s = Spam(name)
            self._cache[name] = s
        else:
            s = self._cache[name]
        return s

    def clear(self):
        self._cache.clear()

class Spam:
    manager = CachedSpamManager()
    def __init__(self, name):
        self.name = name

def get_spam(name):
    return Spam.manager.get_spam(name)


a = Spam('foo')
b = Spam('foo')
a is b
# False


class Spam:
    def __init__(self, *args, **kwargs):
        raise RuntimeError("Can't instantiate directly")

    # 대안 생성자
    @classmethod
    def _new(cls, name):
        self = cls.__new__(cls)
        self.name = name


import weakref

class CachedSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()
    def get_spam(self, name):
        if name not in self._cache:
            s = Spam._new(name)          # 수정한 생성
            self._cache[name] = s
        else:
            s = self._cache[name]
        return s
