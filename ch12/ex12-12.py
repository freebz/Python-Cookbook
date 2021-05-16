# 12.12 스레드의 대안으로 제너레이터 사용

# 간단한 제너레이터 함수 두 가지
def countdown(n):
    while n > 0:
        print('T-minus', n)
        yield
        n -= 1
    print('Blastoff!')

def countup(n):
    x = 0
    while x < n:
        print('Counting up', x)
        yield
        x += 1


from collections import deque

class TaskScheduler:
    def __init__(self):
        self._task_queue = deque()

    def new_task(self, task):
        '''
        새롭게 시작한 작업을 스케줄러에 등록
        '''
        self._task_queue.append(task)

    def run(self):
        '''
        작업이 없을 때까지 실행
        '''
        while self._task_queue:
            task = self._task_queue.popleft()
            try:
                # 다음 yield 구문까지 작업을 실행
                next(task)
                self._task_queue.append(task)
            except StopIteration:
                # 제너레이터가 더 이상 실행 중이지 않다.
                pass

# 사용 예제
sched = TaskScheduler()
sched.new_task(countdown(10))
sched.new_task(countdown(5))
sched.new_task(countup(15))
sched.run()


# T-minus 10
# T-minus 5
# Counting up 0
# T-minus 9
# T-minus 4
# Counting up 1
# T-minus 8
# T-minus 3
# Counting up 2
# T-minus 7
# T-minus 2
# ...


from collections import deque

class ActorScheduler:
    def __init__(self):
        self._actors = { }           # 이름을 액터에 매핑
        self._msg_queue = deque()    # 메시지 큐

    def new_actor(self, name, actor):
        '''
        새롭게 시작한 액터를 스케줄러에 등록하고 이름을 짓는다.
        '''
        self._msg_queue.append((actor,None))
        self._actors[name] = actor

    def send(self, name, msg):
        '''
        이름 있는 액터에 메시지 전송
        '''
        actor = self._actors.get(name)
        if actor:
            self._msg_queue.append((actor,msg))

    def run(self):
        '''
        지연 중인 메시지가 있으면 실행
        '''
        while self._msg_queue:
            actor, msg = self._msg_queue.popleft()
            try:
                actor.send(msg)
            except StopIteration:
                pass

# 사용 예제
if __name__ == '__main__':
    def printer():
        while True:
            msg = yield
            print('Got:', msg)

    def counter(sched):
        while True:
            # 현재 카운트 받기
            n = yield
            if n == 0:
                break
            # 프린터 작업에 전송
            sched.send('printer', n)
            # 다음 카운트를 카운터 작업에 전송(재귀적)
            sched.send('counter', n-1)

    sched = ActorScheduler()
    # 초기 액터 생성
    sched.new_actor('printer', printer())
    sched.new_actor('counter', counter(sched))

    # 시작하기 위해 초기 메시지를 카운터에 전송
    sched.send('counter', 10000)
    sched.run()


from collections import deque
from select import select

# 이 클래스는 스케줄러에서 일반적인 yield 이벤트를 표시한다.
class YieldEvent:
    def handle_yield(self, sched, task):
        pass
    def handle_resume(self, sched, task):
        pass

# 작업 스케줄러
class Scheduler:
    def __init__(self):
        self._numtasks = 0         # 작업 개수
        self._ready = deque()      # 실행 준비가 된 작업
        self._read_waiting = {}    # 읽기 대기 중인 작업
        self._write_waiting = {}   # 쓰기 대기 중인 작업

    # 입출력 이벤트를 폴링하고 기다리기 동작을 재시작한다.
    def _iopoll(self):
        rset,wset,eset = select(self._read_waiting,
                                self._write_waiting,[])
        for r in rset:
            evt, task = self._read_waiting.pop(r)
            evt.handle_resume(self, task)
        for w in wset:
            evt, task = self._write_waiting.pop(w)
            evt.handle_resume(self, task)

    def new(self,task):
        '''
        새롭게 시작한 작업을 스케줄러에 등록
        '''
        self._ready.append((task, None))
        self._numtasks += 1

    def add_ready(self, task, msg=None):
        '''
        이미 시작한 작업을 기다림 큐에 넣는다.
        msg는 다시 시작할 때 작업에 보내는 것이다.
        '''
        self._ready.append((task, msg))

    # 읽기 세트에 작업 추가
    def _read_wait(self, fileno, evt, task):
        self._read_waiting[fileno] = (evt, task)

    # 쓰기 세트에 작업 추가
    def _write_wait(self, fileno, evt, task):
        self._write_waiting[fileno] = (evt, task)

    def run(self):
        '''
        작업이 없을 때까지 작업 스케줄러 실행
        '''
        while self._numtasks:
            if not self._ready:
                self._iopoll()
            task, msg = self._ready.popleft()
            try:
                # 다음 yield에 코루틴 실행
                r = task.send(msg)
                if isinstance(r, YieldEvent):
                    r.handle_yield(self, task)
                else:
                    raise RuntimeError('unrecognized yield event')
            except StopIteration:
                self._numtasks -= 1

# 코루틴 기반 소켓 입출력 구현 예제
class ReadSocket(YieldEvent):
    def __init__(self, sock, nbytes):
        self.sock = sock
        self.nbytes = nbytes
    def handle_yield(self, sched, task):
        sched._read_wait(self.sock.fileno(), self, task)
    def handle_resume(self, sched, task):
        data = self.sock.recv(self.nbytes)
        sched.add_ready(task, data)

class WriteSocket(YieldEvent):
    def __init__(self, sock, data):
        self.sock = sock
        self.data = data
    def handle_yield(self, sched, task):
        sched._write_wait(self.sock.fileno(), self, task)
    def handle_resume(self, sched, task):
        nsent = self.sock.send(self.data)
        sched.add_ready(task, nsent)

class AcceptSocket(YieldEvent):
    def __init__(self, sock):
        self.sock = sock
    def handle_yield(self, sched, task):
        sched._read_wait(self.sock.fileno(), self, task)
    def handle_resume(self, sched, task):
        r = self.sock.accept()
        sched.add_ready(task, r)

# yield와 함께 사용하기 위해 소켓 객체를 감싸는 래퍼(wrapper)
class Socket(object):
    def __init__(self, sock):
        self._sock = sock
    def recv(self, maxbytes):
        return ReadSocket(self._sock, maxbytes)
    def send(self, data):
        return WriteSocket(self._sock, data)
    def accept(self):
        return AcceptSocket(self._sock)
    def __getattr__(self, name):
        return getattr(self._sock, name)

if __name__ == '__main__':
    from socket import socket, AF_INET, SOCK_STREAM
    import time

    # 제너레이터 관련 함수 예제
    # 이 함수는 yield from readline(sock)과 함께 호출해야 한다.
    def readline(sock):
        chars = []
        while True:
            c = yield sock.recv(1)
            if not c:
                break
            chars.append(c)
            if c == b'\n':
                break
        return b''.join(chars)

    # 제너레이터를 사용한 에코 서버
    class EchoServer:
        def __init__(self,addr,sched):
            self.sched = sched
            sched.new(self.server_loop(addr))

        def server_loop(self,addr):
            s = Socket(socket(AF_INET,SOCK_STREAM))
            s.bind(addr)
            s.listen(5)
            while True:
                c,a = yield s.accept()
                print('Got connection from ', a)
                self.sched.new(self.client_handler(Socket(c)))

        def client_handler(self,client):
            while True:
                line = yield from readline(client)
                if not line:
                    break
                line = b'GOT:' + line
                while line:
                    nsent = yield client.send(line)
                    line = line[nsent:]
            client.close()
            print('Client closed')

    sched = Scheduler()
    EchoServer(('',16000),sched)
    sched.run()



# 토론

def some_generator():
    ...
    result = yield data
    ...


f = some_generator()

# 아직 아무것도 계산하지 않았기 때문에 초기 값은 None
result = None
while True:
    try:
        data = f.send(result)
        result = ... do some calculation ...
    except StopIteration:
        break
