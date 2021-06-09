// 15.8 C와 파이썬에서 스레드 믹싱

#include <Python.h>

  ...
  if (!PyEval_ThreadsInitialized()) {
    PyEval_InitThreads();
  }
  ...

  ...
  /* GIL을 소유하고 있는지 확인 */
  PyGILState_STATE state = PyGILSTATE_Ensure();

  /* 인터프리터의 함수 사용 */
  ...
  /* 기존 GIL 상태를 복원하고 반환 */
  PyGILState_Release(state);
  ...



// 토론
