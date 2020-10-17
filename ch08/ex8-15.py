# 8.15 속성 접근 델리게이팅

class A:
    def spam(self, x):
        pass

    def foo(self):
        pass

class B:
    def __init__(self):
        self._a = A()

    def spam(self, x):
        # 내부 self._a 인스턴스로 델리게이트
        return self._a.spam(x)

    def foo(self):
        # 내부 self._a 인스턴스로 델리게이트
        return self._a.foo()

    def bar(self):
        pass


class A:
    def spam(self, x):
        pass

    def foo(self):
        pass

class B:
    def __init__(self):
        self._a = A()

    def bar(self):
        pass

    # A 클래스에 정의한 모든 메소드를 노출한다.
    def __getattr__(self, name):
        return getattr(self._a, name)


b = B()
b.bar()    # B.bar() 호출 (B에 존재함.)
b.spam(42) # B.__getattr__('spam') 호출하고 A.spam으로 델리게이트


# 다른 객체를 감싸는 프록시 클래스, 하지만
# public 속성을 노출한다.

class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # 속성 검색을 내부 객체로 델리게이트
    def __getattr__(self, name):
        print('getattr:', name)
        return getattr(self._obj, name)

    # 속성 할당 델리게이트
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            print('setattr:', name, value)
            setattr(self._obj, name, value)

    # 속성 삭제 델리게이트
    def __delattr__(self, name):
        if name.startswith('_'):
            super().__delattr__(name)
        else:
            print('delattr:', name)
            delattr(self._obj, name)


class Spam:
    def __init__(self, x):
        self.x = x
    def bar(self, y):
        print('Spam.bar:', self.x, y)

# 인스턴스 생성
s = Spam(2)

# 프록시를 만들고 감싸기
p = Proxy(s)

# 프록시에 접근
print(p.x)    # 2 출력
p.bar(3)      # "Spam.bar: 2 3" 출력
p.x = 37      # s.x를 37로 변경


# 토론

class A:
    def spam(self, x):
        print('A.spam', x)

    def foo(self):
        print('A.foo')

class B:
    def spam(self, x):
        print('B.spam')
        super().spam(x)

    def bar(self):
        print('B.bar')


class A:
    def spam(self, x):
        print('A.spam', x)

    def foo(self):
        print('A.foo')

class B:
    def __init__(self):
        self._a = A()

    def spam(slef, x):
        print('B.spam', x)
        self._a.spam(x)

    def bar(self):
        print('B.bar')

    def __getattr__(self, name):
        return getattr(self._a, name)


class ListLike:
    def __init__(self):
        self._items = []
    def __getattr__(self, name):
        return getattr(self._items, name)


a = ListLike()
a.append(2)
a.insert(0, 1)
a.sort()
len(a)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: object of type 'ListLike' has no len()
a[0]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'ListLike' object does not support indexing


class ListLike:
    def __init__(self):
        self._items = []
    def __getattr__(self, name):
        return getattr(self._items, name)

    # 특정 리스트 연산을 지원하기 위한 특별 메소드 추가
    def __len__(self):
        return len(self._items)
    def __getitem__(self, index):
        return self._items[index]
    def __setitem__(self, index, value):
        self._items[index] = value
    def __delitem__(self, index):
        del self._items[index]
