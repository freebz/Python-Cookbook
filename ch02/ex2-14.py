# 2.14 문자열 합치기

parts = ['Is', 'Chicago', 'Not', 'Chicago?']
' '.join(parts)
# 'Is Chicago Not Chicago?'
','.join(parts)
# 'Is,Chicago,Not,Chicago?'
''.join(parts)
# 'IsChicagoNotChicago?'


a = 'Is Chicago'
b = 'Not Chicago?'
a + ' ' + b
# 'Is Chicago Not Chicago?'


print('{} {}'.format(a,b))
# Is Chicago Not Chicago?
print(a + ' ' + b)
# Is Chicago Not Chicago?


a = 'Hello' 'World'
a
# 'HelloWorld'


# 토론

s = ''
for p in parts:
    s += p


data = ['ACME', 50, 91.1]
','.join(str(d) for d in data)
# 'ACME,50,91.1'


print(a + ':' + b + ':' + c)    # 좋지 않다.
print(':'.join([a, b, c]))      # 여전히 개선할 점이 있다.

print(a, b, c, sep=':')         # 좋은 방식이다.


# 버전 1 (무자열 합치기)
f.write(chunk1 + chunk2)

# 버전 2 (개별 입출력 수행)
f.write(chunk1)
f.write(chunk2)


def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'


text = ''.join(sample())


for part in sample():
    f.write(part)


def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)

for part in combine(sample(), 32768):
    f.write(part)
