# 1.8 딕셔너리 계산

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}


min_price = min(zip(prices.values(), prices.keys()))
# min_price는 (10.75, 'FB')이다.

max_price = max(zip(prices.values(), prices.keys()))
# max_price는 (612.78, 'AAPL')이다.


prices_sorted = sorted(zip(prices.values(), prices.keys()))
# prices_sorted는 [(10.75, 'FB'), (37.2, 'HPQ'),
#                  (45.23, 'ACME'), (205.55, 'IBM'),
#                  (612.78, 'AAPL')]이다.


prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))   # OK
print(max(prices_and_names))   # ValueError: max() 인자가 비어 있다.


# 토론

min(prices)   # 'AAPL'을 리턴한다.
max(prices)   # 'IBM'을 리턴한다


min(prices.values())  # 10.75를 리턴한다.
max(prices.values())  # 612.78을 리턴한다.


min(prices, key=lambda k: prices[k]) # 'FB'를 리턴한다.
max(prices, key=lambda k: prices[k]) # 'AAPL'을 리턴한다.


min_value = prices[min(prices, key=lambda k: prices[k])]


prices = { 'AAA' : 45.23, 'ZZZ': 45.23 }
min(zip(prices.values(), prices.keys()))
# (45.23, 'AAA')
max(zip(prices.values(), prices.keys()))
# (45.23, 'ZZZ')
