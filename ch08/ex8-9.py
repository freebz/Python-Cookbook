# 8.9 새로운 클래스나 인스턴스 속성 만들기

# 타입을 확인하는 정수형 디스크립터 속성
class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = Integer('x')
    y = Integer('y')
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(2, 3)
p.x           # Point.x.__get__(p,Point) 호출
# 2
p.y = 5       # Point.y.__set__(p, 5) 호출
p.x = 2.3     # Point.x.__set__(p, 2.3) 호출
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "descrip.py", line 12, in __set__
#     raise TypeError('Expected an int')
# TypeError: Expected an int


# 토론

# 동작하지 않음
class Point:
    def __init__(self, x, y):
        self.x = Integer('x')       # 안 된다. 반드시 클래스 변수여야 한다.
        self.y = Integer('y')
        self.x = x
        self.y = y


# 타입을 확인하는 정수형 디스크립터 속성
class Integer:
    ...
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]
    ...


p = Point(2,3)
p.x      # Point.x.__get__(p, Point) 호출
# 2
Point.x  # Point.x.__get__(None, Point) 호출
# <__main__.Integer object at 0x7f6330ad9cf8>


# 속성 타입을 확인하는 디스크립터
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected ' + str(self.expected_type))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

# 선택한 속성에 적용되는 클래스 데코레이터(decorator)
def typeassert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
            # 클래스에 Typed 디스크립터 설정
            setattr(cls, name, Typed(name, expected_type))
        return cls
    return decorate

# 사용 예
@typeassert(name=str, shares=int, price=float)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
