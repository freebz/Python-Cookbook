# 1.17 딕셔너리의 부분 추출

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# 가격이 200 이상인 것에 대한 딕셔너리
p1 = { key:value for key, value in prices.items() if value > 200 }

# 기술 관련 주식으로 딕셔너리 구성
tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
p2 = { key:value for key,value in prices.items() if key in tech_names }


# 토론

p1 = dict((key, value) for key, value in prices.items() if value > 200)


# 기술 관련 주식으로 딕셔너리 구성
tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
p2 = { key:prices[key] for key in prices.keys() & tech_names }
