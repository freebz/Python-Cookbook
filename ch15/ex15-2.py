# 15.2 간단한 C 확장 모듈 작성

# setup.py
from distutils.core import setup, Extension

setup(name='sample',
      ext_modules=[
        Extension('sample',
                  ['pysample.c'],
                  include_dirs = ['/some/dir'],
                  define_macros = [('FOO','1')],
                  undef_macros = ['BAR'],
                  library_dirs = ['/usr/local/lib'],
                  libraries = ['sample']
                  )
        ]
)


import sample
sample.gcd(35, 42)
# 7
sample.in_mandel(0, 0, 500)
# 1
sample.in_mandel(2.0, 1.0, 500)
# 0
sample.divide(42, 8)
# (5, 2)



# 토론

# static PyObject *py_func(PyObject *self, PyObject *args) {
#   ...
# }


# return Py_BuildValue("1", 34);       // 정수형 반환
# return Py_BuildValue("d", 3.4);      // 더블형 반환
# return Py_BuildValue("s", "Hello");  // Null로 끝나는 UTF-8 문자열
# return Py_BuildValue("(ii)", 3, 4);  // 튜플 (3, 4)
