# 1.1 시퀀스를 개별 변수로 나누기

p = (4, 5)
x, y = p
x
# 4
y
# 5

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, date = data
name
# 'ACME'
date
# (2012, 12, 21)

name, shares, price, (year, mon, day) = data
name
# 'ACME'
year
# 2012
mon
# 12
day
# 21


p = (4, 5)
x, y, z = p
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: not enough values to unpack (expected 3, got 2)


# 토론

s = 'Hello'
a, b, c, d, e = s
a
# 'H'
b
# 'e'
e
# 'o'


data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
_, shares, price, _ = data
shares
# 50
price
# 91.1
