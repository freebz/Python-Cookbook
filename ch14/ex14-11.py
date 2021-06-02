# 14.11 경고 메시지 생성

import warnings

def func(x, y, logfile=None, debug=False):
    if logfile is not None:
        warnings.warn('logfile argument deprecated', DeprecationWarning)
    ...



# 토론

import warnings
warnings.simplefilter('always')
f = open('/etc/passwd')
del f
# <stdin>:1: ResourceWarning: unclosed file <_io.TextIOWrapper name='/etc/passwd' mode='r' encoding='UTF-8'>
# ResourceWarning: Enable tracemalloc to get the object allocation traceback
