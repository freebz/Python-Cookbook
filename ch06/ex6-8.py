# 6.8 관계형 데이터베이스 작업

stocks = [
    ('GOOG', 100, 490.1),
    ('AAPL', 50, 545.75),
    ('FB', 150, 7.45),
    ('HPQ', 75, 33.2),
]


import sqlite3
db = sqlite3.connect('database.db')


c = db.cursor()
c.execute('create table portfolio (symbol text, shares integer, price real)')
# <sqlite3.Cursor object at 0x7ff0010b8d50>
db.commit()


c.executemany('insert into portfolio values (?,?,?)', stocks)
# <sqlite3.Cursor object at 0x7ff0010b8d50>
db.commit()


for row in db.execute('select * from portfolio'):
    print(row)

# ('GOOG', 100, 490.1)
# ('AAPL', 50, 545.75)
# ('FB', 150, 7.45)
# ('HPQ', 75, 33.2)


min_price = 100
for row in db.execute('select * from portfolio where price >= ?',
                      (min_price,)):
    print(row)

# ('GOOG', 100, 490.1)
# ('AAPL', 50, 545.75)
