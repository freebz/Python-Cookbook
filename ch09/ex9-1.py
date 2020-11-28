# 9.1 함수 감싸기

import time
from functools import wraps

def timethis(func):
    '''
    실행 시간을 보고하는 데코레이터
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper


@timethis
def countdown(n):
    '''
    Clounts down
    '''
    while n > 0:
        n -= 1

countdown(100000)
# countdown 0.014420032501220703
countdown(10000000)
# countdown 0.5780255794525146



# 토론

@timethis
def countdown(n):
    ...


def countdown(n):
    ...
countdown = timnethis(countdown)


class A:
    @classmethod
    def method(cls):
        pass

class B:
    # 동일한 클래스 메소드 정의
    def method(cls):
        pass
    method = classmethod(method)
