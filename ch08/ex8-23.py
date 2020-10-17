# 8.23 순환 자료 구조에서 메모리 관리

import weakref

class Node:
    def __init__(self, value):
        self.value = value
        self._parent = None
        self.children = []

    def __repr__(self):
        return 'Node({!r})'.format(self.value)

    # 부모를 약한 참조로 관리하는 프로퍼티
    @property
    def parent(self):
        return self._parent if self._parent is None else self._parent()

    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)
        
    def add_child(self, child):
        self.children.append(child)
        child.parent = self


root = Node('parent')
c1 = Node('child')
root.add_child(c1)
print(c1.parent)
# Node('parent')
del root
print(c1.parent)
# None



# 토론

# 삭제 시기를 알려 주기 위한 클래스
class Data:
    def __del__(self):
        print('Data.__del__')

# 순환 구조가 있는 Node 클래스
class Node:
    def __init__(self):
        self.data = Data()
        self.parent = None
        self.children = []
    def add_child(self, child):
        self.children.append(child)
        child.parent = self


a = Data()
del a               # 즉시 삭제
# Data.__del__
a = Node()
del a               # 즉시 삭제
# Data.__del__
a = Node()
a.add_child(Node())
del a               # 삭제되지 않음(메시지 없음)


import gc
gc.collect()        # 강제 실행
# Data.__del__
# Data.__del__


# 삭제 시기를 알려 주기 위한 클래스
class Data:
    def __del__(self):
        print('Data.__del__')

# 순환 구조가 있는 Node 클래스
class Node:
    def __init__(self):
        self.data = Data()
        self.parent = None
        self.children = []

    # 절대로 다음과 같이 하지 않는다!
    # 이해를 돋기 위한 코드이다.
    def __del__(self):
        del self.data
        del parent
        del children

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


a = Node()
a.add_child(Node())
del a               # 메시지 없음(가비지 컬렉션 발생하지 않음)
import gc
gc.collect()        # 메시지 없음(가비지 컬렉션 발생하지 않음)


import weakref
a = Node()
a_ref = weakref.ref(a)
a_ref
# <weakref at 0x7fccef2b6908; to 'Node' at 0x7fccf5130a90>


print(a_ref())
# <__main__.Node object at 0x7fccf5130a90>
del a
# Data.__del__
print(a_ref())
# None
