# 15.1 ctypes로 C 코드 접근

# sample.py
import ctypes
import os

# 동일한 디렉터리에서 이 파일과 동일한 .so 파일을 찾는다.
_file = 'libsample.so'
_path = os.path.join(*(os.path.split(__file__)[:-1] + (_file,)))
_mod = ctypes.cdll.LoadLibrary(_path)

# int gcd(int, int)
gcd = _mod.gcd
gcd.argtypes = (ctypes.c_int, ctypes.c_int)
gcd.restype = ctypes.c_int

# int in_mandel(double, double, int)
in_mandel = _mod.in_mandel
in_mandel.argtypes = (ctypes.c_double, ctypes.c_double, ctypes.c_int)
in_mandel.restype = ctypes.c_int

# int divide(int, int, int *)
_divide = _mod.divide
_divide.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int))
_divide.restype = ctypes.c_int

def divide(x, y):
    rem = ctypes.c_int()
    quot = _divide(x, y, rem)
    return quot,rem.value

# void avg(double *, int n)
# 특별 타입 'double *' 속성을 정의한다.
class DoubleArrayType:
    def from_param(self, param):
        typename = type(param).__name__
        if hasattr(self, 'from_' + typename):
            return getattr(self, 'from_' + typename)(param)
        elif isinstance(param, ctypes.Array):
            return param
        else:
            raise TypeError("Can't convert %s" % typename)

    # array.array 객체로부터 캐스팅
    def from_array(self, param):
        if param.typecode != 'd':
            raise TypeError('must be an array of doubles')
        ptr, _ = param.buffer_info()
        return ctypes.cast(ptr, ctypes.POINTER(ctypes.c_double))

    # 리스트/튜플로부터 캐스팅
    def from_list(self, param):
        val = ((ctypes.c_double)*len(param))(*param)
        return val

    from_tuple = from_list

    # numpy 배열로부터 캐스팅
    def from_ndarray(self, param):
        return param.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

DoubleArray = DoubleArrayType()
_avg = _mod.avg
_avg.argtypes = (DoubleArray, ctypes.c_int)
_avg.restype = ctypes.c_double

def avg(values):
    return _avg(values, len(values))

# Point 구조체 { }
class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_double),
                ('y', ctypes.c_double)]

# double distance(Point *, Point *)
distance = _mod.distance
distance.argtypes = (ctypes.POINTER(Point), ctypes.POINTER(Point))
distance.restype = ctypes.c_double


import sample
sample.gcd(35,42)
# 7
sample.in_mandel(0,0,500)
# 1
sample.in_mandel(2.0,1.0,500)
# 0
sample.divide(42,8)
# (5, 2)
sample.avg([1,2,3])
# 2.0
p1 = sample.Point(1,2)
p2 = sample.Point(4,5)
sample.distance(p1,p2)
# 4.242640687119285



# 토론

from ctypes.util import find_library
find_library('m')
# '/usr/lib/libm.dylib'
find_library('pthread')
# '/usr/lib/libpthread.dylib'
find_library('sample')
# '/usr/local/lib/libsample.so'


_mod = ctypes.cdll.LoadLibrary(_path)


# int in_mandel(double, double, int)
in_mandel = _mod.in_mandel
in_mandel.argtypes = (ctypes.c_double, ctypes.c_double, ctypes.c_int)
in_mandel.restype = ctypes.c_int


divide = _mod.divide
divide.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int))
x = 0
divide(10, 3, x)
# Tranceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ctypes.ArgumentError: argument 3: <class 'TypeError'>: expected LP_c_int
# instance instead of int


x = ctypes.c_int()
divide(10, 3, x)
# 3
x.value
# 1


# int divide(int, int, int *)
_divide = _mod.divide
_divide.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int))
_divide.restype = ctypes.c_int

def divide(x, y):
    rem = ctypes.c_int()
    quot = _divide(x,y,rem)
    return quot, rem.value


nums = [1, 2, 3]
a = (ctypes.c_double * len(nums))(*nums)
a
# <__main__.c_double_Array_3 object at 0x7f971fb349c0>
a[0]
# 1.0
a[1]
# 2.0
a[2]
# 3.0


import array
a = array.array('d',[1,2,3])
a
# array('d', [1.0, 2.0, 3.0])
ptr = a.buffer_info()
ptr
# (140287049341680, 3)
ctypes.cast(ptr[0], ctypes.POINTER(ctypes.c_double))
# <__main__.LP_c_double object at 0x7f971fb34540>


import sample
sample.avg([1,2,3])
# 2.0
sample.avg((1,2,3))
# 2.0
import array
sample.avg(array.array('d',[1,2,3]))
# 2.0
import numpy
sample.avg(numpy.array([1.0,2.0,3.0]))
# 2.0


class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_double),
                ('y', ctypes.c_double)]


p1 = sample.Point(1,2)
p2 = sample.Point(4,5)
p1.x
# 1.0
p1.y
# 2.0
sample.distance(p1,p2)
# 4.242640687119285
