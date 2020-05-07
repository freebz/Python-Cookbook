# 1.11 슬라이스 이름 붙이기

###### 01234567890123456789012345678901234567890123456789012345678901234567890'
record = '....................100         ........513.25  .........'
const = int(record[20:32]) * float(record[40:48])


SHARES = slice(20,32)
PRICE = slice(40,48)

const = int(record[SHARES]) * float(record[PRICE])


# 토론

items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
items[2:4]
# [2, 3]
items[a]
# [2, 3]
items[a] = [10,11]
items
# [0, 1, 10, 11, 4, 5, 6]
del items[a]
items
# [0, 1, 4, 5, 6]


a = slice(10, 50, 2)
a.start
# 10
a.stop
# 50
a.step
# 2


a = slice(5, 50, 2)


s = 'HelloWorld'
a.indices(len(s))
# (5, 10, 2)
for i in range(*a.indices(len(s))):
    print(s[i])
# W
# r
# d
