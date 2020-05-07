# 1.2 임의 순환체의 요소 나누기

def drop_first_last(grades):
    firt, *middle, last = grades
    return avg(middle)


user_record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = user_record
name
# 'Dave'
email
# 'dave@example.com'
phone_numbers
# ['773-555-1212', '847-555-1212']


*trailing_qtrs, current_qtr = sales_record
trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
return avg_comparison(trailing_avg, current_qtr)


*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
trailing
# [10, 8, 7, 1, 9, 5, 10]
current
# 3


# 토론

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
uname
# 'nobody'
homedir
# '/var/empty'
sh
# '/usr/bin/false'


record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
name
# 'ACME'
year
# 2012


items = [1, 10, 7, 4, 5, 9]
head, *tail = items
head
# 1
tail
# [10, 7, 4, 5, 9]


def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

sum(items)
# 36
