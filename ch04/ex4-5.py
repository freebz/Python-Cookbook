# 4.5 역방향 순환

a = [1, 2, 3, 4]
for x in reversed(a):
    print(x)

# 4
# 3
# 2
# 1


# 파일을 거꾸로 출력하기
f = open('somefile')
for line in reversed(list(f)):
    print(line, end='')


# 토론

class Countdown:
    def __init__(self, start):
        self.start = start

    # 순방향 순환
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # 역방향 순환
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1
