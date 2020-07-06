# 7.12 클로저 내부에서 정의한 변수에 접근

def sample():
    n = 0
    # 클로저 함수
    def func():
        print('n=', n)

    # n에 대한 접근 메소드
    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    # 함수 속성으로 클로저에 붙임
    func.get_n = get_n
    func.set_n = set_n
    return func


f = sample()
f()
# n= 0
f.set_n(10)
f()
# n= 10
f.get_n()
# 10


# 토론

import sys
class ClosureInstance:
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals

        # 인스턴스 딕셔너리를 호출체로 갱신
        self.__dict__.update((key,value) for key, value in locals.items()
                             if callable(value) )
    # 특별 메소드 리다이렉트(redirect)
    def __len__(self):
        return self.__dict__['__len__']()

# 사용 예제
def Stack():
    items = []

    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()


s = Stack()
s
# <__main__.ClosureInstance object at 0x7f0abbd235f8>
s.push(10)
s.push(20)
s.push('Hello')
len(s)
# 3
s.pop()
# 'Hello'
s.pop()
# 20
s.pop()
# 10


class Stack2:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)


from timeit import timeit
# 클로저
s = Stack()
timeit('s.push(1);s.pop()', 'from __main__ import s')
# 0.45524884199767257
# 클래스
s = Stack2()
timeit('s.push(1);s.pop()', 'from __main__ import s')
# 0.5234481600018626
