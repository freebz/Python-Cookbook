# 8.14 커스텀 컨테이너 구현

import collections

class A(collections.Iterable):
    pass


a = A()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: Can't instantiate abstract class A with abstract methods __iter__


import collections
collections.Sequence()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: Can't instantiate abstract class Sequence with abstract methods __getitem__, __len__


import collections
import bisect

class SortedItems(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []

    # 필요한 시퀀스 메소드
    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    # 올바른 장소에 아이템을 추가하기 위한 메소드
    def add(self, item):
        bisect.insort(self._items, item)


items = SortedItems([5, 1, 3])
list(items)
# [1, 3, 5]
items[0]
# 1
items[-1]
# 5
items.add(2)
list(items)
# [1, 2, 3, 5]
items.add(-10)
list(items)
# [-10, 1, 2, 3, 5]
items[1:4]
# [1, 2, 3]
3 in items
# True
len(items)
# 5
for n in items:
    print(n)

# -10
# 1
# 2
# 3
# 5


# 토론

items = SortedItems()
import collections
isinstance(items, collections.Iterable)
# True
isinstance(items, collections.Sequence)
# True
isinstance(items, collections.Container)
# True
isinstance(items, collections.Sized)
# True
isinstance(items, collections.Mapping)
# False


class Items(collections.MutableSequence):
    def __init__(self, initial=None):
        self._items = list(initial) if initial is not None else []

    # 필요한 시퀀스 메소드
    def __getitem__(self, index):
        print('Getting:', index)
        return self._items[index]

    def __setitem__(self, index, value):
        print('Setting:', index, value)
        self._items[index] = value

    def __delitem__(self, index):
        print('Deleting:', index)
        del self._items[index]

    def insert(self, index, value):
        print('Inserting:', index, value)
        self._items.insert(index, value)

    def __len__(self):
        print('Len')
        return len(self._items)


a = Items([1, 2, 3])
len(a)
# Len
# 3
a.append(4)
# Len
# Inserting: 3 4
a.append(2)
# Len
# Inserting: 4 2
a.count(2)
# Getting: 0
# Getting: 1
# Getting: 2
# Getting: 3
# Getting: 4
# Getting: 5
# 2
a.remove(3)
# Getting: 0
# Getting: 1
# Getting: 2
# Deleting: 2
