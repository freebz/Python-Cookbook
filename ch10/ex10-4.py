# 10.4 모듈을 여러 파일로 나누기

# module.py

class A:
    def spam(self):
        print('A.spam')

class B(A):
    def bar(self):
        print('B.bar')


mymodule/
    __init__.py
    a.py
    b.py


# a.py

class A:
    def spam(self):
        print('A.spam')


# b.py

from .a import A

class B(A):
    def bar(self):
        print('B.bar')


# __init__.py

from .a import A
from .b import B


import mymodule
a = mymodule.A()
a.spam()
# A.spam
b = mymodule.B()
b.bar()
# B.bar



# 토론

from mymodule.a import A
from mymodule.b import B
...


from mymodule import A, B


# __init__.py

def A():
    from .a import A
    return A()

def B():
    from .b import B
    return B()


import mymodule
a = mymodule.A()
a.spam()
# A.spam


if isinstance(x, mymodule.A):   # Error
    ...

if isinstance(x, mymodule.a.A): # OK
    ...
