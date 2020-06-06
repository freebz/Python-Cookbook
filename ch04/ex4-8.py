# 4.8 순환 객체 첫 번째 부분 건너뛰기

with open('/etc/passwd') as f:
    for line in f:
        print(line, end='')

##
# User Database
#
# Note that this file is consulted directly only when the system is running
# in single-user mode. At other times, this information is provided by
# Open Directory.
# ...
##
# nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
# root:*:0:0:System Administrator:/var/root:/bin/sh
# ...


from itertools import dropwhile
with open('/etc/passwd') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')


from itertools import islice
items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x)

# 1
# 4
# 10
# 15


# 토론

with open('/etc/passwd') as f:
    # 처음 주석을 건너뛴다.
    while True:
        line = next(f, '')
        if not line.startswith('#'):
            break

    # 남아 있는 라인을 처리한다.
    while line:
        # 의미 있는 라인으로 치환한다.
        print(line, end='')
        line = next(f, None)


with open('/etc/passwd') as f:
    lines = (line for line in f if not line.startswith('#'))
    for line in lines:
        print(line, end='')
