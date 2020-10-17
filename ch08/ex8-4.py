# 8.4 인스턴스를 많이 생성할 때 메모리 절약

class Date:
    __slots__ = ['year', 'month', 'day']
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
