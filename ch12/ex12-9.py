# 12.9 GIL 다루기(그리고 더 이상 걱정하지 않기)

# CPU 계산을 많이 수행하는 함수
def some_work(args):
    ...
    return result

# 위 함수를 호출하는 스레드
def some_thread():
    while True:
        ...
        r = some_work(args)
        ...


# 프로세스 풀 (초기화는 다음 코드 참고)
pool = None

# CPU 계산을 많이 수행하는 함수
def some_work(args):
    ...
    return result

# 위 함수를 호출하는 스레드
def some_thread():
    while True:
        ...
        r = pool.apply(some_work, (args))
        ...

# 풀 초기화
if __name__ == '__main__':
    import multiprocessing
    pool = multiprocessing.Pool()


#include "Python.h"
...

PyObject *pyfunc(PyObject *self, PyObject *args) {
   ...
    Py_BEGIN_ALLOW_THREADS
    // Threaded C code
    ...
    Py_END_ALLOW_THREADS
    ...
}



# 토론
