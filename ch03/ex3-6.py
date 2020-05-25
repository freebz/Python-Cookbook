# 3.6 복소수 계산

a = complex(2, 4)
b = 3 - 5j
a
# (2+4j)
b
# (3-5j)


a.real
# 2.0
a.imag
# 4.0
a.conjugate()
# (2-4j)


a + b
# (5-1j)
a * b
# (26+2j)
a / b
# (-0.4117647058823529+0.6470588235294118j)
abs(a)
# 4.47213595499958


import cmath
cmath.sin(a)
# (24.83130584894638-11.356612711218173j)
cmath.cos(a)
# (-11.36423470640106-24.814651485634183j)
cmath.exp(a)
# (-4.829809383269385-5.5920560936409816j)


# 토론

import numpy as np
a = np.array([2+3j, 4+5j, 6-7j, 8+9j])
a
# array([2.+3.j, 4.+5.j, 6.-7.j, 8.+9.j])
a + 2
# array([ 4.+3.j,  6.+5.j,  8.-7.j, 10.+9.j])
np.sin(a)
# array([   9.15449915  -4.16890696j,  -56.16227422 -48.50245524j,
#        -153.20827755-526.47684926j, 4008.42651446-589.49948373j])


import math
math.sqrt(-1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: math domain error


import cmath
cmath.sqrt(-1)
# 1j
