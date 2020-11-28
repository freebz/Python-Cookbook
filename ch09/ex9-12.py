# 9.12 클래스 정의 패치에 데코레이터 사용

def log_getattribute(cls):
    # 원본 구현 얻기
    orig_getattribute = cls.__getattribute__

    # 새로운 정의 생성
    def new_getattribute(self, name):
        print('getting:', name)
        return orig_getattribute(self, name)

    # 클래스에 붙이고 반환
    cls.__getattribute__ = new_getattribute
    return cls

# 사용 예제
@log_getattribute
class A:
    def __init__(self,x):
        self.x = x
    def spam(self):
        pass


a = A(42)
a.x
# getting: x
# 42
a.spam()
# getting: spam



# 토론

class LoggedGetattribute:
    def __getattribute__(self, name):
        print('getting:', name)
        return super().__getattribute__(name)

# 예제:
class A(LoggedGetattribute):
    def __init__(self,x):
        self.x = x
    def spam(self):
        pass
