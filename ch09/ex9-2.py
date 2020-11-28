# 9.2 데코레이터 작성 시 함수 메타데이터 보존

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
def countdown(n:int):
    '''
    Counts down
    '''
    while n > 0:
        n -= 1

countdown(100000)
# countdown 0.007936954498291016
countdown.__name__
# 'countdown'
countdown.__doc__
# '\n\tCounts down\n\t'
countdown.__annotations__
# {'n': <class 'int'>}



# 토론

countdown.__name__
# 'wrapper'
countdown.__doc__
countdown.__annotations__
# {}


countdown.__wrapped__(100000)


from inspect import signature
print(signature(countdown))
# (n:int)
