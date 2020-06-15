# 5.9 바이너리 데이터를 수정 가능한 버퍼에 넣기

import os.path

def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf


# 샘플 파일 쓰기
with open('sample.bin', 'wb') as f:
    f.write(b'Hello World')

buf = read_into_buffer('sample.bin')
buf
# bytearray(b'Hello World')
buf[0:5] = b'Hallo'
buf
# bytearray(b'Hallo World')
with open('newsample.bin', 'wb') as f:
    f.write(buf)

# 11


# 토론

record_size = 32          # 레코드의 크기 (값을 조절)

buf = bytearray(record_size)
with open('somefile', 'rb') as f:
    while True:
        n = f.readinto(buf)
        if n < record_size:
            break
        # buf 내용을 사용
        ...


buf
# bytearray(b'Hello World')
m1 = memoryview(buf)
m2 = m1[-5:]
# <memory at 0x7fb04ae77708>
m2[:] = b'WORLD'
buf
# bytearray(b'Hello WORLD')
