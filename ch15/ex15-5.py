# 15.5 확장 모듈에서 C API 정의, 내보내기

# setup.py
from distutils.core import setup, Extension

setup(name='ptexample',
      ext_modules=[
        Extension('ptexample',
                  ['ptexample.c'],
                  include_dirs =[], # pysample.h 디렉터리가 필요할 수 있음
                  )
        ]
)


import sample
p1 = sample.Point(2,3)
p1
# <sample.Point object at 0x7f971fb348c0>
import ptexample
ptexample.print_point(p1)
# 2.000000 3.000000



# 토론
