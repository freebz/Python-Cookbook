# 1.19 데이터를 변환하면서 줄이기

nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)


# 디렉터리에 또 다른 .py 파일이 있는지 살펴본다.
import os
files = os.listdir('dirname')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')

# 튜플을 CSV로 출력한다.
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# 자료 구조의 필드를 줄인다.
portfolio = [
    {'name':'GOOG', 'shares': 50},
    {'name':'AOL', 'shares': 20},
    {'name':'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)


# 토론

s = sum((x * x for x in nums))  # 생성자 표현식을 인자로 전달
s = sum(x * x for x in nums)    # 더 우아한 방식


nums = [1, 2, 3, 4, 5]
s = sum([x * x for x in nums])


# 원본: 20을 반환
min_shares = min(s['shares'] for s in portfolio)

# 대안: {'name': 'AOL', 'shares': 20}을 반환
min_shares = min(portfolio, key=lambda s: s['shares'])
