// 15.20 C에서 순환 객체 소비

static PyObject *py_consume_iterable(PyObject *self, PyObject *args) {
  PyObject *obj;
  PyObject *iter;
  PyObject *item;

  if (!PyArg_ParseTuple(args, "0", &obj)) {
    return NULL;
  }
  if ((iter = PyObject_GetIter(obj)) == NULL) {
    return NULL;
  }
  while ((item = PyIter_Next(iter)) != NULL) {
    /* 아이템 사용 */
    ...
    Py_DECREF(item);
  }
  Py_DECREF(iter);
  return Py_BuildValue("");
}



// 토론
