# 15.11 Cython으로 성능 좋은 배열 연산 구현

# sample.pyx (Cython)

cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef clip(double[:] a, double min, double max, double[:] out):
    '''
    min과 max 범위의 값만 남기고 out에 기록한다.
    '''
    if min > max:
        raise ValueError("min must be <= max")
    if a.shape[0] != out.shape[0]:
        raise ValueError("input and output arrays mustbe the same size")
    for i in range(a.shape[0]):
        if a[i] < min:
            out[i] = min
        elif a[i] > max:
            out[i] = max
        else:
            out[i] = a[i]


# setup.py

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension('sample',
              ['sample.pyx'])
]

setup(
    name = 'Sample app',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)


# array 모듈 예제
import sample
import array
a = array.array('d',[1,-3,4,7,2,0])
a
# array('d', [1.0, -3.0, 4.0, 7.0, 2.0, 0.0])
sample.clip(a,1,4,a)
a
# array('d', [1.0, 1.0, 4.0, 4.0, 2.0, 1.0])

# numpy 예제
import numpy
b = numpy.random.uniform(-10,10,size=1000000)
b
# array([-6.43056168,  2.62088531,  3.44525464, ...,  2.48194312,
#         5.36732304,  1.25373588])
c = numpy.zeros_like(b)
c
# array([0., 0., 0., ..., 0., 0., 0.])
sample.clip(b,-5,5,c)
c
# array([-5.        ,  5.        ,  0.69248932, ...,  0.69583148,
#        -3.86290931,  2.37266888])
min(c)
# -5.0
max(c)
# 5.0


timeit('numpy.clip(b,-5,5,c)','from __main__ import b,c,numpy',number=1000)
# 8.093049556000551
timeit('sample.clip(b,-5,5,c)','from __main__ import b,c,sample',
       number=1000)
# 3.760528204000366



# 토론

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef clip(double[:] a, double min, double max, double[:] out):
    if min > max:
        raise ValueError("min must be <= max")
    if a.shape[0] != out.shape[0]:
        raise ValueError("input and output arrays must be the same size")
    for i in range(a.shape[0]):
        out[i] = (a[i] if a[i] < max else max) if a[i] > min else min


void clip(double *a, int n, double min, double max, double *out) {
    double x;
    for (; n >= 0; n--, a++, out++) {
        x = *a;
        *out = x > max ? max : (x < min ? min : x);
    }
}


@cython.boundscheck(False)
@cython.wraparound(False)
cpdef clip(double[:] a, double min, double max, double[:] out):
    if min > max:
        raise ValueError("min must be <= max")
    if a.shape[0] != out.shape[0]:
        raise ValueError("input and output arrays must be the same size")
    with nogil:
        for i in range(a.shape[0]):
            out[i] = (a[i] if a[i] < max else max) if a[i] > min else min


@cython.boundscheck(False)
@cython.wraparound(False)
cpdef clip2d(double[:,:] a, double min, double max, double[:,:] out):
    if min > max:
        raise ValueError("min must be <= max")
    for n in range(a.ndim):
        if a.shape[n] != out.shape[n]:
            raise TypeError("a and out have different shapes")
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            if a[i,j] < min:
                out[i,j] = min
            elif a[i,j] > max:
                out[i,j] = max
            else:
                out[i,j] = a[i,j]
