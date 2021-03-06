# 4.9 가능한 모든 순열과 조합 순환

items = ['a', 'b', 'c']
from itertools import permutations
for p in permutations(items):
    print(p)

# ('a', 'b', 'c')
# ('a', 'c', 'b')
# ('b', 'a', 'c')
# ('b', 'c', 'a')
# ('c', 'a', 'b')
# ('c', 'b', 'a')


for p in permutations(items, 2):
    print(p)

# ('a', 'b')
# ('a', 'c')
# ('b', 'a')
# ('b', 'c')
# ('c', 'a')
# ('c', 'b')


from itertools import combinations
for c in combinations(items, 3):
    print(c)

# ('a', 'b', 'c')
for c in combinations(items, 2):
    print(c)

# ('a', 'b')
# ('a', 'c')
# ('b', 'c')
for c in combinations(items, 1):
    print(c)

# ('a',)
# ('b',)
# ('c',)


from itertools import  combinations_with_replacement
for c in combinations_with_replacement(items, 3):
    print(c)

# ('a', 'a', 'a')
# ('a', 'a', 'b')
# ('a', 'a', 'c')
# ('a', 'b', 'b')
# ('a', 'b', 'c')
# ('a', 'c', 'c')
# ('b', 'b', 'b')
# ('b', 'b', 'c')
# ('b', 'c', 'c')
# ('c', 'c', 'c')
