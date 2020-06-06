# 4.6 추가 상태를 가진 제너레이터 함수 정의

from collections import deque

class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines,1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


with open('somefile.txt') as f:
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')


# 토론

f = open('somefile.txt')
lines = linehistory(f)
next(lines)
# Traceback (most recent call last):
#   File "<stdin>", in <module>
# TypeError: 'linehistory' object is not an iterator

# iter()를 먼저 호출하고, 순환을 시작한다.
it = iter(lines)
next(it)
# 'hello world\n'
next(it)
# 'this is a test\n'
