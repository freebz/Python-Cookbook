# 3.12 시간 단위 변환

from datetime import timedelta
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
c.days
# 2
c.seconds
# 37800
c.seconds / 3600
# 10.5
c.total_seconds() / 3600
# 58.5


from datetime import datetime
a = datetime(2012, 9, 23)
print(a + timedelta(days=10))
# 2012-10-03 00:00:00

b = datetime(2012, 12, 21)
d = b - a
d.days
# 89
now = datetime.today()
print(now)
# 2012-12-21 14:54:43.094063
print(now + timedelta(minutes=10))
# 2012-12-21 15:04:43.094063


a = datetime(2012, 3, 1)
b = datetime(2012, 2, 28)
a - b
# datetime.timedelta(2)
(a - b).days
# 2
c = datetime(2013, 3, 1)
d = datetime(2013, 2, 28)
(c - d).days
# 1


# 토론

a = datetime(2012, 9, 23)
a + timedelta(months=1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'months' is an invalid keyword argument for this function

from dateutil.relativedelta import relativedelta
a + relativedelta(months=+1)
# datetime.datetime(2012, 10, 23, 0, 0)
a + relativedelta(months=+4)
# datetime.datetime(2013, 1, 23, 0, 0)

# 두 날짜 사이의 시간
b = datetime(2012, 12, 21)
d = b - a
# datetime.timedelta(89)
d = relativedelta(b, a)
# relativedelta(months=+2, days=+28)
d.months
# 2
d.days
# 28
