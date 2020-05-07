# 1.20 여러 매핑을 단일 매핑으로 합치기

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}


from collections import ChainMap
c = ChainMap(a,b)
print(c['x'])      # a의 1을 출력
print(c['y'])      # b의 2를 출력
print(c['z'])      # a의 3을 출력


# 토론

len(c)
# 3
list(c.keys())
# ['z', 'x', 'y']
list(c.values())
# [1, 2, 3]


c['z'] = 10
c['w'] = 40
del c['x']
a
# {'w': 40, 'z': 10}
del c['y']
# ...
# KeyError: "Key not found in the first mapping: 'y'"


values = ChainMap()
values['x'] = 1
# 새로운 매핑 추가
values = values.new_child()
values['x'] = 2
# 새로운 매핑 추가
values = values.new_child()
values['x'] = 3
values
# ChainMap({'x': 3}, {'x': 2}, {'x': 1})
values['x']
# 3
# 마지막 매핑 삭제
values = values.parents
values['x']
# 2
# 마지막 매핑 삭제
values = values.parents
values['x']
# 1
values
# ChainMap({'x': 1})


a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
merged = dict(b)
merged.update(a)
merged['x']
# 1
merged['y']
# 2
merged['z']
# 3


a['x'] = 13
merged['x']
# 1


a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
merged = ChainMap(a, b)
merged['x']
# 1
a['x'] = 42
merged['x']    # 합친 딕셔너리에 변경 알림
# 42
