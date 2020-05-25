# 3.8 분수 계산

from fractions import Fraction
a = Fraction(5, 4)
b = Fraction(7, 16)
print(a + b)
# 27/16
print(a * b)
# 35/64

# 분자 / 분모 구하기
c = a * b
c.numerator
# 35
c.denominator
# 64

# 소수로 변환
float(c)
# 0.546875

# 분자를 특정 값으로 제한
print(c.limit_denominator(8))
# 4/7

# 소수를 분수로 변환
x = 3.75
y = Fraction(*x.as_integer_ratio())
y
# Fraction(15, 4)
