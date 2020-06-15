# 5.17 텍스트 파일에 바이트 쓰기

import sys
sys.stdout.write(b'Hello\n')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: write() argument must be str, not bytes
sys.stdout.buffer.write(b'Hello\n')
# Hello
# 6
