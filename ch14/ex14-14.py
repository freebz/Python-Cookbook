# 14.14 프로그램 실행 속도 향상

# somescript.py

import sys
import csv

with open(sys.argv[1]) as f:
    for row in csv.reader(f):

        # 작업 수행
        ...


# 함수 사용

# somescript.py
import sys
import csv

def main(filename):
    with open(filename) as f:
        for row in csv.reader(f):
            # Some kind of processing
            ...

main(sys.argv[1])


# 속성 접근의 선택적 삭제

import math

def compute_roots(nums):
    result = []
    for n in nums:
        result.append(math.sqrt(n))
    return result

# 테스트
nums = range(1000000)
for n in range(100):
    r = compute_roots(nums)


from math import sqrt

def compute_roots(nums):
    result = []
    result_append = result.append
    for n in nums:
        result_append(sqrt(n))
    return result


# 변수의 지역성 이해

import math

def compute_roots(nums):
    sqrt = math.sqrt
    result = []
    result_append = result.append
    for n in nums:
        result_append(sqrt(n))
    return result


# 느림
class SomeClass:
    ...
    def method(self):
        for x in s:
            op(self.value)

# 빠름
class SomeClass:
    ...
    def method(self):
        value = self.value
        for x in s:
            op(value)


# 불필요한 추상화 피하기

class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, value):
        self._y = value


from timeit import timeit
a = A(1,2)
timeit('a.x', 'from __main__ import a')
# 0.045616441988386214
timeit('a.y', 'from __main__ import a')
# 0.11643141601234674


# 내장 컨테이너 사용

# 불필요한 자료 구조 생성이나 복사 피하기

values = [x for x in sequence]
squares = [x*x for x in values]


squares = [x*x for x in sequence]



# 토론

a = {
    'name' : 'AAPL',
    'shares' : 100,
    'price' : 534.22
    }

b = dict(name='AAPL', shares=100, price=534.22)
