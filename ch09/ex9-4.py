# 9.4 매개변수를 받는 데코레이터 정의

from functools import wraps
import logging

def logged(level, name=None, message=None):
    '''
    함수에 로깅 추가. level은 로깅 레벨, name은
    로거 이름, message는 로그 메시지. name과
    message가 명시되지 않으면 함수의 모듈 이름을
    기본 값으로 한다.
    '''
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate

# 사용 예
@logged(logging.DEBUG)
def add(x, y):
    return x + y

@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')



# 토론

@decorator(x, y, z)
def func(a, b):
    pass


def func(a, b):
    pass

func = decorator(x, y, z)(func)
