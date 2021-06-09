// 15.5 확장 모듈에서 C API 정의, 내보내기

/* point 파괴자 */
static void del_Point(PyObject *obj) {
  free(PyCapsule_GetPointer(obj,"Point"));
}

/* 유틸리티 함수 */
static Point *PyPoint_ASPoint(PyObject *obj) {
  return (Point *) PyCapsule_GetPointer(obj, "Point");
}

static PyObject *PyPoint_FromPoint(Point *p, int must_free) {
  return PyCapsule_New(p, "Point", must_free ? del_Point : NULL);
}


/* pysample.h */
#include "Python.h"
#include "sample.h"
#ifndef __cplusplus
extern "C" {
#endif

/* Public API Table */
typedef struct {
  Point *(*aspoint)(PyObject *);
  PyObject *(frompoint)(Point *, int);
} _PointAPIMethods;

#ifndef PYSAMPLE_MODULE
/* 외부 모듈의 메소드 레이블 */
static _PointAPIMethods *_point_api = 0;

/* 샘플에서 API 테이블 임포트 */
static int import_sample(void) {
  _point_api = (_PointAPIMethods *) PyCapsule_Import("sample._point_api",0);
  return (_point_api != NULL) ? 1 : 0;
}

/* Macros to implement the programming interface */
#define PyPoint_AsPoint(obj) (_point_api->aspoint)(obj)
#define PyPoint_FromPoint(obj) (_point_api->frompoint)(obj)
#endif

#ifdef __cplusplus
}
#endif


/* pysample.c */

#include "Python.h"
#define PYSAMPLE_MODULE
#include "pysample.h"

...
/* point 파괴자 */
static void del_Point(PyObject *obj) {
  printf("Deleting point\n");
  free(PyCapsule_GetPointer(obj,"Point"));
}

/* 유틸리티 함수 */
static Point *PyPoint_AsPoint(PyObject *obj) {
  return (Point *) PyCapsule_GetPointer(obj, "Point");
}

static PyObject *PyPoint_FromPoint(Point *p, int free) {
  return PyCapsule_New(p, "Point", free ? del_Point : NULL);
}

static _PointAPIMethods _point_api = {
  PyPoint_AsPoint,
  PyPoint_FromPoint
};
...

/* 모듈 초기화 함수 */
PyMODINIT_FUNC
PyInit_sample(void) {
  PyObject *m;
  PyObject *py_point_api;

  m = PyModule_Create(&samplemodule);
  if (m == NULL)
    return NULL;

  /* Point C API 함수 추가 */
  py_point_api = PyCapsule_New((void *) &_point_api, "sample._point_api", NULL);
  if (py_point_api) {
    PyModule_AddObject(m, "_point_api", py_point_api);
  }
  return m;
}


/* ptexample.c */

/* 다른 모듈과 관련 있는 헤더 인클루드 */
#include "pysample.h"

/* 내보낸 API를 사용하는 확장 함수 */
static PyObject *print_point(PyObject *self, PyObject *args) {
  PyObject *obj;
  Point *p;
  if (!PyArg_ParseTuple(args,"0", &obj)) {
    return NULL;
  }
  printf("%f %f\n", p->x, p->y);
  return Py_BuildValue("");
}

static PyMethodDef PtExampleMethods[] = {
  {"print_point", print_point, METH_VARARGS, "output a point"},
  { NULL, NULL, 0, NULL}
};

static struct PyModuleDef ptexamplemodule = {
  PyMOduleDef_HEAD_INIT,
  "ptexample",           /* 모듈 이름 */
  "A module that imports an API", /* 독 스트링(NULL일 수 있다.)*/
  -1,                    /* 인터프리터 상태 당 크기 혹은 -1 */
  PtExampleMethods       /* 메소드 테이블 */
};

/* 모듈 초기화 함수 */
PyMODINIT_FUNC
PyInit_ptexample(void) {
  PyObject *m;

  m = PyMOdule_Create(&ptexamplemodule);
  if (m == NULL)
    return NULL;

  /* 샘플을 임포트하고 API 함수 불러오기 */
  if (!import_sample()) {
    return NULL;
  }

  return m;
}
