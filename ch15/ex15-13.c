// 15.13 C 라이브러리에 NULL로 끝나는 문자열 전달

void print_chars(char *s) {
  while (*s) {
    printf("%2x ", (unsigned char) *s);
    s++;
  }
  printf("\n");
}


print_chars("Hello");    // 출력: 48 65 6c 6c 6f


static PyObject *py_print_chars(PyObject *self, PyObject *args) {
  char *s;

  if (!PyArg_ParseTuple(args, "y", &s)) {
    return NULL;
  }
  print_chars(s);
  Py_RETURN_NONE;
}


static PyObject *py_print_chars(PyObject *self, PyObject *args) {
  char *s;

  if (!PyArg_ParseTuple(args, "s", &s)) {
    return NULL;
  }
  print_chars(s);
  Py_RETURN_NONE;
}


/* 파이썬 객체 */
PyObject *obj;

/* 바이트에서 변환 */
{
  char *s;
  s = PyBytes_AsString(o);
  if (!s) {
    return NULL;    /* TypeError가 이미 발생했다. */
  }
  print_chars(s);
}

/* 문자열에서 UTF-8 바이트로 변환 */
{
  PyObject *bytes;
  char *s;
  if (!PyUnicode_Check(obj)) {
    PyErr_SetString(PyExc_TypeError, "Expected string");
    return NULL;
  }
  bytes = PyUnicode_AsUTF8String(obj);
  s = PyBytes_AsString(bytes);
  print_chars(s);
  Py_DECREF(bytes);
}



// 토론

static PyObject *py_print_chars(PyObject *self, PyObject *args) {
  PyObject *o, *bytes;
  char *s;

  if (!PyArg_ParseTuple(args, "U", &o)) {
    return NULL;
  }
  bytes = PyUnicode_AsUTF8String(o);
  s = PyBytes_AsString(bytes);
  print_chars(s);
  Py_DECREF(bytes);
  Py_RETURN_NONE;
}
