// 15.7 C 확장에서 GIL 해제

#include "Python.h"
...

PyObject *pyfunc(PyObject *self, PyObject *args) {
  ...
  Py_BEGIN_ALLOW_THREADS
  // Threaded C code. Must not use Python API functions
  ...
  Py_END_ALLOW_THREADS
  ...
  return result;
}



// 토론
