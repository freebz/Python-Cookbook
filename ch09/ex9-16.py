# 9.16 *args, **kwargs에 매개변수 시그니처 강제

from inspect import Signature, Parameter
# func(x, y=42, *, z=None)에 시그니처 만들기
parms = [ Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
          Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=42),
          Parameter('z', Parameter.KEYWORD_ONLY, default=None) ]
sig = Signature(parms)
print(sig)
# (x, y=42, *, z=None)


def func(*args, **kwargs):
    bound_values = sig.bind(*args, **kwargs)
    for name, value in bound_values.arguments.items():
        print(name,value)

# 여러 예제 시도
func(1, 2, z=3)
# x 1
# y 2
# z 3
func(1)
# x 1
func(1, z=3)
# x 1
# z 3
func(y=2, x=1)
# x 1
# y 2
func(1, 2, 3, 4)
# Traceback (most recent call last):
# ...
#   File "/usr/lib/python3.8/inspect.py", line 2951, in _bind
#     raise TypeError('too many positional arguemnts')
# TypeError: too many positional arguments
func(y=2)
# Traceback (most recent call last):
# ...
#   File "/usr/lib/python3.8/inspect.py", line 2940, in _bind
#     raise TypeError(msg) from None
# TypeError: missing a required argument: 'x'


from inspect import Signature, Parameter

def make_sig(*names):
    parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
             for name in names]
    return Signature(parms)

class Structure:
    __signature__ = make_sig()
    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)

    # 사용 예제
    class Stock(Structure):
        __signature__ = make_sig('name', 'shares', 'price')

    class Point(Structure):
        __signature__ = make_sig('x', 'y')


import inspect
print(inspect.signature(Stock))
# (name, shares, price)
s1 = Stock('ACME', 100, 490.1)
s2 = Stock('ACME', 100)
# Traceback (most recent call last):
# ...
# TypeError: __init__() missing 1 required positional argument: 'price'
s3 = Stock('ACME', 100, 490.1, shares=50)
# Traceback (most recent call last):
# ...
# TypeError: __init__() got multiple values for argument 'shares'



# 토론

from inspect import Signature, Parameter

def make_sig(*names):
    parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
             for name in names]
    return Signature(parms)

class StructureMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        clsdict['__signature__'] = make_sig(*clsdict.get('_fields',[]))
        return super().__new__(cls, clsname, bases, clsdict)

class Structure(metaclass=StructureMeta):
    _fields = []
    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)

# 예제
class Stock(Structure):
    _fields = ['name', 'shares', 'price']

class Point(Structure):
    _fields = ['x', 'y']


import inspect
print(inspect.signature(Stock))
# (name, shares, price)
print(inspect.signature(Point))
# (x, y)
