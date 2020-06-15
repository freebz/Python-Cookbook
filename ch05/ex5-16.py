# 5.16 이미 열려 있는 파일의 인코딩을 수정하거나 추가하기

import urllib.request
import io

u = urllib.request.urlopen('http://www.python.org')
f = io.TextIOWrapper(u,encoding='utf-8')
text = f.read()


import sys
sys.stdout.encoding
# 'UTF-8'
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')
sys.stdout.encoding
# 'latin-1'


# 토론

f = open('sample.txt', 'w')
f
# <_io.TextIOWrapper name='sample.txt' mode='w' encoding='UTF-8'>
f.buffer
# <_io.BufferedWriter name='sample.txt'>
f.buffer.raw
# <_io.FileIO name='sample.txt' mode='wb' closefd=True>


f
# <_io.TextIOWrapper name='sample.txt' mode='w' encoding='UTF-8'>
f = io.TextIOWrapper(f.buffer, encoding='latin-1')
f
# <_io.TextIOWrapper name='sample.txt' encoding='latin-1'>
f.write('Hello')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: I/O operation on closed file.


f = open('sample.txt', 'w')
f
# <_io.TextIOWrapper name='sample.txt' mode='w' encoding='UTF-8'>
b = f.detach()
b
# <_io.BufferedWriter name='sample.txt'>
f.write('hello')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: underlying buffer has been detached


f = io.TextIOWrapper(b, encoding='latin-1')
f
# <_io.TextIOWrapper name='sample.txt' encoding='latin-1'>


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='ascii',
                              errors='xmlcharrefreplace')
print('Jalape\u00f1o')
# Jalape&#241;o
