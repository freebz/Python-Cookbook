# 3.13 마지막 금요일 날짜 구하기

from datetime import datetime, timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']

def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date


datetime.today() # 참고용
# datetime.datetime(2012, 8, 28, 22, 4, 30, 263076)
get_previous_byday('Monday')
# datetime.datetime(2012, 8, 27, 22, 3, 57, 29045)
get_previous_byday('Tuesday') # 저번 주, 오늘 아님
# datetime.datetime(2012, 8, 21, 22, 4, 12, 629771)
get_previous_byday('Friday')
# datetime.datetime(2012, 8, 24, 22, 5, 9, 911393)


get_previous_byday('Sunday', datetime(2012, 12, 21))
# datetime.datetime(2012, 12, 16, 0, 0)


# 토론

from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *
d = datetime.now()
print(d)
# 2012-12-23 16:31:52.718111

# 다음 금요일
print(d + relativedelta(weekday=FR))
# 2012-12-28 16:31:52.718111

# 마지막 금요일
print(d + relativedelta(weekday=FR(-1)))
# 2012-12-21 16:31:52.718111
