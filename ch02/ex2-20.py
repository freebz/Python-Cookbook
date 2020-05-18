# 2.20 바이트 문자열에 텍스트 연산 수행

data = b'Hello World'
data[0:5]
# b'Hello'
data.startswith(b'Hello')
# True
data.split()
# [b'Hello', b'World']
data.replace(b'Hello', b'Hello Cruel')
# b'Hello Cruel World'


data = bytearray(b'Hello World')
data[0:5]
# bytearray(b'Hello')
data.startswith(b'Hello')
# True
data.split()
# [bytearray(b'Hello'), bytearray(b'World')]
data.replace(b'Hello', b'Hello Cruel')
# bytearray(b'Hello Cruel World')


data = b'FOO:BAR,SPAM'
import re
re.split('[:,]',data)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/usr/lib/python3.6/re.py", line 212, in split
#     return _compile(pattern, flags).split(string, maxsplit)
# TypeError: cannot use a string pattern on a bytes-like object

re.split(b'[:,]',data)          # 주의: 패턴도 바이트로 나타냄
# [b'FOO', b'BAR', b'SPAM']


# 토론

a = 'Hello World'               # 텍스트 문자열
a[0]
# 'H'
a[1]
# 'e'
b = b'Hello World'              # 바이트 문자열
b[0]
# 72
b[1]
# 101


s = b'Hello World'
print(s)
# b'Hello World'                # b'...' 형식으로 출력된다.
print(s.decode('ascii'))
# Hello World


b'%10s %10d %10.2f' % (b'ACME', 100, 490.1)
# b'      ACME        100     490.10'

b'{} {} {}'.format(b'ACME', 100, 490.1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'bytes' object has no attribute 'format'


'{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii')
# b'ACME              100     490.10'


# UTF-8 파일 이름 작성
with open('jalape\xf1o.txt', 'w') as f:
    f.write('spicy')

# 디렉터리 리스트 구하기
import os
os.listdir('.')                 # 텍스트 문자열 (이름이 디코딩된다.)
# ['jalapeño.txt']
os.listdir(b'.')                # 바이트 문자열 (이름이 바이트로 남는다.)
# [b'jalape\xc3\xb1o.txt']
