# 9.17 클래스 코딩 규칙 강제

class MyMeta(type):
    def __new__(self, clsname, bases, clsdict):
        # clsname은 정의하려는 클래스 이름
        # bases는 베이스 클래스의 튜플
        # clsdict는 클래스 딕셔너리
        return super().__new__(cls, clsname, bases, clsdict)


class MyMeta(type):
    def __init__(self, clsname, bases, clsdict):
        super().__init__(clsname, bases, clsdict)
        # clsname은 정의하려는 클래스 이름
        # bases는 베이스 클래스의 튜플
        # clsdict는 클래스 딕셔너리


class Root(metaclass=MyMeta):
    pass

class A(Root):
    pass

class B(Root):
    pass


class NoMixedCaseMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        for name in clsdict:
            if name.lower() != name:
                raise TypeError('Bad attribute name: ' + name)
        return super().__new__(cls, clsname, bases, clsdict)

class Root(metaclass=NoMixedCaseMeta):
    pass

class A(Root):
    def foo_bar(self):    # 허용
        pass

class B(Root):
    def fooBar(self):     # 에러
        pass


from inspect import signature
import logging

class MatchSignaturesMeta(type):
    def __init__(self, clsname, bases, clsdict):
        super().__init__(clsname, bases, clsdict)
        sup = super(self, self)
        for name, value in clsdict.items():
            if name.startswith('_') or not callable(value):
                continue
            # (있다면) 앞의 정의를 가져와서 시그니처를 비교한다.
            prev_dfn = getattr(sup,name,None)
            if prev_dfn:
                prev_sig = signature(prev_dfn)
                val_sig = signature(value)
                if prev_sig != val_sig:
                    logging.warning('Signature mismatch in %s. %s != %s',
                                    value.__qualname__, prev_sig, val_sig)

# 예제
class Root(metaclass=MatchSignaturesMeta):
    pass

class A(Root):
    def foo(self, x, y):
        pass

    def spam(self, x, *, z):
        pass

# 재정의한 메소드가 있는 클래스. 하지만 시그니처가 조금 다르다.
class B(A):
    def foo(self, a, b):
        pass

    def spam(self,x,z):
        pass


# WARNING:root:Signature mismatch in B.foo. (self, x, y) != (self, a, b)
# WARNING:root:Signature mismatch in B.spam. (self, x, *, z) != (self, x, z)



# 토론
