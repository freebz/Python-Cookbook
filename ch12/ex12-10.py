# 12.10 액터 작업 정의

from queue import Queue
from threading import Thread, Event

# 종료에 사용하는 센티넬
class ActorExit(Exception):
    pass

class Actor:
    def __init__(self):
        self._mailbox = Queue()

    def send(self, msg):
        '''
        액터에 메시지 전송
        '''
        self._mailbox.put(msg)

    def recv(self):
        '''
        메시지 수신
        '''
        msg = self._mailbox.get()
        if msg is ActorExit:
            raise ActorExit()
        return msg

    def close(self):
        '''
        액터를 닫고, 종료
        '''
        self.send(ActorExit)

    def start(self):
        '''
        병렬 실행 시작
        '''
        self._terminated = Event()
        t = Thread(target=self._bootstrap)
        t.daemon = True
        t.start()

    def _bootstrap(self):
        try:
            self.run()
        except ActorExit:
            pass
        finally:
            self._terminated.set()

    def join(self):
        self._terminated.wait()

    def run(self):
        '''
        사용자가 구현한 메소드 실행
        '''
        while True:
            msg = self.recv()

# 샘플 액터 작업
class PrintActor(Actor):
    def run(self):
        while True:
            msg = self.recv()
            print('Got:', msg)

# 사용 예
p = PrintActor()
p.start()
p.send('Hello')
p.send('World')
p.close()
p.join()


def print_actor():
    while True:
        try:
            msg = yield      # 메시지 받기
            print('Got:', msg)
        except GeneratorExit:
            print('Actor terminating')

# 사용 예
p = print_actor()
next(p)      # yield하기 위한 진행(받을 준비가 됨)
p.send('Hello')
p.send('World')
p.close()



# 토론

class TaggedActor(Actor):
    def run(self):
        while True:
            tag, *payload = self.recv()
            getattr(self,'do_'+tag)(*payload)

    # 메시지 태그에 따른 메소드
    def do_A(self, x):
        print('Running A', x)

    def do_B(self, x, y):
        print('Running B', x, y)

# 예제
a = TaggedActor()
a.start()
a.send(('A', 1))       # do_A(1) 실행
a.send(('B', 2, 3))    # do_B(2,3) 실행


from threading import Event
class Result:
    def __init__(self):
        self._evt = Event()
        self._result = None

    def set_result(self, value):
        self._result = value
        self._evt.set()

    def result(self):
        self._evt.wait()
        return self._result

class Worker(Actor):
    def submit(self, func, *args, **kwargs):
        r = Result()
        self.send((func, args, kwargs, r))
        return r

    def run(self):
        while True:
            func, args, kwargs, r = self.recv()
            r.set_result(func(*args, **kwargs))

# 사용 예제
worker = Worker()
worker.start()
r = worker.submit(pow, 2, 3)
print(r.result())
