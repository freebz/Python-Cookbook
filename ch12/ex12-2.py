# 12.2 스레드가 시작했는지 판단하기

from threading import Thread, Event
import time

# 독립된 스레드에서 실행할 코드
def countdown(n, started_evt):
    print('countdown starting')
    started_evt.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)

# 시작을 호출하는 데 사용할 이벤트 객체를 생성
started_evt = Event()

# 스레드를 실행하고 시작 이벤트에 전달
print('Launching countdown')
t = Thread(target=countdown, args=(10,started_evt))
t.start()

# 스레드가 시작하기를 기다림
started_evt.wait()
print('countdown is running')



# 토론

import threading
import time

class PeriodicTimer:
    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition()

    def start(self):
        t = threading.Thread(target=self.run)
        t.daemon = True
        t.start()

    def run(self):
        '''
        타이머를 실행하고 구간마다 기다리는 스레드에게 알림
        '''
        while True:
            time.sleep(self._interval)
            with self._cv:
                self._flag ^= 1
                self._cv.notify_all()

    def wait_for_tick(self):
        '''
        타이머의 다음 틱을 기다림
        '''
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                self._cv.wait()

# 타이머 사용 예제
ptimer = PeriodicTimer(5)
ptimer.start()

# 타이머에 싱크하는 두 스레드
def countdown(nticks):
    while nticks > 0:
        ptimer.wait_for_tick()
        print('T-minus', nticks)
        nticks -= 1

def countup(last):
    n = 0
    while n < last:
        ptimer.wait_for_tick()
        print('Counting', n)
        n += 1

threading.Thread(target=countdown, args=(10,)).start()
threading.Thread(target=countup, args=(5,)).start()


# 워커 스레드
def worker(n, sema):
    # 호출을 기다림
    sema.acquire()
    # 메시지 출력
    print('Working', n)

# 스레드 생성
sema = threading.Semaphore(0)
nworkers = 10
for n in range(nworkers):
    t = threading.Thread(target=worker, args=(n, sema,))
    t.start()
    
sema.release()
# Working 0
sema.release()
# Working 1
