# 1.13 일반 키로 딕셔너리 리스트 정렬

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]


from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

print(rows_by_fname)
print(rows_by_uid)


# [{'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
#  {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
#  {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
#  {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}]

# [{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
#  {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
#  {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
#  {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}]


rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)


[{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
 {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
 {'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
 {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003}]


# 토론

rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'],r['fname']))


min(rows, key=itemgetter('uid'))
# {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}
max(rows, key=itemgetter('uid'))
# {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
