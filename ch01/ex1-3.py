# 1.3 마지막 N개 아이템 유지

from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# 파일 사용 예
if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)


# 토론

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
q
# deque([1, 2, 3], maxlen=3)
q.append(4)
q
# deque([2, 3, 4], maxlen=3)
q.append(5)
q
# deque([3, 4, 5], maxlen=3)


q = deque()
q.append(1)
q.append(2)
q.append(3)
q
# deque([1, 2, 3])
q.appendleft(4)
q
# deque([4, 1, 2, 3])
q.pop()
# 3
q
# deque([4, 1, 2])
q.popleft()
# 4
