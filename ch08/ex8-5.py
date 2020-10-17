# 8.5 클래스 이름의 캡슐화

class A:
    def __init__(self):
        self._internal = 0      # 내부 속성
        self.public = 1         # 공용 속성

    def public_method(self):
        '''
        A public method
        '''
        ...

    def _internal_method(self):
        ...


class B:
    def __init__(self):
        self.__private = 0
    def __private_method(self):
        ...
    def public_method(self):
        ...
        self.__private_method()
        ...


class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1      # B.__private를 오버라이드하지 않는다.
    # B.__private_method()를 오버라이드하지 않는다.
    def __private_method(self):
        ...


# 토론

lambda_ = 2.0       # lambda 키워드와의 충돌을 피하기 위해 밑줄을 붙인다.
