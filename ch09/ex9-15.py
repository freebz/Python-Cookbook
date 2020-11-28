# 9.15 옵션 매개변수를 받는 메타클래스 정의

from abc import ABCMeta, abstractmethod

class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxsize=None):
        pass

    @abstractmethod
    def write(self, data):
        pass


class Spam(metaclass=MyMeta, debug=True, synchronize=True):
    ...


class MyMeta(type):
    # 옵션
    @classmethod
    def __prepare__(cls, name, bases, *, debug=False, synchronize=False):
        # 커스텀 처리
        ...
        return super().__prepare__(name, bases)

    # 필수
    def __new__(cls, name, bases, ns, *, debug=False, synchronize=False):
        # 커스텀 처리
        ...
        return super().__new__(cls, name, bases, ns)

    # 필수
    def __init__(self, name, bases, ns, *, debug=False, synchronize=False):
        # 커스텀 처리
        ...
        super().__init__(name, bases, ns)



# 토론

class Spam(metaclass=MyMeta):
    debug = True
    synchronize = True
    ...
