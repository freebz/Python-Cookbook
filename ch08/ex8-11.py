# 8.11 자료 구조 초기화 단순화하기

class Structure:
    # 예상되는 필드를 명시하는 클래스 변수
    _fields= []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        # 속성 설정
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

# 예제 클래스 정의
if __name__ == '__main__':
    class Stock(Structure):
        _fields = ['name', 'shares', 'price']

    class Point(Structure):
        _fields = ['x','y']

    class Circle(Structure):
        _fields = ['radius']
        def area(self):
            return math.pi * self.radius ** 2


s = Stock('ACME', 50, 91.1)
p = Point(2, 3)
c = Circle(4.5)
s2 = Stock('ACME', 50)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "STRUCTURE.py", line 6, in <module>
#     s = Stock('ACME', 50, 91.1)
# NameError: name 'Stock' is not defined


class Structure:
    _fields= []
    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        # 모든 위치 매개변수 설정
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # 남아 있는 키워드 매개변수 설정
        for name in self._fields[len(args):]:
            setattr(self, name, kwargs.pop(name))

        # 남아 있는 기타 매개변수가 없는지 확인
        if kwargs:
            raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))

# 사용 예
if __name__ == '__main__':
    class Stock(Structure):
        _fields = ['name', 'shares', 'price']

    s1 = Stock('ACME', 50, 91.1)
    s2 = Stock('ACME', 50, price=91.1)
    s3 = Stock('ACME', shares=50, price=91.1)


class Structure:
    # 예상되는 필드를 명시하는 클래스 변수
    _fields= []
    def __init__(self, *args, **kwargs):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        # 속성 설정
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # (있다면) 추가적인 매개변수 설정
        extra_args = kwargs.keys() - self._fields
        for name in extra_args:
            setattr(self, name, kwargs.pop(name))
        if kwargs:
            raise TypeError('Duplicate values for {}'.format(','.join(kwargs)))

# 사용 예
if __name__ == '__main__':
    class Stock(Structure):
        _fields = ['name', 'shares', 'price']

    s1 = Stock('ACME', 50, 91.1)
    s2 = Stock('ACME', 50, 91.1, date='8/2/2012')


# 토론

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Structure:
    # 예상되는 필드를 명시하는 클래스 변수
    _fields= []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        # 매개변수 설정 (대안)
        self.__dict__.update(zip(self._fields,args))


help(Stock)
# Help on class Stock in module __main__:

# class Stock(Structure)
# ...
#  |  ----------------------------------------------------------------------
#  |  Methods inherited from Structure:
#  |  
#  |  __init__(self, *args, **kwargs)
#  |  
# ...


def init_fromlocals(self):
    import sys
    locs = sys._getframe(1).f_locals
    for k, v in locs.items():
        if k != 'self':
            setattr(self, k, v)

class Stock:
    def __init__(self, name, shares, price):
        init_fromlocals(self)
