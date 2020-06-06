# 4.11 여러 시퀀스 동시에 순환

xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]
for x, y in zip(xpts, ypts):
    print(x,y)

# 1 101
# 5 78
# 4 37
# 2 15
# 10 62
# 7 99


a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
for i in zip(a,b):
    print(i)

# (1, 'w')
# (2, 'x')
# (3, 'y')


from itertools import zip_longest
for i in zip_longest(a,b):
    print(i)

# (1, 'w')
# (2, 'x')
# (3, 'y')
# (None, 'z')
for i in zip_longest(a, b, fillvalue=0):
    print(i)

# (1, 'w')
# (2, 'x')
# (3, 'y')
# (0, 'z')


# 토론

headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]


s = dict(zip(headers,values))


for name, val in zip(headers, values):
    print(name, '=', val)


a = [1, 2, 3]
b = [10, 11, 12]
c = ['x','y','z']
for i in zip(a, b, c):
    print(i)

# (1, 10, 'x')
# (2, 11, 'y')
# (3, 12, 'z')


zip(a, b)
# <zip object at 0x7f28eabc7a48>
list(zip(a, b))
# [(1, 10), (2, 11), (3, 12)]
