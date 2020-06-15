# 5.2 파일에 출력

with open('somefile.txt', 'wt') as f:
    print('Hello World!', file=f)
