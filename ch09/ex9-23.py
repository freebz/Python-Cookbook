# 9.23 지역변수 문제 없이 코드 실행

a = 13
exec('b = a + 1')
print(b)
# 14


def test():
    a = 13
    exec('b = a + 1')
    print(b)

test()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 4, in test
# NameError: name 'b' is not defined


def test():
    a = 13
    loc = locals()
    exec('b = a + 1')
    b = loc['b']
    print(b)

test()
# 14



# 토론

def test1():
    x = 0
    exec('x += 1')
    print(x)

test1()
# 0


def test2():
    x = 0
    loc = locals()
    print('before:', loc)
    exec('x += 1')
    print('after:', loc)
    print('x = ', x)

test2()
# before: {'x': 0}
# after: {'x': 1, 'loc': {...}}
# x =  0


def test3():
    x = 0
    loc = locals()
    print(loc)
    exec('x += 1')
    print(loc)
    locals()
    print(loc)

test3()
# {'x': 0}
# {'x': 1, 'loc': {...}}
# {'x': 0, 'loc': {...}}


def test4():
    a = 13
    loc = { 'a' : a }
    glb = { }
    exec('b = a + 1', glb, loc)
    b = loc['b']
    print(b)

test4()
# 14
