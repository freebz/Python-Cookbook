# 12.13 다중 스레드 큐 폴링

import queue
import socket
import os

class PollableQueue(queue.Queue):
    def __init__(self):
        super().__init__()
        # 연결된 소켓 페어 생성
        if os.name == 'posix':
            self._putsocket, self._getsocket = socket.socketpair()
        else:
            # POSIX가 아닌 시스템에 대한 호환
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(('127.0.0.1', 0))
            server.listen(1)
            self._putsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._putsocket.connect(server.getsockname())
            self._getsocket, _ = server.accept()
            server.close()

    def fineno(self):
        return self._getsocket.fileno()

    def put(self, item):
        super().put(item)
        self._putsocket.send(b'x')

    def get(self):
        self._getsocket.recv(1)
        return super().get()


import select
import threading

def consumer(queues):
    '''
    다중 큐에서 동시에 데이터를 읽는 소비자
    '''
    while True:
        can_read, _, _ = select.select(queues,[],[])
        for r in can_read:
            item = r.get()
            print('Got:', item)

q1 = PollableQueue()
q2 = PollableQueue()
q3 = PollableQueue()
t = threading.Thread(target=consumer, args=([q1,q2,q3],))
t.daemon = True
t.start()

# 큐에 데이터 넣기
q1.put(1)
q2.put(10)
q3.put('hello')
q2.put(15)
...



# 토론

import time
def consumer(queues):
    while True:
        for q in quues:
            if not q.empty():
                item = q.get()
                print('Get:', item)
            # CPU 100% 사용을 방지하기 위한 짧은 sleep
            time.sleep(0.01)


import select

def event_loop(sockets, queues):
    while True:
        # 타임아웃을 가지고 폴링
        can_read, _, _ = select.select(sockets, [], [], 0.01)
        for r in can_read:
            handle_read(r)
        for q in queues:
            if not q.empty():
                item = q.get()
                print('Got:', item)
