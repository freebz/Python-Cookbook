# 5.7 압축된 데이터 파일 읽고 쓰기

# gzip 압축
import gzip
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()

# bz2 압축
import bz2
with bz2.open('somefile.bz2', 'rt') as f:
    text = f.read()


# gzip 압축
import gzip
with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)

# bz2 압축
import bz2
with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)


# 토론

with gzip.open('somefile.gz', 'wt', compresslevel=5) as f:
    f.write(text)


import gzip

f = open('somefile.gz', 'rb')
with gzip.open(f, 'rt') as g:
    text = g.read()
