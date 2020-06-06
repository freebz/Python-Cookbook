# 4.13 데이터 처리 파이프라인 생성

import os
import fnmatch
import gzip
import bz2
import re

def gen_find(filepat, top):
    '''
    디렉터리 트리에서 와일드카드 패턴에 매칭하는 모든 파일 이름을 찾는다.
    '''
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path,name)

def gen_opener(filenames):
    '''
    파일 이름 시퀀스를 하나씩 열어 파일 객체를 생성한다.
    다음 순환으로 넘어가는 순간 파일을 닫는다.
    '''
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close()

def gen_concatenate(iterators):
    '''
    이터레이터 시퀀스를 합쳐 하나의 시퀀스로 만든다.
    '''
    for it in iterators:
        yield from it

def gen_grep(pattern, lines):
    '''
    라인 시퀀스에서 정규식 패턴을 살펴본다.
    '''
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line


lognames = gen_find('access-log*', 'www')
files = gen_opener(lognames)
lines = gen_concatenate(files)
pylines = gen_grep('(?i)python', lines)
for line in pylines:
    print(line)


lognames = gen_find('access-log*', 'www')
files = gen_opener(lognames)
lines = gen_concatenate(files)
pylines = gen_grep('(?i)python', lines)
bytecolumn = (line.rsplit(None,1)[1] for line in pylines)
bytes = (int(x) for x in bytecolumn if x != '-')
print('Total', sum(bytes))
