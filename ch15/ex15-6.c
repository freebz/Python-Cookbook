// 15.6 C에서 파이썬 호출

#include <Python.h>

/* 파이썬 인터프리터에서 func(x,y)를 실행한다.
   함수 인자와 반환 값은 반드시 파이썬 float여야 한다. */

double call_func(PyObject *func, double x, double y) {
  PyObject *args;
  PyObject *kwargs;
  PyObject *result = 0;
  double retval;

  /* GIL을 소유하고 있는지 확인하다. */
  PyGILState_STATE state = PyGILState_Ensure();
  /* func가 올바른 호출 객체인지 검증한다. */
  if (!PyCallable_Check(func)) {
    fprintf(stderr,"call_func: expected a callable\n");
    goto fail;
  }
  /* 함수 인자 빌드 */
  args = Py_BuildValue("(dd)", x, y);
  kwargs = NULL;

  /* 함수 호출 */
  result = PyObject_Call(func, args, kwargs);
  Py_DECREF(args);
  py_XDECREF(kwargs);

  /* 파이썬 예외가 있는지 확인 */
  if (PyErr_Occurred()) {
    PyErr_Print();
    goto fail;
  }

  /* 결과 값이 float인지 검증 */
  if (!PyFloat_Check(result)) {
    fprintf(stderr,"call_func: callable didn't return a float\n");
    goto fail;
  }

  /* 반환 값 생성 */
  retval = PyFloat_AsDouble(result);
  Py_DECREF(result);

  /* 기존 GIL 상태를 복구하고 반환 */
  PyGILState_Release(state);
  return retval;

fail:
  Py_XDECREF(result);
  PyGILState_Release(state):
  abort();  // 좀 더 올바른 것으로 바꾼다.
}


#include <Pyhon.h>

/* 앞에 나온 것과 동일한 call_func() 정의 */
...

/* 모듈에서 심볼 불러오기 */
PyObject *import_name(const char *modname, const char *symbol) {
  PyObject *u_name, *module;
  u_name = PyUnicode_FromString(modname);
  module = PyImport_Import(u_name);
  Py_DECREF(u_name);
  return PyObject_GetAttrString(module, symbol);
}

/* 간단한 임베드 예제 */
int main() {
  PyObject *pow_fnc;
  double x;

  Py_Initialize();
  /* math.pow 함수에 대한 참조 얻기 */
  pow_func = import_name("math","pow");

  /* call_func() 코드를 사용해서 호출하기 */
  for (x = 0.0; x < 10.0; x += 0.1) {
    printf("%0.2f %0.2f\n", x, call_func(pow_func,x,2.0));
  }
  /* 완료 */
  Py_DECREF(pow_func);
  Py_Finalize();
  return 0;
}


/* C-Python 콜백을 테스트하기 위한 확장 함수 */
PyObject *py_call_func(PyObject *self, PyObject *args) {
  PyObject *func;
  double x, y, result;
  if (!PyArg_ParseTuple(args,"Odd", &func,&x,&y)) {
    return NULL;
  }
  result = call_func(func, x, y);
  return Py_BuildValue("d", result);
}



// 토론

double call_func(PyObject *func, double x, double y) {
  ...
  /* func가 올바른지 검증 */
  if (!PyCallable_Check(func)) {
    fprintf(stderr,"call_func: expected a callable\n");
    goto fail;
  }
  ...


double call_func(PyObject *func, double x, double y) {
  PyObject *args;
  PyObject *kwargs;

  ...
  /* 인자 빌드 */
  args = Py_BuildValue("(dd)", x, y);
  kwargs = NULL;

  /* 함수 호출 */
  result = PyObject_Call(func, args, kwargs);
  Py_DECREF(args);
  Py_XDECREF(kwargs);
  ...


  ...
  /* 파이썬 예외가 있는지 확인 */
  if (PyErr_Occurred()) {
    PyErr_Print();
    goto fail;
  }
  ...
fail:
  PyGILState_Release(state);
  abort();


double call_func(PyObject *func, double x, double y) {
  ...
  double retval;

  /* GIL을 소유하고 있는지 확인한다. */
  PyGILState_STATE state = PyGILState_Ensure();
  ...
  /* 파이썬 C API 함수를 사용하는 코드 */
  ...
  /* 기존 GIL 상태를 복원하고 반환 */
  PyGILState_Release(state);
  return retval;

fail:
  PyGILSTATE_Release(state);
  abort();
}
