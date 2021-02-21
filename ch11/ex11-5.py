# 11.5 간단한 REST 기반 인터페이스 생성

# resty.py

import cgi

def notfound_404(environ, start_response):
    start_response('404 Not Found', [ ('Content-type', 'text/plain') ])
    return [b'Not Found']

class PathDispatcher:
    def __init__(self):
        self.pathmap = { }

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        params = cgi.FieldStorage(environ['wsgi.input'],
                                  environ=environ)
        method = environ['REQUEST_METHOD'].lower()
        environ['params'] = { key: params.getvalue(key) for key in params }
        handler = self.pathmap.get((method,path), notfound_404)
        return handler(environ, start_response)

    def register(self, method, path, function):
        self.pathmap[method.lower(), path] = function
        return function


import time

_hello_resp = '''\
<html>
  <head>
    <title>Hello {name}</title>
  </head>
  <body>
    <h1>Hello {name}!</h1>
  </body>
</html>'''

def hello_world(environ, start_response):
    start_response('200 OK', [ ('Content-type','text/html')])
    params = environ['params']
    resp = _hello_resp.format(name=params.get('name'))
    yield resp.encode('utf-8')

_localtime_resp = '''\
<?xml version="1.0"?>
<time>
  <year>{t.tm_year}</year>
  <month>{t.tm_mon}</month>
  <day>{t.tm_mday}</day>
  <hour>{t.tm_hour}</hour>
  <minute>{t.tm_min}</minute>
  <second>{t.tm_sec}</second>
</time>'''

def localtime(environ, start_response):
    start_response('200 OK', [ ('Content-type', 'application/xml') ])
    resp = _localtime_resp.format(t=time.localtime())
    yield resp.encode('utf-8')

if __name__ == '__main__':
    from resty import PathDispatcher
    from wsgiref.simple_server import make_server

    # 디스패처를 생성하고 함수 등록
    dispatcher = PathDispatcher()
    dispatcher.register('GET', '/hello', hello_world)
    dispatcher.register('GET', '/localtime', localtime)

    # 기본 서버 실행
    httpd = make_server('', 8080, dispatcher)
    print('Serving on port 8080...')
    httpd.serve_forever()


u = urlopen('http://localhost:8080/hello?name=Guido')
print(u.read().decode('utf-8'))
# <html>
#   <head>
#     <title>Hello Guido</title>
#   </head>
#   <body>
#     <h1>Hello Guido!</h1>
#   </body>
# </html>
u = urlopen('http://localhost:8080/localtime')
print(u.read().decode('utf-8'))
# <?xml version="1.0"?>
# <time>
#   <year>2012</year>
#   <month>11</month>
#   <day>24</day>
#   <hour>14</hour>
#   <minute>49</minute>
#   <second>17</second>
# </time>



# 토론

import cgi

def wsgi_app(environ, start_response):
    ...

    
def wsgi_app(environ, start_response):
    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']
    # 쿼리 파라미터 파싱
    params = cgi.FieldStorage(environ['wsgi.input'], environ=environ)
    ...


def wsgi_app(environ, start_response):
    ...
    start_response('200 OK', [('Content-type', 'text/plain')])


def wsgi_app(environ, start_response):
    ...
    start_response('200 OK', [('Content-type', 'text/plain')])
    resp = []
    resp.append(b'Hello World\n')
    resp.append(b'Goodbye!\n')
    return resp


def wsgi_app(environ, start_response):
    ...
    start_response('200 OK', [('Content-type', 'text/plain')])
    yield b'Hello World\n'
    yield b'Goodbye!\n'


class WSGIApplication:
    def __init__(self):
        ...
    def __call__(self, environ, start_response):
        ...


if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    # 디스패처를 생성하고 함수 등록
    dispatcher = PathDispatcher()
    ...

    # 기본 서버 실행
    httpd = make_server('', 8080, dispatcher)
    print('Serving on port 8080...')
    httpd.serve_forever()
