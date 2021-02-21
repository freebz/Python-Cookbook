# 11.8 원격 프로시저 호출 구현

# rpcserver.py

import pickle
class RPCHandler:
    def __init__(self):
        self._functions = { }

    def register_function(self, func):
        self._functions[func.__name__] = func

    def handle_connection(self, connection):
        try:
            while True:
                # 메시지 받기
                func_name, args, kwargs = pickle.loads(connection.recv())
                # RPC 실행: 응답 전송
                try:
                    r = self._functions[func_name](*args,**kwargs)
                    connection.send(pickle.dumps(r))
                except Exception as e:
                    connection.send(pickle.dumps(e))
        except EOFError:
            pass


from multiprocessing.connection import Listener
from threading import Thread

def rpc_server(handler, address, authkey):
    sock = Listener(address, authkey=authkey)
    while True:
        client = sock.accept()
        t = Thread(target=handler.handle_connection, args=(client,))
        t.daemon = True
        t.start()

# 일급 함수
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

# 핸들러에 등록
handler = RPCHandler()
handler.register_function(add)
handler.register_function(sub)

# 서버 실행
rpc_server(handler, ('localhost', 17000), authkey=b'peekaboo')


import pickle

class RPCProxy:
    def __init__(self, connection):
        self._connection = connection
    def __getattr__(self, name):
        def do_rpc(*args, **kwargs):
            self._connection.send(pickle.dumps((name, args, kwargs)))
            result = pickle.loads(self._connection.recv())
            if isinstance(result, Exception):
                raise result
            return result
        return do_rpc


from multiprocessing.connection import Client
c = Client(('localhost', 17000), authkey=b'peekaboo')
proxy = RPCProxy(c)
proxy.add(2, 3)
# 5
proxy.sub(2, 3)
# -1
proxy.sub([1, 2], 4)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 9, in do_rpc
# TypeError: unsupported operand type(s) for -: 'list' and 'int'



# 토론

# jsonrpcserver.py
import json

class RPCHandler:
    def __init__(self):
        self._functions = { }

    def register_function(self, func):
        self._functions[func.__name__] = func

    def handle_connection(self, connection):
        try:
            while True:
                # 메시지 받기
                func_name, args, kwargs = json.loads(connection.recv())
                # RPC 실행, 응답 전송
                try:
                    r = self._functions[func_name](*args,**kwargs)
                    connection.send(json.dumps(r))
                except Exception as e:
                    connection.send(json.dumps(str(e)))
        except EOFError:
            pass

# jsonrpcclient.py
import json

class RPCProxy:
    def __init__(self, connection):
        self._connection = connection
    def __getattr__(self, name):
        def do_rpc(*args, **kwargs):
            self._connection.send(json.dumps((name, args, kwargs)))
            result = json.loads(self._connection.recv())
            return result
        return do_rpc
