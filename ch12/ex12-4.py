# 12.4 임계 영역 락

import threading

class SharedCounter:
    '''
    다중 스레드에서 공유 가능한 카운터 객체
    '''
    def __init__(self, initial_value = 0):
        self._value = initial_value
        self._value_lock = threading.Lock()

    def incr(self,delta=1):
        '''
        락과 함께 카운터 증가
        '''
        with self._value_lock:
            self._value += delta

    def decr(self,delta=1):
        '''
        락과 함께 카운터 감소
        '''
        with self._value_lock:
            self._value -= delta



# 토론

import threading

class SharedCounter:
    '''
    다중 스레드에서 공유 가능한 카운터 객체
    '''
    def __init__(self, initial_value = 0):
        self._value = initial_value
        self._value_lock = threading.Lock()

    def incr(self,delta=1):
        '''
        락과 함께 카운터 증가
        '''
        self._value_lock.acquire()
        self._value += delta
        self._value_lock.release()

    def decr(self,delta=1):
        '''
        락과 함께 카운터 감소
        '''
        self._value_lock.acquire()
        self._value -= delta
        self._value_lock.release()


import threading

class SharedCounter:
    '''
    다중 스레드에서 공유 가능한 카운터 객체
    '''
    _lock = threading.RLock()
    def __init__(self, initial_value = 0):
        self._value = initial_value

    def incr(self.delta=1):
        '''
        락과 함께 카운터 증가
        '''
        with SharedCounter._lock:
            self._value += delta

    def decr(self,delta=1):
        '''
        락과 함께 카운터 감소
        '''
        with SharedCounter._lock:
            self.incr(-delta)


from threading import Semaphore
import urllib.request

# 최대 다섯 개의 스레드만 한 번에 실행 가능하다.
_fetch_url_sema = Semaphore(5)

def fetch_url(url):
    with _fetch_url_sema:
        return urllib.request.urlopen(url)
