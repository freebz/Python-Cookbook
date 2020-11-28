# 9.20 함수 주석으로 다중 디스패치 구현

class Spam:
    def bar(self, x:int, y:int):
        print('Bar 1:', x, y)
    def bar(self, s:str, n:int = 0):
        print('Bar 2:', s, n)

s = Spam()
s.bar(2, 3)        # Bar 1: 2 3 출력
s.bar('hello')     # Bar 2: hello 0 출력


# multiple.py

import inspect
import types

class MultiMethod:
    '''
    Represents a single multimethod.
    '''
    def __init__(self, name):
        self._methods = {}
        self.__name__ = name

    def register(self, meth):
        '''
        멀티 메소드로 새 메소드 등록
        '''
        sig = inspect.signature(meth)

        # 메소드 주석으로부터 타입 시그니처 만들기
        types = []
        for name, parm in sig.parameters.items():
            if name == 'self':
                continue
            if parm.annotation is inspect.Parameter.empty:
                raise TypeError(
                    'Argument {} must be annotated with a type'.format(name)
                )
            if not isinstance(parm.annotation, type):
                raise TypeError(
                    'Argument {} annotation must be a type'.format(name)
                )
            if parm.default is not inspect.Parameter.empty:
                self._methods[tuple(types)] = meth
            types.append(parm.annotation)

        self._methods[tuple(types)] = meth

    def __call__(self, *args):
        '''
        인자의 타입 시그니처에 따라 메소드 호출
        '''
        types = tuple(type(arg) for arg in args[1:])
        meth = self._methods.get(types, None)
        if meth:
            return meth(*args)
        else:
            raise TypeError('No matching method for types {}'.format(types))

    def __get__(self, instance, cls):
        '''
        클래스에 동작하는 호출을 할 필요가 있는 디스크립터 메소드
        '''
        if instance is not None:
            return types.MethodType(self, instance)
        else:
            return self

class MultiDict(dict):
    '''
    메타클래스에 멀티메소드를 만들기 위한 특별 딕셔너리
    '''
    def __setitem__(self, key, value):
        if key in self:
            # 만약 키가 이미 존재한다면, 반드시 멀티메소드나 호출 가능한 것이어야 한다.
            current_value = self[key]
            if isinstance(current_value, MultiMethod):
                current_value.register(value)
            else:
                mvalue = MultiMethod(key)
                mvalue.register(current_value)
                mvalue.register(value)
                super().__setitem__(key, mvalue)
        else:
            super().__setitem__(key, value)

class MultipleMeta(type):
    '''
    메소드의 다중 디스패치를 허용하는 메타클래스
    '''
    def __new__(cls, clsname, bases, clsdict):
        return type.__new__(cls, clsname, bases, dict(clsdict))

    @classmethod
    def __prepare__(cls, clsname, bases):
        return MultiDict()


class Spam(metaclass=MultipleMeta):
    def bar(self, x: int, y:int):
        print('Bar 1:', x, y)
    def bar(self, s:str, n:int = 0):
        print('Bar 2:', s, n)

# 예제: 오버로딩된 __init__
import time
class Date(metaclass=MultipleMeta):
    def __init__(self, year: int, month:int, day:int):
        self.year = year
        self.month = month
        self.day = day

    def __init__(self):
        t = time.localtime()
        self.__init__(t.tm_year, t.tm_mon, t.tm_mday)


s = Spam()
s.bar(2, 3)
# Bar 1: 2 3
s.bar('hello')
# Bar 2: hello 0
s.bar('hello', 5)
# Bar 2: hello 5
s.bar(2, 'hello')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "multiple.py", line 42, in __call__
#     raise TypeError('No matching method for types {}'.format(types))
# TypeError: No matching method for types (<class 'int'>, <class 'str'>)

# 오버로딩된 __init__
d = Date(2012, 12, 21)
# 오늘 날짜 구하기
e = Date()
e.year
# 2012
e.month
# 12
e.day
# 3



# 토론

b = s.bar
b
# <bound method bar of <__main__.Spam object at 0x7f0d79aa3700>>
b.__self__
# <__main__.Spam object at 0x7f0d79aa3700>
b.__func__
# <__main__.MultiMethod object at 0x7f0d79aa3760>
b(2, 3)
# Bar 1: 2 3
b('hello')
# Bar 2: hello 0


s.bar(x=2, y=3)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: __call__() got an unexpected keyword argument 'x'

s.bar(s='hello')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: __call__() got an unexpected keyword argument 's'


class A:
    pass

class B(A):
    pass

class C:
    pass

class Spam(metaclass=MultipleMeta):
    def foo(self, x:A):
        print('Foo 1:', x)

    def foo(self, x: C):
        print('Foo 2:', x)


s = Spam()
a = A()
s.foo(a)
# Foo 1: <__main__.A object at 0x7f0d7ae48040>
c = C()
s.foo(c)
# Foo 2: <__main__.C object at 0x7f0d79b06760>
b = B()
s.foo(b)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "muliple.py", line 61, in __call__
#     raise TypeError('No matching method for types {}'.format(types))
# TypeError: No matching method for types (<class '__main__.B'>,)


import types

class multimethod:
    def __init__(self, func):
        self._methods = {}
        self.__name__ = func.__name__
        self._default = func

    def match(self, *types):
        def register(func):
            ndefaults = len(func.__defaults__) if func.__defaults__ else 0
            for n in range(ndefaults+1):
                self._methods[types[:len(types) - n]] = func
            return self
        return register

    def __call__(self, *args):
        types = tuple(type(arg) for arg in args[1:])
        meth = self._methods.get(types, None)
        if meth:
            return meth(*args)
        else:
            return self._default(*args)

    def __get__(self, instance, cls):
        if instance is not None:
            return types.MethodType(self, instance)
        else:
            return self


class Spam:
    @multimethod
    def bar(self, *args):
        # 매치가 없는 경우 호출되는 기본 메소드
        raise TypeError('No matching method for bar')

    @bar.match(int, int)
    def bar(self, x, y):
        print('Bar 1:', x, y)

    @bar.match(str, int)
    def bar(self, s, n = 0):
        print('Bar 2:', s, n)
