# 15.3 배열에동작하는 확장 함수 작성

import array
avg(array.array('d',[1,2,3]))
# 2.0
import numpy
avg(numpy.array([1.0,2.0,3.0]))
# 2.0
avg([1,2,3])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'list' does not support the buffer interface
avg(b'Hello')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'list' does not support the buffer interface
a = numpy.array([[1.,2.,3.],[4.,5.,6.]])
avg(a[:,2])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: ndarray is not contiguous
sample.avg(a)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: Expected a 1-dimensional array
sample.avg(a[0])
# 2.0



# 토론

# typedef struct bufferinfo {
#     void *buf;                 /* 버퍼 메모리 포인터 */
#     PyObject *obj;             /* 소유자 파이썬 객체 */
#     Py_ssize_t len;            /* 전체 크기(byte) */
#     Py_ssize_t itemsize;       /* 아이템 하나의 크기(byte) */
#     int readonly;              /* 읽기 전용 플래그 */
#     int ndim;                  /* 차원 수 */
#     char *format;              /* 아이템 하나의 구조체 코드 */
#     Py_ssize_t *shape;         /* 차원 배열 */
#     Py_ssize_t *strides;       /* strides 배열 */
#     Py_ssize_t *suboffsets;    /* suboffsets 배열 */
# } Py_buffer;
