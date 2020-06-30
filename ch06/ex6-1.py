# 6.1 CSV 데이터 읽고 쓰기

import csv
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # 행 처리
        ...


from collections import namedtuple
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    Row = namedtuple('Row', headings)
    for r in f_csv:
        row = Row(*r)
        # 행 처리
        ...


import csv
with open('stocks.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        # 행 처리
        ...


headers = ['Symbol','Price','Date','Time','Change','Volume']
rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
        ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
        ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
       ]

with open('stocks.csv','w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)


headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volumn']
rows = [{'Symbol':'AA', 'Price':39.48, 'Date':'6/11/2007',
          'Time':'9:36am', 'Change':-0.18, 'Volumn':181800},
        {'Symbol':'AIG', 'Price': 71.38, 'Date':'6/11/2007',
         'Time':'9:36am', 'Change':-0.15, 'Volumn': 195500},
        {'Symbol':'AXP', 'Price': 62.58, 'Date':'6/11/2007',
         'Time':'9:36am', 'Change':-0.46, 'Volumn': 935000},
       ]

with open('stocks.csv','w') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)


# 토론

with open('stocks.csv') as f:
    for line in f:
        row = line.split(',')
        # 행 처리
        ...


# 탭으로 구분한 값 읽기 예제
with open('stocks.tsv') as f:
    f_tsv = csv.reader(f, delimiter='\t')
    for row in f_tsv:
        # 행 처리
        ...


# Street Address,Num-Premises,Latitude,Longitude
# 5412 N CLARK,10,41.980262,-87.668452


import re
with open('stock.csv') as f:
    f_csv = csv.reader(f)
    headers = [ re.sub('[^a-zA-Z_]', '_', h) for h in next(f_csv) ]
    Row = namedtuple('Row', headers)
    for r in f_csv:
        row = Row(*r)
        # 행 처리
        ...


col_types = [str, float, str, str, float, int]
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # 행 아이템에 변환 적용
        row = tuple(convert(value) for convert, value in zip(col_types, row))
        ...


print('Reading as dicts with type conversion')
field_types = [ ('Price', float),
                ('Change', float),
                ('Volume', int) ]

with open('stocks.csv') as f:
    for row in csv.DictReader(f):
        row.update((key, conversion(row[key]))
                   for key, conversion in field_types)
        print(row)
