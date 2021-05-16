# 12.1 스레드 시작과 정지

# 개별 스레드에서 실행할 코드
import time
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)

# 스레드 생성과 실행
from threading import Thread
t = Thread(target=countdown, args=(10,))
t.start()


if t.is_alive():
    print('Still running')
else:
    print('Completed')


t.join()


t = Thread(target=countdown, args=(10,), daemon=True)
t.start()


class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(5)
c = CountdownTask()
t = Thread(target=c.run, args=(10,))
t.start()
...
c.terminate() # 종료 지시
t.join()      # 실제 종료까지 기다림(필요한 경우)


class IOTask:
    def terminate(self):
        self._running = False

    def run(self, sock):
        # sock은 소켓이다.
        sock.settimeout(5)      # 타임아웃 시간 설정
        while self._running:
            # 실행이 멈추는 입출력을 타임아웃과 함께 수행
            try:
                data = sock.recv(8192)
                break
            except socket.timeout:
                continue
            # 계속된 처리
            ...
        # 종료
        return



# 토론

from threading import Thread

class CountdownThread(Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n
    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)
c = CountdownThread(5)
c.start()


import multiprocessing
c = CountdownThread(5)
p = multiprocessing.Process(target=c.run)
p.start()
...
