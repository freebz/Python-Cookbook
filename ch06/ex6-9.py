# 6.9 16진수 인코딩, 디코딩

# 최초 바이트 문자열
s = b'hello'

# 16진법으로 인코딩
import binascii
h = binascii.b2a_hex(s)
h
# b'68656c6c6f'

# 바이트로 디코딩
binascii.a2b_hex(h)
# b'hello'


import base64
h = base64.b16encode(s)
h
# b'68656C6C6F'
base64.b16decode(h)
# b'hello'


# 토론

h = base64.b16encode(s)
print(h)
# b'68656C6C6F'
print(h.decode('ascii'))
# 68656C6C6F
