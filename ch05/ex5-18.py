# 5.18 기존 파일 디스크립터를 파일 객체로 감싸기

# 하위 레벨 파일 디스크립터 열기
import os
fd = os.open('somefile.txt', os.O_WRONLY | os.O_CREAT)

# 올바른 파일로 바꾸기
f = open(fd, 'wt')
f.write('hello world\n')
f.close()


# 파일 객체를 생성하지만, 사용이 끝났을 때 fd를 닫지 않는다.
f = open(fd, 'wt', closefd=False)
...


# 토론

from socket import socket, AF_INET, SOCK_STREAM

def echo_client(client_sock, addr):
    print('Got connection from', addr)

    # 읽기/쓰기를 위해 소켓에 대한 텍스트 모드 파일 래퍼(wrapper)를 만든다.
    client_in = open(client_sock.fileno(), 'rt', encoding='latin-1',
                     closefd=False)
    client_out = open(client_sock.fineno(), 'wt', encoding='latin-1',
                      closefd=False)

    # 파일 I/O를 사용해 클라이언트에 라인을 에코한다.
    for line in client_in:
        client_out.write(line)
        client_out.flush()
    client_sock.close()

def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        echo_client(client, addr)


import sys
# stdout에 대한 바이너리 모드 파일 만들기
bstdout = open(sys.stdout.fileno(), 'wb', closefd=False)
bstdout.write(b'Hello World\n')
bstdout.flush()
