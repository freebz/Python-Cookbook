# 4.10 인덱스-값 페어 시퀀스 순환

my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list):
    print(idx, val)

# 0 a
# 1 b
# 2 c


my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list, 1):
    print(idx, val)

# 1 a
# 2 b
# 3 c


def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(fields[1])
                ...
            except ValueError as e:
                print('Line {}: Parse error: {}'.format(lineno, e))


from collections import defaultdict
word_summary = defaultdict(list)

with open('myfile.txt', 'r') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    # 현재 라인에 단어 리스트를 생성
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)


# 토론

lineno = 1
for line in f:
    # 라인 처리
    ...
    lineno += 1


for lineno, line in enumerate(e):
    # 라인 처리
    ...


data = [ (1, 2), (3, 4), (5, 6), (7, 8) ]

# 올바른 방법!
for n, (x, y) in enumerate(data):
    ...

# 에러
for n, x, y in enumerate(data):
    ...
