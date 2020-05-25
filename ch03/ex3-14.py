# 3.14 현재 달의 날짜 범위 찾기

from datetime import datetime, date, timedelta
import calendar

def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date, end_date)


a_day = timedelta(days=1)
first_day, last_day = get_month_range()
while first_day < last_day:
    print(first_day)
    first_day += a_day

# 2012-08-01
# 2012-08-02
# 2012-08-03
# 2012-08-04
# 2012-08-05
# 2012-08-06
# 2012-08-07
# 2012-08-08
# 2012-08-09
# #... 등등...


# 토론

def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step


for d in date_range(datetime(2012, 9, 1), datetime(2012,10,1),
                    timedelta(hours=6)):
    print(d)

# 2012-09-01 00:00:00
# 2012-09-01 06:00:00
# 2012-09-01 12:00:00
# 2012-09-01 18:00:00
# 2012-09-02 00:00:00
# 2012-09-02 06:00:00
# ...
