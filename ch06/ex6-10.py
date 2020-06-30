# 6.10 Base64 인코딩, 디코딩

# 바이트 데이터
s = b'hello'
import base64

# Base64로 인코딩
a = base64.b64encode(s)
a
# b'aGVsbG8='

# Base64를 디코딩
base64.b64decode(a)
# b'hello'


# 토론

a = base64.b64encode(s).decode('ascii')
a
# 'aGVsbG8='
