# 3.16 시간대 관련 날짜 처리

from datetime import datetime
from pytz import timezone
d = datetime(2012, 12, 21, 9, 30, 0)
print(d)
# 2012-12-21 09:30:00

# 시카고에 맞게 현지화
central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)
# 2012-12-21 09:30:00-06:00


# 방갈로르 시간으로 변환
bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(bang_d)
# 2012-12-21 21:00:00+05:30


d = datetime(2013, 3, 10, 1, 45)
loc_d = central.localize(d)
print(loc_d)
# 2013-03-10 01:45:00-06:00
later = loc_d + timedelta(minutes=30)
print(later)
# 2013-03-10 02:15:00-06:00    # 틀림! 틀림!


from datetime import timedelta
later = central.normalize(loc_d + timedelta(minutes=30))
print(later)
# 2013-03-10 03:15:00-05:00


# 토론

print(loc_d)
# 2013-03-10 01:45:00-06:00
utc_d = loc_d.astimezone(pytz.utc)
print(utc_d)
# 2013-03-10 07:45:00+00:00


later_utc = utc_d + timedelta(minutes=30)
print(later_utc.astimezone(central))
# 2013-03-10 03:15:00-05:00


pytz.country_timezones['IN']
# ['Asia/Kolkata']
