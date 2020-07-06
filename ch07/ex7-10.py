# 7.10 콜백 함수에 추가적 상태 넣기

def apply_async(func, args, *, callback):
    # 결과 계산
    result = func(*args)

    # 결과 값으로 콜백 함수 호출
    callback(result)


def print_result(result):
    print('Got:', result)

def add(x, y):
    return x + y

apply_async(add, (2, 3), callback=print_result)
# Got: 5
apply_async(add, ('hello', 'world'), callback=print_result)
# Got: helloworld


class ResultHandler:
    def __init__(self):
        self.sequence = 0
    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))


r = ResultHandler()
apply_async(add, (2, 3), callback=r.handler)
# [1] Got: 5
apply_async(add, ('hello', 'world'), callback=r.handler)
# [2] Got: helloworld


def make_handler():
    sequence = 0
    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))
    return handler


handler = make_handler()
apply_async(add, (2, 3), callback=handler)
# [1] Got: 5
apply_async(add, ('hello', 'world'), callback=handler)
# [2] Got: helloworld


def make_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))


handler = make_handler()
next(handler)        # Advance to the yield
apply_async(add, (2, 3), callback=handler.send)
# [1] Got: 5
apply_async(add, ('hello', 'world'), callback=handler.send)
# [2] Got: helloworld


class SequenceNo:
    def __init__(self):
        self.sequence = 0

def handler(result, seq):
    seq.sequence += 1
    print('[{}] Got: {}'.format(seq.sequence, result))

seq = SequenceNo()
from functools import partial
apply_async(add, (2, 3), callback=partial(handler, seq=seq))
# [1] Got: 5
apply_async(add, ('hello', 'world'), callback=partial(handler, seq=seq))
# [2] Got: helloworld


# 토론

apply_async(add, (2, 3), callback=lambda r: handler(r, seq))
# [1] Got: 5
