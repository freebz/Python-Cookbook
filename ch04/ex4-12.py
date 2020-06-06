# 4.12 서로 다른 컨테이너 아이템 순환

from itertools import chain
a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
for x in chain(a, b):
    print(x)

# 1
# 2
# 3
# 4
# x
# y
# z


# 여러 아이템 세트
active_items = set()
inactive_items = set()

# 모든 아이템 한번에 순환
for item in chain(active_items, inactive_items):
    # 작업
    ...


for item in active_items:
    # 작업
    ...

for item in inactive_items:
    # 작업
    ...


# 토론

# 비효율적
for x in a + b:
    ...

# 더 나은 방식
for x in chain(a, b):
    ...
