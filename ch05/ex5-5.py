# 5.5 존재하지 않는 파일에 쓰기

with open('somefile', 'wt') as f:
    f.write('Hello\n')

with open('somefile', 'xt') as f:
    f.write('Hello\n')

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# FileExistsError: [Errno 17] File exists: 'somefile'


# 토론

import os
if not os.path.exists('somefile'):
    with open('somefile', 'wt') as f:
        f.write('Hello\n')
else:
    print('File already exists!')

# File already exists!
