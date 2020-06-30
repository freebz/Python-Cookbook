# 6.11 바이너리 배열 구조체 읽고 쓰기

from struct import Struct

def write_records(records, format, f):
    '''
    일련의 튜플을 구조체의 바이너리 파일에 기록
    '''
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))

# 예제
if __name__ == '__main__':
    records = [ (1, 2.3, 4.5),
                (6, 7.8, 9.0),
                (12, 13.4, 56.7) ]

    with open('data.b', 'wb') as f:
        write_records(records, '<idd', f)


from struct import Struct

def read_records(format, f):
    record_struct = Struct(format)
    chunks = iter(lambda: f.read(record_struct.size), b'')
    return (record_struct.unpack(chunk) for chunk in chunks)

# 예제
if __name__ == '__main__':
    with open('data.b', 'rb') as f:
        for rec in read_records('<idd', f):
            # rec 처리
            ...


from struct import Struct

def unpack_records(format, data):
    record_struct = Struct(format)
    return (record_struct.unpack_from(data, offset)
            for offset in range(0, len(data), record_struct.size))

# 예제
if __name__ == '__main__':
    with open('data.b', 'rb') as f:
        data = f.read()

    for rec in unpack_records('<idd', data):
        # rec 처리
        ...


# 토론

# 리틀 엔디안 32비트 정수, 소수점 두 자리 정확도 부동 소수점
record_struct = Struct('<idd')


from struct import Struct
record_struct = Struct('<idd')
record_struct.size
# 20
record_struct.pack(1, 2.0, 3.0)
# b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x08@'
record_struct.unpack(_)
# (1, 2.0, 3.0)


import struct
struct.pack('<idd', 1, 2.0, 3.0)
# b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x08@'
struct.unpack('<idd', _)
# (1, 2.0, 3.0)


f = open('data.b', 'rb')
chunks = iter(lambda: f.read(20), b'')
chunks
# <callable_iterator object at 0x7ff002be2da0>
for chk in chunks:
    print(chk)

# b'\x01\x00\x00\x00ffffff\x02@\x00\x00\x00\x00\x00\x00\x12@'
# b'\x06\x00\x00\x00333333\x1f@\x00\x00\x00\x00\x00\x00"@'
# b'\x0c\x00\x00\x00\xcd\xcc\xcc\xcc\xcc\xcc*@\x9a\x99\x99\x99\x99YL@'


def read_records(format, f):
    record_struct = Struct(format)
    while True:
        chk = f.read(record_struct.size)
        if chk == b'':
            break
        yield record_struct.unpack(chk)
    return records


def unpack_records(format, data):
    record_struct = Struct(format)
    return (record_struct.unpack(data[offset:offset + record_struct.size])
            for offset in range(0, len(data), record_struct.size))


from collections import namedtuple

Record = namedtuple('Record', ['kind','x','y'])

with open('data.p', 'rb') as f:
    records = (Record(*r) for r in read_records('<idd', f))

for r in records:
    print(r.kind, r.x, r.y)


import numpy as np
f = open('data.b', 'rb')
records = np.fromfile(f, dtype='<i,<d,<d')
records
# array([( 1,  2.3,  4.5), ( 6,  7.8,  9. ), (12, 13.4, 56.7)],
#       dtype=[('f0', '<i4'), ('f1', '<f8'), ('f2', '<f8')])
records[0]
# (1, 2.3, 4.5)
records[1]
# (6, 7.8, 9.)
