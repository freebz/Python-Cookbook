# 15.13 C 라이브러리에 NULL로 끝나는 문자열 전달

print_chars(b'Hello World')
# 48 65 6c 6c 6f 20 57 6f 72 6c 64
print_chars(b'HEllo\x00World')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: must be bytes without null bytes, not bytes
print_chars('Hello World')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' does not support the buffer interface


print_chars('Hello World')
# 48 65 6c 6c 6f 20 57 6f 72 6c 64
print_chars('Spicy Jalape\u00f1o') # 노트: UTF-8 인코딩
# 53 70 69 20 4a 61 6c 61 70 65 c3 b1 6f
print_chars('Hello\x00World')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: must be str without null characters, not str
print_chars(b'Hello World')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: must be str, not bytes



# 토론

import sys
s = 'Spicy Jalape\u00f1o'
sys.getsizeof(s)
# 87
print_chars(s)      # 문자열 전달
# 53 70 69 63 79 20 4a 61 6c 61 70 65 c3 b1 6f
sys.getsizeof(s)    # 크기 증가 확인
# 103


import sys
s = 'Spicy Jalape\u00f1o'
sys.getsizeof(s)
# 87
print_chars(s)      # 문자열 전달
# 53 70 69 63 79 20 4a 61 6c 61 70 65 c3 b1 6f
sys.getsizeof(s)    # 크기 증가 확인
# 87


import ctypes
lib = ctypes.cdll.LoadLibrary("./libsample.so")
print_chars = lib.print_chars
print_chars.argtypes = (ctypes.c_char_p,)
print_chars(b'Hello World')
# 48 65 6c 6c 6f 20 57 6f 72 6c 64
print_chars(b'Hello\x00World')
# 48 65 6c 6c 6f
print_chars('Hello World')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ctypes.ArgumentError: argument 1: <class 'TypeError'>: wrong type


print_chars('Hello World'.encode('utf-8'))
# 48 65 6c 6c 6f 20 57 6f 72 6c 64
