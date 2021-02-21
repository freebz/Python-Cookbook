# 11.1 클라이언트로 HTTP 서비스와 통신

from urllib import request, parse

# 접속할 URL
url = 'http://httpbin.org/get'

# (있다면) 쿼리 파라미터 딕셔너리
parms = {
    'name1' : 'value1',
    'name2' : 'value2'
}

# 쿼리 문자열 인코드
querystring = parse.urlencode(parms)

# GET 요청 후 응답 읽기
u = request.urlopen(url+'?' + querystring)
resp = u.read()


from urllib import request, parse

# 접속할 URL
url = 'http://httpbin.org/post'

# (있다면) 쿼리 파라미터 딕셔너리
parms = {
    'name1' : 'value1',
    'name2' : 'value2'
}

# 쿼리 문자열 인코드
querystring = parse.urlencode(parms)

# POST 요청 후 응답 읽기
u = request.urlopen(url, querystring.encode('ascii'))
resp = u.read()


from urllib import request, parse
...

# 추가적인 헤더
headers = {
    'User-agent' : 'none/ofyourbusiness',
    'Spam' : 'Eggs'
}

req = request.Request(url, querystring.encode('ascii'), headers=headers)

# 요청 후 응답 읽기
u = request.urlopen(req)
resp = u.read()


import requests

# 접속할 URL
url = 'http://httpbin.org/post'

# (있다면) 쿼리 파라미터 딕셔너리
parms = {
    'name1' : 'value1',
    'name2' : 'value2'
}

# 추가적인 헤더
headers = {
    'User-agent' : 'none/ofyourbusiness',
    'Spam' : 'Eggs'
}

resp = requests.post(url, data=parms, headers=headers)

# 요청이 반환한 텍스트 디코드
text = resp.text


import requests

resp = requests.head('http://www.python.org/index.html')

status = resp.status_code
last_modified = resp.headers['last-modified']
content_type = resp.headers['content-type']
content_length = resp.headers['content-length']


import requests

resp = requests.get('http://pypi.python.org/pypi?:action=login',
                    auth('user','password'))


import requests

# 첫 번째 요청
resp1 = requests.get(url)
...

# 첫 번째 요청으로부터 쿠키를 받은 두 번째 요청
resp2 = requests.get(url, cookies=resp1.cookies)


import requests
url = 'http://httpbin.org/post'
files = { 'file': ('data.csv', open('data.csv', 'rb')) }

r = requests.post(url, files=files)



# 토론

from http.client import HTTPConnection
from urllib import parse

c = HTTPConnection('www.python.org', 80)
c.request('HEAD', '/index.html')
resp = c.getresponse()

print('Status', resp.status)
for name, value in resp.getheaders():
    print(name, value)


import urllib.request

auth = urllib.request.HTTPBasicAuthHandler()
auth.add_password('pypi','http://pypi.python.org','username','password')
opener = urllib.request.build_opener(auth)

r = urllib.request.Request('http://pypi.python.org/pypi?:action=login')
u = opener.open(r)
resp = u.read()

# 여기부터 오프너를 사용해서 더 많은 페이지에 접속할 수 있다.
...


import requests
r = requests.get('http://httpbin.org/get?name=Dave&n=37',
    headers = { 'User-agent': 'goaway/1.0' })
resp = r.json()
resp['headers']
# {'Date': 'Fri, 04 Dec 2020 14:56:45 GMT', 'Content-Type': 'application/json', 'Content-Length': '348', 'Connection': 'keep-alive', 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}
resp['args']
# {'name': 'Dave', 'n': '37'}
