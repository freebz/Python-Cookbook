# 5.21 파이썬 객체를 직렬화하기

import pickle

data = ...   # 파이썬 객체
f = open('somefile', 'wb')
pickle.dump(data, f)


s = pickle.dumps(data)


# 파일에서 불러들이기
f = open('somefile', 'rb')
data = pickle.load(f)

# 문자열에서 불러들이기
data = pickle.loads(s)


# 토론

import pickle
f = open('somedata', 'wb')
pickle.dump([1, 2, 3, 4], f)
pickle.dump('hello', f)
pickle.dump({'Apple', 'Pear', 'Banana'}, f)
f.close()
f = open('somedata', 'rb')
pickle.load(f)
# [1, 2, 3, 4]
pickle.load(f)
# 'hello'
pickle.load(f)
# {'Apple', 'Banana', 'Pear'}


import math
import pickle
pickle.dumps(math.cos)
# b'\x80\x03cmath\ncos\nq\x00.'


# countdown.py
import time
import threading

class Countdown:
    def __init__(self, n):
        self.n = n
        self.thr = threading.Thread(target=self.run)
        self.thr.daemon = True
        self.thr.start()

    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)

    def __getstate__(self):
        return self.n

    def __setstate__(self, n):
        self.__init__(n)


import countdown
c = countdown.Countdown(30)
# T-minus 30
# T-minus 29
# T-minus 28
# ...

# 잠시 후에
f = open('cstate.p', 'wb')
import pickle
pickle.dump(c, f)
f.close()


f = open('cstate.p', 'rb')
pickle.load(f)
# <countdown.Countdown object at 0x7fb04edf40f0>
# T-minus 19
# T-minus 18
# ...
