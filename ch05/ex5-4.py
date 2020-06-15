# 5.4 바이너리 데이터 읽고 쓰기

# 파일 전체를 하나의 바이트 문자열로 읽기
with open('somefile.bin', 'rb') as f:
    data = f.read()

# 바이너리 데이터 파일에 쓰기
with open('somefile.bin', 'wb') as f:
    f.write(b'Hello World')


# 토론

# 텍스트 문자열
t = 'Hello World'
t[0]
# 'H'
for c in t:
    print(c)

# H
# e
# l
# l
# o
# ...
# 바이트 문자열
b = b'Hello World'
b[0]
# 72
for c in b:
    print(c)

# 72
# 101
# 108
# 108
# 111
# ...


with open('somefile.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')

with open('somefile.bin', 'wb') as f:
    text = 'Hello World'
    f.write(text.encode('utf-8'))


import array
nums = array.array('i', [1, 2, 3, 4])
with open('data.bin', 'wb') as f:
    f.write(nums)


import array
a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
with open('data.bin', 'rb') as f:
    f.readinto(a)

# 16
a
array('i', [1, 2, 3, 4, 0, 0, 0, 0])
