# 9.6 옵션 매개변수를 받는 데코레이터 정의

from functools import wraps, partial
import logging

def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)

    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)
    return wrapper

# 사용 예
@logged
def add(x, y):
    return x + y

@logged(level=logging.CRITICAL, name='example')
def spam():
    print('Spam!')



# 토론

@logged()
def add(x, y):
    return x+y


# 사용 예
@logged
def add(x, y):
    return x + y


def add(x, y):
    return x + y
add = logged(add)


@logged(level=logging.CRITICAL, name='example')
def spam():
    print('Spam!')
spam = logged(level=logging.CRITICAL, name='example')(spam)

