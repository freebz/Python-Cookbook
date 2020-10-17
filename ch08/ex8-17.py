# 8.17 init 호출 없이 인스턴스 생성

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


d = Date.__new__(Date)
d
# <__main__.Date object at 0x7f9e10c71b38>
d.year
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'Date' object has no attribute 'year'


data = {'year':2012, 'month':8, 'day':29}
for key, value in data.items():
    setattr(d, key, value)

d.year
# 2012
d.month
# 8


# 토론

from time import localtime

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        d = cls.__new__(cls)
        t = localtime()
        d.year = t.tm_year
        d.month = t.tm_mon
        d.day = t.tm_mday
        return d


data = { 'year': 2012, 'month': 8, 'day': 29 }
