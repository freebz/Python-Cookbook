# 14.12 프로그램 크래시 디버깅

# sample.py

def func(n):
    return n + 10

func('Hello')


# python3 -i sample.py
# Traceback (most recent call last):
#   File "ex14-12.py", line 8, in <module>
#     func('Hello')
#   File "ex14-12.py", line 6, in func
#     return n + 10
# TypeError: can only concatenate str (not "int") to str
# >>> func(10)
# 20


# >>> import pdb
# >>> pdb.pm()
# > sample.py(4)func()
# -> return n + 10
# (Pdb) w
#   sample.py(6)<module>()
# -> func('Hello')
# > sample.py(4)func()
# -> return n + 10
# (Pdb) print n
# 'Hello'
# (Pdb) q
# >>> 


import traceback
import sys

try:
    func(arg)
except:
    print('**** AN ERROR OCCURRED ****')
    traceback.print_exc(file=sys.stderr)


def sample(n):
    if n > 0:
        sample(n-1)
    else:
        traceback.print_stack(file=sys.stderr)

sample(5)
  # File "<stdin>", line 1, in <module>
  # File "<stdin>", line 3, in sample
  # File "<stdin>", line 3, in sample
  # File "<stdin>", line 3, in sample
  # [Previous line repeated 2 more times]
  # File "<stdin>", line 5, in sample


import pdb

def func(arg):
    ...
    pdb.set_trace()
    ...



# 토론
