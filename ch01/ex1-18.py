# 1.18 시퀀스 요소에 이름 매핑

from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
sub
# Subscriber(addr='jonesy@example.com', joined='2012-10-19')
sub.addr
# 'jonesy@example.com'
sub.joined
# '2012-10-19'


len(sub)
# 2
addr, joined = sub
addr
# 'jonesy@example.com'
joined
# '2012-10-19'


def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total


from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


# 토론

s = Stock('ACME', 100, 123.45)
s
# Stock(name='ACME', shares=100, price=123.45)
s.shares = 75
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: can't set attribute


s = s._replace(shares=75)
s
# Stock(name='ACME', shares=75, price=123.45)


from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

# 프로토타입 인스턴스 생성
stock_prototype = Stock('', 0, 0.0, None, None)

# 딕셔너리 Stock으로 변환하는 함수
def dict_to_stock(s):
    return stock_prototype._replace(**s)


a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
dict_to_stock(a)
# Stock(name='ACME', shares=100, price=123.45, date=None, time=None)
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
dict_to_stock(b)
# Stock(name='ACME', shares=100, price=123.45, date='12/17/2012', time=None)
