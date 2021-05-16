# 12.3 스레드 간 통신

from queue import Queue
from threading import Thread

# 데이터를 생성하는 스레드
def producer(out_q):
    while True:
        # 데이터 생성
        ...
        out_q.put(data)

# 데이터를 소비하는 스레드
def consumer(in_q):
    while True:
        # 데이터 얻기
        data = in_q.get()
        # 데이터처 리
        ...

# 공유 큐를 만들고 양쪽 스레드 실행
q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()


from queue import Queue
from threading import Thread

# 종료 신호를 보내는 객체
_sentinel = object()

# 데이터를 생성하는 스레드
def producer(out_q):
    while running:
        # 데이터 생성
        ...
        out_q.put(data)

    # 큐에 센티넬을 넣어서 종료를 가리킨다.
    out_q.put(_sentinel)

# 데이터를 소비하는 스레드
def consumer(in_q):
    while True:
        # 데이터 얻기
        data = in_q.get()

        # 종료 확인
        if data is _sentinel:
            in_q.put(_sentinel)
            break

        # 데이터 처리
        ...


import heapq
import threading

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._count = 0
        self._cv = threading.Condition()
    def put(self, item, priority):
        with self._cv:
            heapq.heappush(self._queue, (-priority, self._count, item))
            self._count += 1
            self._cv.notify()

    def get(self):
        with self._cv:
            while len(self._queue) == 0:
                self._cv.wait()
            return heapq.heappop(self._queue)[-1]


from queue import Queue
from threading import Thread

# 데이터를 생성하는 스레드
def producer(out_q):
    while running:
        # 데이터 생성
        ...
        out_q.put(data)

# 데이터를 소비하는 스레드
def consumer(in_q):
    while True:
        # 데이터 얻기
        data = in_q.get()
        # 데이터 처리
        ...
        # 종료 알림
        in_q.task_done()

# 공유 큐를 만들고 양쪽 스레드 실행
q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()

# 생성한 모든 아이템을 소비할 때까지 기다림
q.join()


from queue import Queue
from threading import Thread, Event

# 데이터를 생성하는 스레드
def producer(out_q):
    while running:
        # 데이터 생성
        ...
        # (data, event) 페어를 만들고 소비자 측에 전달
        evt = Event()
        out_q.put((data, evt))
        ...
        # 소비자가 아이템을 처리할 때까지 기다림
        evt.wait()

# 데이터를 소비하는 스레드
def consumer(in_q):
    while True:
        # 데이터 얻기
        data, evt = in_q.get()
        # 데이터 처리
        ...
        # 종료 알림
        evt.set()



# 토론

from queue import Queue
from threading import Thread
import copy

# 데이터를 생성하는 스레드
def producer(out_q):
    while True:
        # 데이터 생성
        ...
        out_q.put(copy.deepcopy(data))

# 데이터를 소비하는 스레드
def consumer(in_q):
    while True:
        # 데이터 얻기
        data = in_q.get()
        # 데이터 처리
        ...


import queue
q = queue.Queue()

try:
    data = q.get(block=False)
except queue.Empty:
    ...

try:
    q.put(item, block=False)
except queue.Full:
    ...

try:
    data = q.get(timeout=5.0)
except queue.Empty:
    ...


def producer(q):
    ...
    try:
        q.put(item, block=False)
    except queue.Full:
        log.warning('queued item %r discarded!', item)


_running = True

def consumer(q):
    while _running:
        try:
            item = q.get(tiemout=5.0)
            # 아이템 처리
            ...
        except queue.Empty:
            pass
