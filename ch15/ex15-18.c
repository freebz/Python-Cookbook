// 15.18 C 확장에 파일 전달

PyObject *fobj;    /* 파일 객체(이미 취득했다.) */
int fd = PyObject_AsFileDescriptor(fobj);
if (fd < 0) {
  return NULL;
}


int fd;    /* 기존 파일 디스크립터(이미 열려 있다.) */
PyObject *fobj = PyFile_FromFd(fd, "filename","r",-1,NULL,NULL,NULL,1);



// 토론
