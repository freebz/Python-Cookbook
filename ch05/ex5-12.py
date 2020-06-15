# 5.12 파일 존재 여부 확인

import os
os.path.exists('/etc/passwd')
# True
os.path.exists('/tmp/spam')
# False


# 일반 파일인지 확인
os.path.isfile('/etc/passwd')
# True

# 디렉터리인지 확인
os.path.isdir('/etc/passwd')
# False

# 심볼릭 링크인지 확인
os.path.islink('/usr/local/bin/python3')
# True

# 연결된 파일 얻기
os.path.realpath('/usr/local/bin/python3')
# '/usr/local/bin/python3.3'


os.path.getsize('/etc/passwd')
# 3669
os.path.getmtime('/etc/passwd')
# 1272478234.0
import time
time.ctime(os.path.getmtime('/etc/passwd'))
# 'Wed Apr 28 13:10:34 2010'


# 토론

os.path.getsize('/Users/guido/Desktop/foo.txt')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/usr/local/lib/python3.3/genericpath.py", line 49, in getsize
#     return os.stat(filename).st_size
# PermissionError: [Errno 13] Permission denied: '/Users/guido/Desktop/foo.txt'
