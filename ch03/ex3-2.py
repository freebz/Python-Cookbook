# 3.2 정확한 10진수 계산

a = 4.2
b = 2.1
a + b
# 6.300000000000001
(a + b) == 6.3
# False


from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
a + b
# Decimal('6.3')
print(a + b)
# 6.3
(a + b) == Decimal('6.3')
# True


from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')
print(a / b)
# 0.7647058823529411764705882353
with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)

# 0.765
with localcontext() as ctx:
    ctx.prec = 50
    print(a / b)

# 0.76470588235294117647058823529411764705882352941176


# 토론

nums = [1.23e+18, 1, -1.23e+18]
sum(nums)    # 1이 사라진다.
# 0.0


import math
math.fsum(nums)
# 1.0
