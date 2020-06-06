# 4.1 수동으로 이터레이터 소비

with open('/etc/passwd') as f:
    try:
        while True:
            line = next(f)
            print(line, end='')
    except StopIteration:
        pass


with open('/etc/passwd') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')


# 토론

items = [1, 2, 3]
# 이터레이터 얻기
it = iter(items)    # items.__iter__() 실행
# 이터레이터 실행
next(it)            # it.__next__() 실행
# 1
next(it)
# 2
next(it)
# 3
next(it)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
