# 8.7 부모 클래스의 메소드 호출

class A:
    def spam(self):
        print('A.spam')

class B(A):
    def spam(self):
        print('B.spam')
        super().spam()          # 부모의 spam() 호출


class A:
    def __init__(self):
        self.x = 0

class B(A):
    def __init__(self):
        super().__init__()
        self.y = 1


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # 내부 obj를 위해 델리게이트(delegate) 속성 찾기
    def __getattr__(self, name):
        return getattr(self._obj, name)

    # 델리게이트(delegate) 속성 할당
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)  # 원본 __setattr__ 호출
        else:
            setattr(self._obj, name, value)


# 토론

class Base:
    def __init__(self):
        print('Base.__init__')

class A(Base):
    def __init__(self):
        Base.__init__(self)
        print('A.__init__')


class Base:
    def __init__(self):
        print('Base.__init__')

class A(Base):
    def __init__(self):
        Base.__init__(self)
        print('A.__init__')

class B(Base):
    def __init__(self):
        Base.__init__(self)
        print('B.__init__')

class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print('C.__init__')


c = C()
# Base.__init__
# A.__init__
# Base.__init__
# B.__init__
# C.__init__


class Base:
    def __init__(self):
        print('Base.__init__')

class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')

class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')

class C(A,B):
    def __init__(self):
        super().__init__()      # 여기서 super()를 한 번만 호출한다.
        print('C.__init__')


c = C()
# Base.__init__
# B.__init__
# A.__init__
# C.__init__


C.__mro__
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Base'>, <class 'object'>)


class A:
    def spam(self):
        print('A.spam')
        super().spam()


a = A()
a.spam()
# A.spam
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 4, in spam
# AttributeError: 'super' object has no attribute 'spam'


class B:
    def spam(self):
        print('B.spam')

class C(A,B):
    pass

c = C()
c.spam()
# A.spam
# B.spam


C.__mro__
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
