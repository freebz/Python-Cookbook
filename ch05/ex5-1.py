# 5.1 텍스트 데이터 읽고 쓰기

# 파일 전체를 하나의 문자열로 읽음
with open('somefile.txt', 'rt') as f:
    data = f.read()

# 파일의 줄을 순환
with open('somefile.txt', 'rt') as f:
    for line in f:
        # 라인 처리
        ...


# 텍스트 데이터 쓰기
with open('somefile.txt', 'wt') as f:
    f.write(text1)
    f.write(text2)
    ...

# 리다이렉트한 print 문
with open('somefile.txt', 'wt') as f:
    print(line1, file=f)
    print(line2, file=f)
    ...


# 토론

f = open('someifle.txt', 'rt')
data = f.read()
f.close()


# 줄바꿈 변환 없이 읽기
with open('somefile.txt', 'rt', newline='') as f:
    ...


# 줄바꿈 변환 사용(기본)
f = open('hello.txt', 'rt')
f.read()
# 'hello world!\n'

# 줄바꿈 변환 미사용
g = open('hello.txt', 'rt', newline='')
g.read()
# 'hello world!\r\n'


f = open('sample.txt', 'rt', encoding='ascii')
f.read()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/usr/local/lib/python3.3/encodings/ascii.py", line 26, in decode
#     return codecs.ascii_decode(input, self.errors)[0]
# UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 12: ordinal not in range(128)


# 알 수 없는 문자를 유니코드 U+fffd로 치환
f = open('sample.txt', 'rt', encoding='ascii', errors='replace')
f.read()
# 'Spicy Jalape?o!'
# 알 수 없는 문자를 무시
g = open('sample.txt', 'rt', encoding='ascii', errors='ignore')
g.read()
'Spicy Jalapeo!'
