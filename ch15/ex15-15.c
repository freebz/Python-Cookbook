// 15.15 C 문자열의 파이썬 변환

char *s;      /* C 문자열 데이터에 대한 포인터 */
int   len;    /* 데이터 길이 */

/* 바이트 객체 만들기 */
PyObject *obj = Py_BuildValue("y#", s, len);


PyObject *obj = Py_BuildValue("s#", s, len);


PyObject *obj = PyUnicode_Decode(s, len, "encoding", "errors");

/* 예제 */
obj = PyUnicode_Decode(s, len, "latin-1", "strict");
obj = PyUnicode_Decode(s, len, "ascii", "ignore");


wchar_t *w;    /* 와이드 캐릭터 문자열 */
int len;       /* 길이 */

PyObject *obj = Py_BuildValue("u#", w, len);


PyObject *obj = PyUnicode_FromWideChar(w, len);



// 토론
