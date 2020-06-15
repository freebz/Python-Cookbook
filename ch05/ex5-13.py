# 5.13 디렉터리 리스팅 구하기

import os
names = os.listdir('somedir')


import os.path
# 일반 파일 모두 구하기
names = [name for name in os.listdir('somedir')
         if os.path.isfile(os.path.join('somedir', name))]

# 디렉터리 모두 구하기
dirnames = [name for name in os.listdir('somedir')
            if os.path.isdir(os.path.join('somedir', name))]


pyfiles = [name for name in os.listdir('somedir')
           if name.endswith('.py')]


import glob
pyfiles = glob.glob('somedir/*.py')

from fnmatch import fnmatch
pyfiles = [name for name in os.listdir('somedir')
           if fnmatch(name, '*.py')]


# 토론

# 디렉터리 리스트 구하기

import os
import os.path
import glob

pyfiles = glob.glob('*.py')

# 파일 크기와 수정 날짜 구하기
name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name))
                for name in pyfiles]

# 대안: 파일 메타데이터 구하기
file_metadata = [(name, os.stat(name)) for name in pyfiles]
for name, meta in file_metadata:
    print(name, meta.st_size, meta.st_mtime)
