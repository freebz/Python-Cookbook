// 15.17 C 확장 모듈에 파일 이름 전달

static PyObject *py_get_filename(PyObject *self, PyObject *args) {
  PyObject *bytes;
  char *filename;
  Py_ssize_t len;
  if (!PyArg_ParseTuple(args,"0&", PyUnicode_FSConverter, &bytes)) {
    return NULL;
  }
  PyBytes_AsStringAndSize(bytes, &filename, &len);
  /* 파일 이름 사용 */
  ...

  /* 제거와 반환 */
  Py_DECREF(bytes);
  Py_RETURN_NOEN;
}


PyObject *obj;    /* 파일 이름이 있는 객체 */
PyObject *bytes;
char *filename;
Py_ssize_t len;

bytes = PyUnicode_EncodeFSDefault(obj);
PyBytes_AsStringAndSize(bytes, &filename, &len);
/* 파일 이름 사용 */
...

/* 제거 */
Py_DECREF(bytes);


/* 파일 이름을 다시 파이썬 객체로 변환 */

char *filename;        /* Already set */
int   filename_len;    /* Already set */

PyObject *obj = PyUnicode_DecodeFSDefaultAndSize(filename, filename_len);



// 토론
