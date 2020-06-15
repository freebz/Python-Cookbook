# 5.6 문자열에 입출력 작업하기

import io

s = io.StringIO()
s.write('Hello World\n')
# 12
print('This is a test', file=s)
# 15
# 기록한 모든 데이터 얻기
s.getvalue()
# 'Hello World\nThis is a test\n'

# 기존 문자열을 파일 인터페이스로 감싸기
s = io.StringIO('Hello\nWorld\n')
s.read(4)
# 'Hell'
s.read()
# 'o\nWorld\n'


s = io.BytesIO()
s.write(b'binary data')
s.getvalue()
# b'binary data'
