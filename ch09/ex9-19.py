# 9.19 정의 시 클래스 멤버 초기화

import operator

class StructTupleMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for n, name in enumerate(cls._fields):
            setattr(cls, name, property(operator.itemgetter(n)))

class StructTuple(tuple, metaclass=StructTupleMeta):
    _fields = []
    def __new__(cls, *args):
        if len(args) != len(cls._fields):
            raise ValueError('{} arguments required'.format(len(cls._fields)))
        return super().__new__(cls,args)


class Stock(StructTuple):
    _fields = ['name', 'shares', 'price']

class Point(StructTuple):
    _fields = ['x', 'y']


s = Stock('ACME', 50, 91.1)
s
# ('ACME', 50, 91.1)
s[0]
# 'ACME'
s.name
# 'ACME'
s.shares * s.price
# 4555.0
s.shares = 23
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: can't set attribute



# 토론

s = Stock('ACME', 50, 91.1)     # OK
s = Stock(('ACME', 50, 91.1))   # Error
