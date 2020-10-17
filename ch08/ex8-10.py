# 8.10 게으른 계산을 하는 프로퍼티 사용

class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius


c = Circle(4.0)
c.radius
# 4.0
c.area
# Computing area
# 50.26548245743669
c.perimeter
# Computing perimeter
# 25.132741228718345
c.perimeter
# 25.132741228718345


# 토론

c = Circle(4.0)
# 인스턴스 변수 구하기
vars(c)
# {'radius': 4.0}

# 면적을 계산하고 추후 변수 확인
c.area
# Computing area
# 50.26548245743669
vars(c)
# {'radius': 4.0, 'area': 50.26548245743669}

# 속성에 접근해도 더 이상 프로퍼티를 실행하지 않는다.
c.area
# 50.26548245743669

# 변수를 삭제하고 프로퍼티가 다시 실행됨을 확인한다.
del c.area
vars(c)
# {'radius': 4.0}
c.area
# Computing area
# 50.26548245743669


c.area
# Computing area
# 50.26548245743669
c.area = 25
c.area
# 25


def lazyproperty(func):
    name = '_lazy_' + func.__name__
    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            value = func(self)
            setattr(self, name, value)
            return value
    return lazy


c = Circle(4.0)
c.area
# Computing area
# 50.26548245743669
c.area
# 50.26548245743669
c.area = 25
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: can't set attribute
