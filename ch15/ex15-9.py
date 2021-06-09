# 15.9 Swig로 C 코드 감싸기

# % swig -python -py3 sample.i


# setup.py
from distutils.core import setup, Extension

setup(name='sample',
      py_moudles=['sample.py'],
      ext_modules=[
        Extionsion('_sample',
                   ['sample_wrap.c'],
                   include_dirs = [],
                   define_macros = [],
                   undef_macros = [],
                   library_dirs = [],
                   libraries = ['sample']
                   )
        ]
)


import sample
sample.gcd(42,8)
# 2
sample.divide(42,8)
# [5, 2]
p1 = sample.Point(2,3)
p2 = sample.Point(4,5)
sample.distance(p1,p2)
# 2.8284271247461903
p1.x
# 2.0
p1.y
# 3.0
import array
a = array.array('d',[1,2,3])
sample.avg(a)
# 2.0



# 토론

%module sample
%{
#include "sample.h"
%}
...
extern int gcd(int, int);
extern int in_mandel(double x0, double y0, int n);
extern int divide(int a, int b, int *remainder);
extern double avg(double *a, int n);

typedef struct Point {
    double x,y;
} Point;

extern double distance(Point *p1, Point *p2);


p1 = sample.Point(2,3)


# Usage if %extend Point is omitted
p1 = sample.Point()
p1.x = 2.0
p1.y = 3


sample.divide(42,8)
# [5, 2]
