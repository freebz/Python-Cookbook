# 9.9 클래스 데코레이터 정의

import types
from functools import wraps

class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


@Profiled
def add(x, y):
    return x + y

class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)


add(2, 3)
# 5
add(4, 5)
# 9
add.ncalls
# 2
s = Spam()
s.bar(1)
# <__main__.Spam object at 0x7f2211d757b8> 1
s.bar(2)
# <__main__.Spam object at 0x7f2211d757b8> 2
s.bar(3)
# <__main__.Spam object at 0x7f2211d757b8> 3
Spam.bar.ncalls
# 3



# 토론

s = Spam()
s.bar(3)
# Traceback (most recent call last):
# ...
# TypeError: spam() missing 1 required positional argument: 'x'


s = Spam()
def grok(self, x):
    pass

grok.__get__(s, Spam)
# <bound method grok of <__main__.Spam object at 0x7f2211d75e48>>


import types
from functools import wraps

def profiled(func):
    ncalls = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal ncalls
        ncalls += 1
        return func(*args, **kwargs)
    wrapper.ncalls = lambda: ncalls
    return wrapper

# 예제
@profiled
def add(x, y):
    return x + y


add(2, 3)
# 5
add(4, 5)
# 9
add.ncalls()
# 2
