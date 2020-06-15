# 5.3 구별자나 종단 부호 바꾸기

print('ACME', 50, 91.5)
# ACME 50 91.5
print('ACME', 50, 91.5, sep=',')
# ACME,50,91.5
print('ACME', 50, 91.5, sep=',', end='!!\n')
# ACME,50,91.5!!


for i in range(5):
    print(i)

# 0
# 1
# 2
# 3
# 4
for i in range(5):
    print(i, end=' ')

# 0 1 2 3 4


# 토론

print(','.join(('ACME','50','91.5')))
# ACME,50,91.5


row = ('ACME', 50, 91.5)
print(','.join(row))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: sequence item 1: expected str instance, int found
print(','.join(str(x) for x in row))
# ACME,50,91.5


print(*row, sep=',')
# ACME,50,91.5
