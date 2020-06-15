# 5.10 바이너리 파일 메모리 매핑

import os
import mmap

def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)


size = 1000000
with open('data', 'wb') as f:
    f.seek(size-1)
    f.write(b'\x00')


m = memory_map('data')
len(m)
# 1000000
m[0:10]
# b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
m[0]
# 0
# 슬라이스 재할당
m[0:11] = b'Hello World'
m.close()

# 수정 검증
with open('data', 'rb') as f:
    print(f.read(11))

# b'Hello World'


with memory_map('data') as m:
    print(len(m))
    print(m[0:10])

# 1000000
# b'Hello Worl'
m.closed
# True


m = memory_map(filename, mmap.ACCESS_READ)


m = memory_map(filename, mmap.ACCESS_COPY)


# 토론

m = memory_map('data')
# 부호 없는 정수형(unsigned integer)의 메모리뷰
v = memoryview(m).cast('I')
v[0] = 7
m[0:4]
# b'\x07\x00\x00\x00'
m[0:4] = b'\x07\x01\x00\x00'
v[0]
# 263
