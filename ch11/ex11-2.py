# 11.2 TCP 서버 만들기

from socketserver import BaseRequestHandler, TCPServer

class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        while True:
            msg = self.request.recv(8192)
            if not msg:
                break
            self.request.send(msg)

if __name__ == '__main__':
    serv = TCPServer(('', 20000), EchoHandler)
    serv.serve_forever()


from socket import socket, AF_INET, SOCK_STREAM
s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 20000))
s.send(b'Hello')
# 5
s.recv(8192)
# b'Hello'


from socketserver import StreamRequestHandler, TCPServer

class EchoHandler(StreamRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        # 읽기 위한 파일 같은 객체 self.rfile
        for line in self.rfile:
            # 쓰기 위한 파일 같은 객체 self.wfile
            self.wfile.write(line)

if __name__ == '__main__':
    serv = TCPServer(('', 20000), EchoHandler)
    serv.serve_forever()



# 토론

from socketserver import ThreadingTCPServer
...

if __name__ == '__main__':
    serv = ThreadingTCPServer(('', 20000), EchoHandler)
    serv.serve_forever()


...
if __name__ == '__main__':
    from threading import Thread
    NWORKERS = 16
    serv = TCPServer(('', 20000), EchoHandler)
    for n range(NWORKERS):
        t = Thread(target=serv.serve_forever)
        t.daemon = True
        t.start()
    serv.serve_forever()


if __name__ == '__main__':
    serv = TCPServer(('', 20000), EchoHandler, bind_and_activate=False)
    # 소켓 옵션 설정
    serv.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 바인드, 활성화
    serv.server_bind()
    serv.server_activate()
    serv.serve_forever()


...
if __main__ == '__main__':
    TCPServer.allow_resue_address = True
    serv = TCPServer(('', 20000), EchoHandler)
    serv.serve_forever()


import socket

class EchoHandler(StreamRequestHandler):
    # 옵션 설정 (기본 값)
    timeout = 5                       # 모든 소켓 동작 타임아웃
    rbufsize = -1                     # 읽기 버퍼 크기
    wbufsize = 0                      # 쓰기 버퍼 크기
    disable_nagle_algorithm = False   # Sets TCP_NODELAY socket option
    def handle(self):
        print('Got connection from', self.client_address)
        try:
            for line in self.rfile:
                # 쓰기 위한 파일 같은 객체 self.wfile
                self.wfile.write(line)
        except socket.timeout:
            print('Timed out!')


from socket import socket, AF_INET, SOCK_STREAM

def echo_handler(address, client_sock):
    print('Got connection from {}'.format(address))
    while True:
        msg = client_sock.recv(8192)
        if not msg:
            break
        client_sock.sendall(msg)
    client_sock.close()

def echo_server(address, backlog=5):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(backlog)
    while True:
        client_sock, client_addr = sock.accept()
        echo_handler(client_addr, client_sock)

if __name__ == '__main__':
    echo_server(('', 20000))
