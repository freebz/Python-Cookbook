# 8.24 비교 연산을 지원하는 클래스 만들기

from functools import total_ordering
class Room:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
        self.square_feet = self.length * self.width

@total_ordering
class House:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.rooms = list()

    @property
    def living_space_footage(self):
        return sum(r.square_feet for r in self.rooms)

    def add_room(self, room):
        self.rooms.append(room)

    def __str__(self):
        return '{}: {} square foot {}'.format(self.name,
                                              self.living_space_footage,
                                              self.style)

    def __eq__(self, other):
        return self.living_space_footage == other.living_space_footage

    def __lt__(self, other):
        return self.living_space_footage < other.living_space_footage


# 집을 몇 개 만들고 방을 추가한다
h1 = House('h1', 'Cape')
h1.add_room(Room('Master Bedroom', 14, 21))
h1.add_room(Room('Living Room', 18, 20))
h1.add_room(Room('Kitchen', 12, 16))
h1.add_room(Room('Office', 12, 12))

h2 = House('h2', 'Ranch')
h2.add_room(Room('Master Bedroom', 14, 21))
h2.add_room(Room('Living Room', 18, 20))
h2.add_room(Room('Kitchen', 12, 16))

h3 = House('h3', 'Split')
h3.add_room(Room('Master Bedroom', 14, 21))
h3.add_room(Room('Living Room', 18, 20))
h3.add_room(Room('Office', 12, 16))
h3.add_room(Room('Kitchen', 15, 17))
houses = [h1, h2, h3]

print('Is h1 bigger than h2?', h1 > h2) # True 출력
print('Is h2 smaller than h3>', h2 < h3) # True 출력
print('Which one is biggest?', max(houses)) # 'h3: 1101-square-foot Split' 출력
print('Which is smallest?', min(houses)) # 'h2: 846-square-foot Ranch' 출력



# 토론

class House:
    def __eq__(self, other):
        ...
    def __lt__(self, other):
        ...

    # @total_ordering이 생성한 메소드
    __le__ = lambda self, other: self < other or self == other
    __gt__ = lambda self, other: not (self < other or self == otehr)
    __ge__ = lambda self, other: not (self < other)
    __ne__ = lambda self, other: not self == other
