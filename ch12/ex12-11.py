# 12.11 메시지 출판/구독 구현

from collections import defaultdict

class Exchange:
    def __init__(self):
        self._subscribers = set()

    def attach(self, task):
        self._subscribers.add(task)

    def detach(self, task):
        self._subscribers.remove(task)

    def send(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)

# 생성된 모든 교환의 딕셔너리
_exchanges = defaultdict(Exchange)

# Exchange 인스턴스와 주어진 이름을 반환
def get_exchange(name):
    return _exchanges[name]


# 작업 예제. send() 메소도가 있는 객체

class Task:
    ...
    def send(self, msg):
        ...

task_a = Task()
task_b = Task()

# 교환을 얻는 예제
exc = get_exchange('name')

# 작업을 구독하는 예제
exc.attach(task_a)
exc.attach(task_b)

# 메시지를 전송하는 예제
exc.send('msg1')
exc.send('msg2')

# 구독을 해제하는 예제
exc.detach(task_a)
exc.detach(task_b)



# 토론

class DisplayMessages:
    def __init__(self):
        self.count = 0
    def send(self, msg):
        self.count += 1
        print('msg[{}]: {!r}'.format(self.count, msg))

exc = get_exchange('name')
d = DisplayMessages()
exc.attach(d)


exc = get_exchange('name')
exc.attach(some_task)
try:
    ...
finally:
    exc.detach(some_task)


from contextlib import contextmanager
from collections import defaultdict

class Exchange:
    def __init__(self):
        self._subscribers = set()

    def attach(self, task):
        self._subscribers.add(task)

    def detach(self, task):
        self._subscribers.remove(task)

    @contextmanager
    def subscribe(self, *tasks):
        for task in tasks:
            self.attach(task)
        try:
            yield
        finally:
            for task in tasks:
                self.detach(task)

    def send(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)

# 생성된 모든 교환의 딕셔너리
_exchanges = defaultdict(Exchange)

# Exchange 인스턴스와 주어진 이름을 반환
def get_exchange(name):
    return _exchanges[name]

# subscribe() 메소드를 사용하는 예제
exc = get_exchange('name')
with exc.subscribe(task_a, task_b):
    ...
    exc.send('msg1')
    exc.send('msg2')
    ...

# task_a와 task_b 연결이 여기서 끊어진다.
