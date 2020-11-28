# 9.5 사용자가 조절 가능한 속성을 가진 데코레이터 정의

from functools import wraps, partial
import logging

# obj의 속성으로 함수에 붙이는 유틸리티 데코레이터
def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func

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

        # 세터 함수 첨부
        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg
                
        return wrapper
    return decorate

# 사용 예
@logged(logging.DEBUG)
def add(x, y):
    return x + y

@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')


import logging
logging.basicConfig(level=logging.DEBUG)
add(2, 3)
# DEBUG:__main__:add
# 5

# Change the log message
add.set_message('Add called')
add(2, 3)
# DEBUG:__main__:Add called
# 5

# Change the log level
add.set_level(logging.WARNING)
add(2, 3)
# WARNING:__main__:Add called
# 5



# 토론

@timethis
@logged(logging.DEBUG)
def countdown(n):
    while n > 0:
        n -= 1


countdown(10000000)
# DEBUG:__main__:countdown
# countdown 0.5865683555603027
countdown.set_level(logging.WARNING)
countdown.set_message("Counting down to zero")
countdown(10000000)
# WARNING:__main__:Counting down to zero
# countdown 0.5604653358459473


@logged(logging.DEBUG)
@timethis
def countdown(n):
    while n > 0:
        n -= 1


...
@attach_wrapper(wrapper)
def get_level():
    return level

# Alternative
wrapper.get_level = lambda: level
...


...
@wraps(func)
def wrapper(*args, **kwargs):
    wrapper.log.log(wrapper.level, wrapper.logmsg)
    return func(*args, **kwargs)

# 조절 가능한 속성 추가
wrapper.level = level
wrapper.logmsg = logmsg
wrapper.log = log
...
