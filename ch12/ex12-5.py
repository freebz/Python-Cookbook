# 12.5 락킹으로 데드락 피하기

import threading
from contextlib import contextmanager

# 이미 취득한 락에 대한 정보를 저장하기 위한 스레드-로컬 상태(thread-local state)
_local = threading.local()

@contextmanager
def acquire(*locks):
    # 객체 식별자로 락 정렬
    locks = sorted(locks, key=lambda x: id(x))

    # 이미 취득한 락의 락 순서가 깨지지 않도록 주의
    acquired = getattr(_local,'acquired',[])
    if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):
        raise RuntimeError('Lock Order Violation')

    # 모든 락 취득
    acquired.extend(locks)
    _local.acquired = acquired
    try:
        for lock in locks:
            lock.acquire()
        yield
    finally:
        # 취득한 반대 순서로 락 해제
        for lock in reversed(locks):
            lock.release()
        del acquired[-len(locks):]


import threading
x_lock = threading.Lock()
y_lock = threading.Lock()

def thread_1():
    while True:
        with acquire(x_lock, y_lock):
            print('Thread-1')

def thread_2():
    while True:
        with acquire(y_lock, x_lock):
            print('Thread-2')

t1 = threading.Thread(target=thread_1)
t1.daemon = True
t1.start()

t2 = threading.Thread(target=thread_2)
t2.daemon = True
t2.start()


import threading
x_lock = threading.Lock()
y_lock = threading.Lock()

def thread_1():
    while True:
        with acquire(x_lock):
            with acquire(y_lock):
                print('Thread-1')

def thread_2():
    while True:
        with acquire(y_lock):
            with acquire(x_lock):
                print('Thread-2')

t1 = threading.Thread(target=thread_1)
t1.daemon = True
t1.start()

t2 = threading.Thread(target=thread_2)
t2.daemon = True
t2.start()

# Exception in thread Thread-1:



# 토론

import threading

# 철학자 스레드
def philosopher(left, right):
    while True:
        with acquire(left,right):
            print(threading.currentThread(), 'eating')

# 젓가락 (락으로 표현됨)
NSTICKS = 5
chopsticks = [threading.Lock() for n in range(NSTICKS)]

# 모든 철학자 생성
for n in range(NSTICKS):
    t = threading.Thread(target=philosopher,
                         args=(chopsticks[n],chopsticks[(n+1) % NSTICKS]))
    t.start()
