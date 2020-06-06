# 4.3 제너레이터로 새로운 순환 패턴 생성

def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


for n in frange(0, 4, 0.5):
    print(n)

# 0
# 0.5
# 1.0
# 1.5
# 2.0
# 2.5
# 3.0
# 3.5
list(frange(0, 1, 0.125))
# [0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875]


# 토론

def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')

# 제너레이터 생성. 아무런 출력물이 없음에 주목한다.
c = countdown(3)
c
# <generator object countdown at 0x7f28eae54570>

# 값을 만들기 위한 첫 번째 실행
next(c)
# Starting to count from 3
# 3

# 다음 값을 위한 실행
next(c)
# 2

# 다음 값을 위한 실행
next(c)
# 1

# 다음 값을 위한 실행 (순환 종료)
next(c)
# Done!
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
