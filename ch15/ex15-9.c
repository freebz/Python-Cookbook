// 15.9 Swig로 C 코드 감싸기

/* sample.h */

#include <math.h>
extern int gcd(int, int);
extern int in_mandel(double x0, double y0, int n);
extern int divide(int a, int b, int *remainder);
extern double avg(double *a, int n);

typedef struct Point {
  double x, y;
} Point;

extern double distance(Point *p1, Point *p2);


// sample.i - Swig interface
%module sample
%{
#include "sample.h"
%}

/* 커스터마이즈 */
%extent Point {
  /* Point 객체 생성자 */
  Point(double x, double y) {
    Point *p = (Point *) malloc(sizeof(Point));
    p->x = x;
    p->y = y;
    return p;
  };
};

/* *remainder를 출력 인자로 매핑 */
%include typemaps.i
%apply int *OUTPUT { int * remainder };

/* 인자 패턴(double *a, int n)을 배열에 매핑 */
%typemap(in) (double *a, int n)(Py_buffer view) {
  view.obj = NULL;
  if (PyObject_GetBuffer($input, &view, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {
    SWIG_fail;
  }
  if (strcmp(view.format,"d") != 0) {
    PyErr_SetString(PyExc_TypeError, "Expected an array of doubles");
    SWIG_fail;
  }
  $1 = (double *) view.buf;
  $2 = view.len / sizeof(double);
}

/* 확장 모듈에 포함할 C 선언 */

extern int gcd(int, int);
extern int in_mandel(double x0, double y0, int n);
extern int divide(int a, int b, int *remainder);
extern double avg(double *a, int n);

typedef struct Point {
  double x,y;
} Point;

extern double distance(Point *p1, Point *p2);
