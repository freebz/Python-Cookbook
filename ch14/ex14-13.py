# 14.13 프로파일링과 타이밍

# timethis.py

import time
from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print('{}.{} : {}'.format(func.__module__, func.__name__, end - start))
        return r
    return wrapper


@timethis
def countdown(n):
    while n > 0:
        n -= 1

countdown(10000000)
# __main__.countdown : 0.5711494580027647


from contextlib import contextmanager

@contextmanager
def timeblock(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        print('{} : {}'.format(label, end - start))


with timeblock('counting'):
    n = 10000000
    while n > 0:
        n -= 1

# counting : 1.274623901990708


from timeit import timeit
timeit('math.sqrt(2)', 'import math')
# 0.10344699601409957
timeit('sqrt(2)', 'from math import sqrt')
# 0.07808520499384031


timeit('math.sqrt(2)', 'import math', number=10000000)
# 0.9226911370060407
timeit('sqrt(2)', 'from math import sqrt', number=10000000)
# 0.5504639690043405



# 토론

from functools import wraps
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.process_time()
        r = func(*args, **kwargs)
        end = time.process_time()
        print('{}.{} : {}'.format(func.__module__, func.__name__, end - start))
        return r
    return wrapper
