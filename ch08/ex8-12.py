# 8.12 인터페이스, 추상 베이스 클래스 정의

from abc import ABCMeta, abstractmethod

class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass
    @abstractmethod
    def write(self, data):
        pass


a = IStream()    # TypeError: 추상 메소드 read, write를 포함한
                 # 추상 클래스 IStream을 인스턴스화할 수 없음


class SocketStream(IStream):
    def read(self, maxbytes=-1):
        ...
    def write(self, data):
        ...


def serialize(obj, stream):
    if not isinstance(stream, IStream):
        raise TypeError('Expected an IStream')
    ...


import io

# 내장 I/O 클래스를 우리의 인터페이스를 지원하도록 등록
IStream.register(io.IOBase)

# 일반 파일을 열고 타입 확인
f = open('foo.txt')
isinstance(f, IStream)      # True 반환


from abc import ABCMeta, abstractmethod

class A(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @classmethod
    @abstractmethod
    def method1(cls):
        pass

    @staticmethod
    @abstractmethod
    def method2():
        pass


# 토론

import collections

# x가 시퀀스인지 확인
if isinstance(x, collections.Sequence):
    ...

# x가 순환 가능한지 확인
if isinstance(x, collections.Iterable):
    ...

# x에 크기가 있는지 확인
if isinstance(x, collections.Sized):
    ...

# x가 매핑인지 확인
if isinstance(x, collections.Mapping):
    ...


from decimal import Decimal
import numbers

x = Decimal('3.4')
isinstance(x, numbers.Real)     # False 반환
