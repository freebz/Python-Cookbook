# 7.5 기본 인자를 사용하는 함수 정의

def spam(a, b=42):
    print(a, b)

spam(1)         # Ok. a=1, b=42
spam(1, 2)      # Ok. a=1, b=2


# 기본 값으로 리스트 사용
def spam(a, b=None):
    if b is None:
        b = []
    ...


_no_value = object()

def spam(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')
    ...


spam(1)
# No b value supplied
spam(1, 2)      # b = 2
spam(1, None)   # b = None


# 토론

x = 42
def spam(a, b=x):
    print(a, b)

spam(1)
# 1 42
x = 23      # 효과 없음
spam(1)
# 1 42


def spam(a, b=[]):      # No!
    ...


def spam(a, b=[]):
    print(b)
    return b

x = spam(1)
x
# []
x.append(99)
x.append('Yow!')
x
# [99, 'Yow!']
spam(1)         # 수정된 리스트가 반환된다!
# [99, 'Yow!']


def spam(a, b=None):
    if not b:      # 주의! 'b is None'을 사용해야 한다.
        b = []
    ...


spam(1)         # 올바름
x = []
spam(1, x)      # 에러. x 값이 기본으로 덮어쓰여진다.
spam(1, 0)      # 에러. 0이 무시된다.
spam(1, '')     # 에러. ''이 무시된다.
