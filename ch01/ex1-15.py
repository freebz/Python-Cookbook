# 1.15 필드에 따라 레코드 묶기

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]


from operator import itemgetter
from itertools import groupby

# 우선 원하는 필드로 정렬한다.
rows.sort(key=itemgetter('date'))

# 그룹 내부에서 순환한다.
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print('    ', i)


# 07/01/2012
#      {'address': '5412 N CLARK', 'date': '07/01/2012'}
#      {'address': '4801 N BROADWAY', 'date': '07/01/2012'}
# 07/02/2012
#      {'address': '5800 E 58TH', 'date': '07/02/2012'}
#      {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'}
#      {'address': '1060 W ADDISON', 'date': '07/02/2012'}
# 07/03/2012
#      {'address': '2122 N CLARK', 'date': '07/03/2012'}
# 07/04/2012
#      {'address': '5148 N CLARK', 'date': '07/04/2012'}
#      {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}


# 토론

from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)


for r in rows_by_date['07/01/2012']:
    print(r)

# {'address': '5412 N CLARK', 'date': '07/01/2012'}
# {'address': '4801 N BROADWAY', 'date': '07/01/2012'}
