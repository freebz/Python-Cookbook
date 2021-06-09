// 15.19 C에서 파일 같은 객체 읽기

#define CHUNK_SIZE 8192

/* "파일 같은" 객체를 소비하고 바이트를 stdout에 쓴다. */
static PyObject *py_consume_file(PyObject *self, PyObject *args) {
  PyObject *obj;
  PyObject *read_meth;
  PyObject *result = NULL;
  PyObject *read_args;

  if (!PyArg_ParseTuple(args,"0", &obj)) {
    return NULL;
  }

  /* 전달한 객체의 읽기 메소드를 얻는다. */
  if ((read_meth = PyObject_GetAttrString(obj, "read")) == NULL) {
    return NULL;
  }

  /* read()의 인자 리스트를 만든다. */
  read_args = Py_BuildValue("(i)", CHUNK_SIZE);
  while (1) {
    PyObject *data;
    PyObject *enc_data;
    char *buf;
    Py_ssize_t len;

    /* read() 호출 */
    if ((data = PyObject_Call(read_meth, read_args, NULL)) == NULL) {
      goto final;
    }

    /* EOF 확인 */
    if (PySequence_Length(data) == 0) {
      Py_DECREF(data);
      break;
    }

    /* Unicode를 바이트로 인코딩 */
    if ((enc_data=PyUnicode_AsEncodedString(data,"utf-8","strict"))==NULL) {
      Py_DECREF(data);
      goto final;
    }

    /* 내부 버퍼 데이터 추출 */
    PyBytes_AsStringAndSize(enc_data, &buf, &len);

    /* stdout에 쓰기(좀 더 유용한 것으로 바꾼다.) */
    write(1, buf, len);

    /* 정리 */
    Py_DECREF(enc_data);
    Py_DECREF(data);
  }
  result = Py_BuildValue("");

final:
  /* 정리 */
  Py_DECREF(read_meth);
  Py_DECREF(read_args);
  return result;
}



// 토론

...
    /* read() 호출 */
    if ((data = PyObject_Call(read_meth, read_args, NULL)) == NULL) {
      goto final;
    }

    /* EOF 확인 */
    if (PySequence_Length(data) == 0) {
      Py_DECREF(data);
      break;
    }
    if (!PyBytes_Check(data)) {
      Py_DECREF(data);
      PyErr_SetString(PyExc_IOError, "File must be in binary mode");
      goto final;
    }

    /* 내부 버퍼 데이터 추출 */
    PyBytes_AsStringAndSize(data, &buf, &len);
    ...
