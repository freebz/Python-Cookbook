# 8.8 서브클래스에서 프로퍼티 확장

class Person:
    def __init__(self, name):
        self.name = name

    # 게터 함수
    @property
    def name(self):
        return self._name

    # 세터 함수
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    # 딜리터 함수
    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)


s = SubPerson('Guido')
# Setting name to Guido
s.name
# Getting name
# 'Guido'
s.name = 'Larry'
# Setting name to Larry
s.name = 42
# Setting name to 42
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "example.py", line 16, in name
#        raise TypeError('Expected a string')
# TypeError: Expected a string


class SubPerson(Person):
    @Person.name.getter
    def name(self):
        print('Getting name')
        return super().name


class SubPerson(Person):
    @Person.name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)


# 토론

class SubPerson(Person):
    @property               # 동작하지 않음
    def name(self):
        print('Getting name')
        return super().name


s = SubPerson('Guido')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "example.py", line 5, in __init__
#     self.name = name
# AttributeError: can't set attribute


class SubPerson(Person):
    @Person.getter
    def name(self):
        print('Getting name')
        return super().name


s = SubPerson('Guido')
s.name
# Getting name
# 'Guido'
s.name = 'Larry'
s.name
# Getting name
# 'Larry'
s.name = 42
# Setting name to 42
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "example.py", line 16, in name
#        raise TypeError('Expected a string')
# TypeError: Expected a string


# 디스크립터
class String:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        instance.__dict__[self.name] = value

# 디스크립터를 가진 클래스
class Person:
    name = String('name')
    def __init__(self, name):
        self.name = name

# 디스크립터에 프로퍼티를 넣어 확장
class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)
