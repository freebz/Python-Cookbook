# 9.18 클래스를 프로그램적으로 정의

# stock.py
# 부분으로부터 클래스를 수동으로 만드는 예제

# 메소드
def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price

def cost(self):
    return self.shares * self.price

cls_dict = {
    '__init__' : __init__,
    'cost' : cost,
}

# 클래스 만들기
import types

Stock = types.new_class('Stock', (), {}, lambda ns: ns.update(cls_dict))
Stock.__modulel__ = __name__


s = Stock('ACME', 50, 91.1)
s
# <types.Stock object at 0x7f96e5273880>
s.cost()
# 4555.0


import abc
Stock = types.new_class('Stock', (), {'metaclass': abc.ABCMeta},
                        lambda ns: ns.update(cls_dict))

Stock.__module__ = __name__
Stock
# <class '__main__.Stock'>
type(Stock)
# <class 'abc.ABCMeta'>


class Spam(Base, debug=True, typecheck=False):
    ...


Spam = types.new_class('Spam', (Base,),
                       {'debug': True, 'typecheck': False},
                       lambda ns: ns.update(cls_dict))



# 토론

Stock = collections.namedtuple('Stock', ['name', 'shares', 'price'])
Stock
# <class '__main__.Stock'>


import operator
import types
import sys

def named_tuple(classname, fieldnames):
    # 필드 속성 접근자의 딕셔너리 생성
    cls_dict = { name: property(operator.itemgetter(n))
                 for n, name in enumerate(fieldnames) }

    # __new__ 함수를 만들고 클래스 딕셔너리에 추가
    def __new__(cls, *args):
        if len(args) != len(fieldnames):
            raise TypeError('Expected {} arguments'.format(len(fieldnames)))
        return tuple.__new__(cls, args)

    cls_dict['__new__'] = __new__

    # 클래스 만들기
    cls = types.new_class(classname, (tuple,), {},
                          lambda ns: ns.update(cls_dict))

    # 호출자에 모듈 설정
    cls.__module__ = sys._getframe(1).f_globals['__name__']
    return cls


Point = named_tuple('Point', ['x', 'y'])
Point
# <class '__main__.Point'>
p = Point(4, 5)
len(p)
# 2
p.x
# 4
p.y
# 5
p.x = 2
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: can't set attribute
print('%s %s' % p)
# 4 5


Stock = type('Stock', (), cls_dict)


import types

metaclass, kwargs, ns = types.prepare_class('Stock', (), {'metaclass': type})
