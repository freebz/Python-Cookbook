# 8.20 문자열로 이름이 주어진 객체의 메소드 호출

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({!r:},{!r:})'.format(self.x, self.y)

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)

p = Point(2, 3)
d = getattr(p, 'distance')(0, 0)  # p.distance(0, 0) 호출


import operator
operator.methodcaller('distance', 0, 0)(p)


points = [
    Point(1, 2),
    Point(3, 0),
    Point(10, -3),
    Point(-5, -7),
    Point(-1, -8),
    Point(3, 2)
]

# origin (0, 0)의 거리를 기준으로 정렬
points.sort(key=operator.methodcaller('distance', 0, 0))



# 토론

p = Point(3, 4)
d = operator.methodcaller('distance', 0, 0)
d(p)
# 5.0
