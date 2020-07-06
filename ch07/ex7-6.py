# 7.6 이름 없는 함수와 인라인 함수 정의

add = lambda x, y: x + y
add(2,3)
# 5
add('hello', 'world')
# 'helloworld'


def add(x, y):
    return x + y

add(2,3)
# 5


names = ['David Beazley', 'Brian Jones',
         'Raymond Hettinger', 'Ned Batchelder']
sorted(names, key=lambda name: name.split()[-1].lower())
# ['Ned Batchelder', 'David Beazley', 'Raymond Hettinger', 'Brian Jones']
