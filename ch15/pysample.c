#include "Python.h"
#include "sample.h"

/* int gcd(int, int) */
static PyObject * py_gcd(PyObject *self, PyObject *args) {
  int x, y, result;
  
  if (!PyArg_ParseTuple(args,"ii", &x, &y)) {
    return NULL;
  }

  result = gcd(x,y);
  return Py_BuildValue("i", result);
}

/* int in_mandel(double, double, int) */
static PyObject *py_in_mandel(PyObject *self, PyObject *args) {
  double x0, y0;
  int n;
  int result;

  if (!PyArg_ParseTuple(args, "ddi", &x0, &y0, &n)) {
    return NULL;
  }
  result = in_mandel(x0,y0,n);
  return Py_BuildValue("i", result);
}

/* int divide(int, int, int *) */
static PyObject *py_divide(PyObject *self, PyObject *args) {
  int a, b, quotient, remainder;
  if (!PyArg_ParseTuple(args, "ii", &a, &b)) {
    return NULL;
  }
  quotient = divide(a,b, &remainder);
  return Py_BuildValue("(ii)", quotient, remainder);
}

/* 모듈 메소드 테이블 */
static PyMethodDef SampleMethods[] = {
  {"gcd", py_gcd, METH_VARARGS, "Greatest comon divisor"},
  {"in_mandel", py_in_mandel, METH_VARARGS, "Mandelbrot test"},
  {"divide", py_divide, METH_VARARGS, "Integer division"},
  { NULL, NULL, 0, NULL }
};

/* 모듈 구조체 */
static struct PyModuleDef samplemodule = {
  PyModuleDef_HEAD_INIT,
  "sample",             /* 모듈 이름 */
  "A sample module",    /* 독스트링(doc string), NULL일 수도 있다. */
  -1,                   /* per-interpreter 상태 크기 혹은 -1 */
  SampleMethods         /* 메소드 테이블 */
};

/* 모듈 초기화 함수 */
PyMODINIT_FUNC
PyInit_sample(void) {
  return PyModule_Create(&samplemodule);
}
