# 1.6 딕셔너리의 키를 여러 값에 매핑하기

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
...

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
...


d = {} # 일반 딕셔너리
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)


# 토론

d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)


d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
