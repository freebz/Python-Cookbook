# 9.10 클래스와 스태틱 메소드에 데코레이터 적용

import time
from functools import wraps

# 간단한 데코레이터
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(end-start)
        return r
    return wrapper

# 서로 다른 메소드에 데코레이터를 적용하는 모습을 보여주기 위한 클래스
class Spam:
    @timethis
    def instance_method(self, n):
        print(self, n)
        while n > 0:
            n -= 1

    @classmethod
    @timethis
    def class_method(cls, n):
        print(cls, n)
        while n > 0:
            n -= 1

    @staticmethod
    @timethis
    def static_method(n):
        print(n)
        while n > 0:
            n -= 1


s = Spam()
s.instance_method(1000000)
# <__main__.Spam object at 0x7f2211d7cfd0> 1000000
# 0.07807445526123047
Spam.class_method(1000000)
# <class '__main__.Spam'> 1000000
# 0.09068417549133301
Spam.static_method(1000000)
# 1000000
# 0.08837485313415527



# 토론

class Spam:
    ...
    @timethis
    @staticmethod
    def static_method(n):
        print(n)
        while n > 0:
            n -= 1


Spam.static_method(1000000)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "timethis.py", line 6, in wrapper
#     r = func(*args, **kwargs)
# TypeError: 'staticmethod' object is not callable


from abc import ABCMeta, abstractmethod

class A(methodclass=ABCMeta):
    @classmethod
    @abstractmethod
    def method(cls):
        pass
