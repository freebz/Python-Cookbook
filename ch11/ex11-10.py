# 11.10 네트워크 서비스에 SSL 추가

from socket import socket, AF_INET, SOCK_STREAM
import ssl

KEYFILE = 'server_key.pem'   # 서버의 비밀키
CERTFILE = 'server_cert.pem' # 서버 인증서 (클라이언트에게 보낸다.)

def echo_client(s):
    while True:
        data = s.recv(8192)
        if data == b'':
            break
        s.send(data)
    s.close()
    print('Connection closed')

def echo_server(address):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(1)

    # 클라이언트 인증을 요구하는 SSL 레이어로 감싼다.
    s_ssl = ssl.wrap_socket(s,
                            keyfile=KEYFILE,
                            certfile=CERTFILE,
                            server_side=True
                            )
    # 연결 기다림
    while True:
        try:
            c,a = s_ssl.accept()
            print('Got connection', c, a)
            echo_client(c)
        except Exception as e:
            print('{}: {}'.format(e.__class__.__name__, e))

echo_server(('', 20000))


from socket import socket, AF_INET, SOCK_STREAM
import ssl
s = socket(AF_INET, SOCK_STREAM)
s_ssl = ssl.wrap_socket(s,
                        cert_reqs=ssl.CERT_REQUIRED,
                        ca_certs = 'server_cert.pem')
s_ssl.connect(('localhost', 20000))
s_ssl.send(b'Hello World?')
# 12
s_ssl.recv(8192)
# b'Hello World?'


import ssl

class SSLMixin:
    '''
    socketserver 모듈에 기반한 기존 서버에 SSL을 추가하는 믹스인 클래스
    '''
    def __init__(self, *args,
                 keyfile=None, certfile=None, ca_certs=None,
                 cert_reqs=ssl.CERT_NONE,
                 **kwargs):
        self._keyfile = keyfile
        self._certfile = certfile
        self._ca_certs = ca_certs
        self._cert_reqs = cert_reqs
        super().__init__(*args, **kwargs)

    def get_request(self):
        client, addr = super().get_request()
        client_ssl = ssl.wrap_socket(client,
                                     keyfile = self._keyfile,
                                     certfile = self._certfile,
                                     ca_certs = self._ca_certs,
                                     cert_reqs = self._cert_reqs,
                                     server_side = True)
        return client_ssl, addr


# XML-RPC server with SSL

from xmlrpc.server import SimpleXMLRPCServer

class SSLSimpleXMLRPCServer(SSLMixin, SimpleXMLRPCServer):
    pass


import ssl
from xmlrpc.server import SimpleXMLRPCServer
from sslmixin import SSLMixin

class SSLSimpleXMLRPCServer(SSLMixin, SimpleXMLRPCServer):
    pass

class KeyValueServer:
    _rpc_methods_ = ['get', 'set', 'delete', 'exists', 'keys']
    def __init__(self, *args, **kwargs):
        self._data = {}
        self._serv = SSLSimpleXMLRPCServer(*args, allow_none=True, **kwargs)
        for name in self._rpc_methods_:
            self._serv.register_function(getattr(self, name))

    def get(self, name):
        return self._data[name]

    def set(self, name, value):
        self._data[name] = value

    def delete(self, name):
        return name in self._data

    def exists(self, name):
        return name in self._data

    def keys(self):
        return list(self._data)

    def serve_forever(self):
        self._serv.serve_forever()

if __name__ == '__main__':
    KEYFILE='server_key.pem'     # 서버의 비밀 키
    CERTFILE='server_cert.pem'   # 서버의 인증서
    kvserv = KeyValueServer(('', 15000),
                            keyfile=KEYFILE,
                            certfile=CERTFILE),
    kvserv.serve_forever()


from xmlrpc.client import ServerProxy
s = ServerProxy('https://localhost:15000', allow_none=True)
s.set('foo','bar')
s.set('spam', [1, 2, 3])
s.keys()
# ['spam', 'foo']
s.get('foo')
# 'bar'
s.get('spam')
# [1, 2, 3]
s.delete('spam')
s.exists('spam')
# False


from xmlrpc.client import SafeTransport, ServerProxy
import ssl

class VerifyCertSafeTransport(SafeTransport):
    def __init__(self, cafile, certfile=None, keyfile=None):
        SafeTransport.__init__(self)
        self._ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        self._ssl_context.load_verify_locations(cafile)
        if cert:
            self._ssl_context.load_cert_shain(certfile, keyfile)
        self._ssl_context.verify_mode = ssl.CERT_REQUIRED

    def make_connection(self, host):
        # 전달된 딕셔너리의 아이템은 http.client.HTTPSConnection() 생성자에
        # 키워드로서 매개변수로 전달된다.
        # context 인자는 ssl.SSLContext 인스턴스가 SSL 환경 설정 정보를 담아서
        # 전달되도록 한다.
        s = super().make_connection((host, {'context': self._ssl_context}))

        return s

# 클라이언트 프록시 생성
s = ServerProxy('https://localhost:15000',
                transport=VerifyCertSafeTransport('server_cert.pem'),
                allow_none=Ture)


if __name__ == '__main__':
    KEYFILE='server_key.pem'   # 서버의 비밀 키
    CERTFILE='server_cert.pem' # 서버 인증서
    CA_CERTS='client_cert.pem' # 허용한 클라이언트 인증서

    kvserv = KeyValueServer(('', 15000),
                            keyfile=KEYFILE,
                            certfile=CERTFILE,
                            ca_certs=CA_CERTS,
                            cert_reqs=ssl.CERT_REQUIRED,
                            )
    kvserv.serve_forever()


# 클라이언트 프록시 생성
s = ServerProxy('https://localhost:15000',
                transport=VerifyCertSafeTransport('server_cert.pem',
                                                  'client_cert.pem',
                                                  'client_key.pem'),
                allow_none=Ture)



# 토론

bash % openssl req -new -x509 -days 365 -nodes -out server_cert.pem \
    -keyout server_key.pem
Generating a 1024 bit RSA private key
.......+++++
..................................................................................................................+++++
writing new private key to 'server_key.pem'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:US
State or Province Name (full name) [Some-State]:Illinois
Locality Name (eg, city) []:Chicago
Organization Name (eg, company) [Internet Widgits Pty Ltd]:Dabeaz, LLC
Organizational Unit Name (eg, section) []:
Common Name (e.g. server FQDN or YOUR name) []:localhost
Email Address []:
bash %
