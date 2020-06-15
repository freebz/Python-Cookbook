# 5.19 임시 파일과 디렉터리 만들기

from tempfile import TemporaryFile

with TemporaryFile('w+t') as f:
    # 파일에서 읽기/쓰기
    f.write('Hello World\n')
    f.write('Testing\n')

    # 처음으로 이동해 데이터를 읽는다.
    f.seek(0)
    data = f.read()

# 임시 파일은 파기된다.


f = TemporaryFile('w+t')
# 임시 파일 사용
...
f.close()
# 파일 파기


with TemporaryFile('w+t', encoding='utf-8', errors='ignore') as f:
    ...


from tempfile import NamedTemporaryFile

with NamedTemporaryFile('w+t') as f:
    print('filename is:', f.name)
    ...

# 파일이 자동으로 파기된다.


with NamedTemporaryFile('w+t', delete=False) as f:
    print('filename is:', f.name)
    ...


from tempfile import TemporaryDirectory
with TemporaryDirectory() as dirname:
    print('dirname is:', dirname)
    # Use the directory
    ...
# 디렉터리와 모든 내용물이 파기된다.


# 토론

import tempfile
tempfile.mkstemp()
# (10, '/tmp/tmpkhi2tfl6')
tempfile.mkdtemp()
# '/tmp/tmphe72mih1'


tempfile.gettempdir()
# '/tmp'


f = NamedTemporaryFile(prefix='mytemp', suffix='.txt', dir='/tmp')
f.name
# '/tmp/mytemp5r2he1x4.txt'
