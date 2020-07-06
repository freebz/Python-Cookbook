# 7.4 함수에서 여러 값을 반환

def myfun():
    return 1, 2, 3

a, b, c = myfun()
a
# 1
b
# 2
c
# 3


# 토론

a = (1, 2)      # 괄호 사용
a
# (1, 2)
b = 1, 2,       # 괄호 미사용
b
# (1, 2)


x = myfun()
x
# (1, 2, 3)
