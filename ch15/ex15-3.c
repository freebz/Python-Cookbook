// 15.3 배열에동작하는 확장 함수 작성

/* double avg(double *, int) 호출 */
static PyObject *py_avg(PyObject *self, PyObject *args) {
  PyObject *bufobj;
  Py_buffer view;
  double result;
  /* 전달 받은 파이썬 객체 얻기 */
  if (!PyArg_ParseTuple(args, "0", &bufobj)) {
    return NULL;
  }

  /* 여기서 버퍼 정보를 얻는다. */
  if (PyObject_GetBuffer(bufobj, &view,
      PyBUF_ANY_CONTIGUOUS | PYy_BUF_FORMAT) == -1) {
    return NULL;
  }

  if (view.ndim != 1) {
    PyErr_SetString(PyExc_TypeError, "Expected a 1-dimensional array");
    PyBuffer_Release(&view);
    return NULL;
  }

  /* 배열 속 아이템 확인 */
  if (strcmp(view.format,"d") != 0) {
    PyErr_SetString(PyExc_TypeError, "Expected an array of doubles");
    PyBuffer_Release(&view);
    return NULL;
  }

  /* 로우 버퍼와 크기를 C 함수에 전달 */
  result = avg(view.buf, view.shape[0]);

  /* 버퍼와 작업을 마쳤음을 알린다. */
  PyBuffer_Release(&view);
  return Py_BuildValue("d", result);
}
