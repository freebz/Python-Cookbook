# 8.16 클래스에 생성자 여러 개 정의

import time

class Date:
    # 기본 생성자
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # 대안 생성자
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


a = Date(2012, 12, 21)  # 기본
b = Date.today()        # 대안


# 토론

class NewDate(Date):
    pass

c = Date.today()       # Date (cls=Date) 인스턴스 생성
d = NewDate.today()    # NewDate (cls=NewDate) 인스턴스 생성


class Date:
    def __init__(self, *args):
        if len(args) == 0:
            t = time.localtime()
            args = (t.tm_year, t.tm_mon, t.tm_mday)
        self.year, self.month, self.day = args


a = Date(2012, 12, 21)  # 명확하다. 특정 날짜 지정
b = Date()              # ??? 무슨 의미인지?

# Class method version
c = Date.today()        # 명확하다. 오늘의 날짜
