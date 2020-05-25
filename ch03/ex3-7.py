# 3.7 무한대와 NaN 사용

a = float('inf')
b = float('-inf')
c = float('nan')
a
# inf
b
# -inf
c
# nan


math.isinf(a)
# True
math.isnan(c)
# True


# 토론

a = float('inf')
a + 45
# inf
a * 10
# inf
10 / a
# 0.0


a = float('inf')
a/a
# nan
b = float('-inf')
a + b
# nan


c = float('nan')
c + 23
# nan
c / 2
# nan
c * 2
# nan
math.sqrt(c)
# nan


c = float('nan')
d = float('nan')
c == d
# False
c is d
# False
