# 3.10 행렬과 선형 대수 계산

import numpy as np
m = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])
m
# matrix([[ 1, -2,  3],
#         [ 0,  4,  5],
#         [ 7,  8, -9]])

# 전치 행렬(transpose)
m.T
# matrix([[ 1,  0,  7],
#         [-2,  4,  8],
#         [ 3,  5, -9]])

# 역행렬(inverse)
m.I
# matrix([[ 0.33043478, -0.02608696,  0.09565217],
#         [-0.15217391,  0.13043478,  0.02173913],
#         [ 0.12173913,  0.09565217, -0.0173913 ]])

# 벡터를 만들고 곱하기
v = np.matrix([[2],[3],[4]])
v
# matrix([[2],
#         [3],
#         [4]])
m * v
# matrix([[ 8],
#         [32],
#         [ 2]])


import numpy.linalg

# Determinant
numpy.linalg.det(m)
# -229.99999999999983

# Eigenvalues
numpy.linalg.eigvals(m)
# array([-13.11474312,   2.75956154,   6.35518158])

# mx = v에서 x 풀기
x = numpy.linalg.solve(m, v)
x
# matrix([[0.96521739],
#         [0.17391304],
#         [0.46086957]])
m * x
# matrix([[2.],
#         [3.],
#         [4.]])
v
# matrix([[2],
#         [3],
#         [4]])
