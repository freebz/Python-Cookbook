# 8.18 믹스인으로 클래스 확장

class LoggedMappingMixin:
    '''
    get/set/delete에 로깅 추가
    '''
    __slots__ = ()

    def __getitem__(self, key):
        print('Getting ' + str(key))
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        print('Setting {} = {!r}'.format(key, value))
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        print('Deleting ' + str(key))
        return super().__delitem__(key)

class SetOnceMappingMixin:
    '''
    키가 한 번만 설정되도록 함
    '''
    __slots__ = ()
    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super().__setitem__(key, value)

class StringKeysMappingMixin:
    '''
    키에 문자열만 허용
    '''
    __slots__ = ()
    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError('keys must be strings')
        return super().__setitem__(key, value)


class LoggedDict(LoggedMappingMixin, dict):
    pass

d = LoggedDict()
d['x'] = 23
# Setting x = 23
d['x']
# Getting x
# 23
del d['x']
# Deleting x

from collections import defaultdict
class SetOnceDefaultDict(SetOnceMappingMixin, defaultdict):
    pass

d = SetOnceDefaultDict(list)
d['x'].append(2)
d['y'].append(3)
d['x'].append(10)
d['x'] = 23
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "mixin.py", line 24, in __setitem__
#     raise KeyError(str(key) + ' already set')
# KeyError: 'x already set'

from collections import OrderedDict
class StringOrderedDict(StringKeysMappingMixin,
                        SetOnceMappingMixin,
                        OrderedDict):
    pass

d = StringOrderedDict()
d['x'] = 23
d[42] = 10
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "mixin.py", line 45, in __setitem__
#     raise TypeError('keys must be strings')
# TypeError: keys must be strings
d['x'] = 42
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "mixin.py", line 46, in __setitem__
#     return super().__setitem__(key, value)
#   File "mixin.py", line 28, in __setitem__
#     raise KeyError(str(key) + ' already set')
# KeyError: 'x already set'


# 토론

from xmlrpc.server import SimpleXMLRPCServer
from socketserver import ThreadingMixIn
class ThreadedXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass


class RestrictKeysMixin:
    def __init__(self, *args, _restrict_key_type, **kwargs):
        self.__restrict_key_type = _restrict_key_type
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        if not isinstance(key, self.__restrict_key_type):
            raise TypeError('Keys must be ' + str(self.__restrict_key_type))
        super().__setitem__(key, value)


class RDict(RestrictKeysMixin, dict):
    pass

d = RDict(_restrict_key_type=str)
e = RDict([('name','Dave'), ('n',37)], _restrict_key_type=str)
f = RDict(name='Dave', n=37, _restrict_key_type=str)
f
# {'name': 'Dave', 'n': 37}
f[42] = 10
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "mixin.py", line 83, in __setitem__
#     raise TypeError('Keys must be ' + str(self.__restrict_key_type))
# TypeError: Keys must be <class 'str'>


class LoggedDict(LoggedMappingMixin, dict):
    pass


def LoggedMapping(cls):
    cls_getitem = cls.__getitem__
    cls_setitem = cls.__setitem__
    cls_delitem = cls.__delitem__

    def __getitem__(self, key):
        print('Getting ' + str(key))
        return cls_getitem(self, key)

    def __setitem__(self, key, value):
        print('Setting {} = {!r}'.format(key, value))
        return cls_setitem(self, key, value)

    def __delitem__(self, key):
        print('Deleting ' + str(key))
        return cls_delitem(self, key)

    cls.__getitem__ = __getitem__
    cls.__setitem__ = __setitem__
    cls.__delitem__ = __delitem__
    return cls


@LoggedMapping
class LoggedDict(dict):
    pass
