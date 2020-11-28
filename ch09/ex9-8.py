# 9.8 데코레이터를 클래스의 일부로 정의

from functools import wraps

class A:
    # 인스턴스 메소드 데코레이터
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 1')
            return func(*args, **kwargs)
        return wrapper

    # 클래스 메소드 데코레이터
    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 2')
            return func(*args, **kwargs)
        return wrapper


# 인스턴스 메소드로
a = A()

@a.decorator1
def spem():
    pass

# 클래스 메소드로
@A.decorator2
def grok():
    pass



# 토론

class Person:
    # 프로퍼티 인스턴스 생성
    first_name = property()

    # 데코레이터 메소드 적용
    @first_name.getter
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value


class B(A):
    @A.decorator2
    def bar(self):
        pass
