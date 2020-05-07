# 1.5 우선 순위 큐 구현

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
q.pop()
# Item('bar')
q.pop()
# Item('spam')
q.pop()
# Item('foo')
q.pop()
# Item('grok')


# 토론

a = Item('foo')
b = Item('bar')
a < b
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: '<' not supported between instances of 'Item' and 'Item'


a = (1, Item('foo'))
b = (5, Item('bar'))
a < b
# True
c = (1, Item('grok'))
a < c
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: '<' not supported between instances of 'Item' and 'Item'


a = (1, 0, Item('foo'))
b = (5, 1, Item('bar'))
c = (1, 2, Item('grok'))
a < b
# True
a < c
# True
