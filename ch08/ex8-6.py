# 8.6 관리 속성 만들기

class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    # 게터 함수
    @property
    def first_name(self):
        return self._first_name

    # 세터 함수
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # 딜리터 함수(옵션)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")


a = Person('Guido')
a.first_name        # 게터 호출
# 'Guido'
a.first_name = 42   # 세터 호출
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "prop.py", line 14, in first_name
# TypeError: Expected a string
del a.first_name
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: Can't delete attribute


class Person:
    def __init__(self, first_name):
        self.set_first_name(first_name)

    # 게터 함수
    def get_first_name(self):
        return self._first_name

    # 세터 함수
    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # 딜리터 함수(옵션)
    def del_first_name(self):
        raise AttributeError("Can't delete attribute")

    # 기존 게터/세터 메소드로 프로퍼티 만들기
    name = property(get_first_name, set_first_name, del_first_name)


# 토론

Person.first_name.fget
# <function Person.first_name at 0x7f632cff1c80>
Person.first_name.fset
# <function Person.first_name at 0x7f632cff1d08>
Person.first_name.fdel
# <function Person.first_name at 0x7f632cff1d90>


class Person:
    def __init__(self, first_name):
        self.first_name = name
    @property
    def first_name(self):
        return self._first_name
    @first_name.setter
    def first_name(self, value):
        self._first_name = value


import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    @property
    def area(self):
        return math.pi * self.radius ** 2
    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


c = Circle(4.0)
c.radius
# 4.0
c.area                  # ()가 쓰이지 않았다.
# 50.26548245743669
c.perimeter             # ()가 쓰이지 않았다.
# 25.132741228718345


p = Person('Guido')
p.get_first_name()
# 'Guido'
p.set_first_name('Larry')


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # 이름이 다른 프러퍼티 코드의 반복 (좋지 않다!)
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._last_name = value
