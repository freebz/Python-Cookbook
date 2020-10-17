# 8.1 인스턴스의 문자열 표현식 변형

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)
    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)

    
p = Pair(3, 4)
p
# Pair(3, 4)      # __repr__() 결과
print(p)
# (3, 4)          # __str__() 결과


p = Pair(3, 4)
print('p is {0!r}'.format(p))
# p is Pair(3, 4)
print('p is {0}'.format(p))
# p is (3, 4)


# 토론

f = open('file.dat')
f
# <_io.TextIOWrapper name='file.dat' mode='r' encoding='UTF-8'>


def __repr__(self):
    return 'Pair({0.x!r}, {0.y!r})'.format(self)


def __repr__(self):
    return 'Pair(%r, %r)' % (self.x, self.y)
