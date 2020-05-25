# 3.15 문자열을 시간으로 변환

from datetime import datetime
text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
diff = z - y
diff
# datetime.timedelta(3, 77824, 177393)


# 토론

z
# datetime.datetime(2012, 9, 23, 21, 37, 4, 177393)
nice_z = datetime.strftime(z, '%A %B %d, %Y')
nice_z
# 'Sunday September 23, 2012'


from datetime import datetime
def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))
