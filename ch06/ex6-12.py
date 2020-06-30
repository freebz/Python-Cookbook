# 6.12 중첩, 가변 바이너리 구조체 읽기

polys = [
    [ (1.0, 2.5), (3.5, 4.0), (2.5, 1.5) ],
    [ (7.0, 1.2), (5.1, 3.0), (0.5, 7.5), (0.8, 9.0) ],
    [ (3.4, 6.3), (1.2, 0.5), (4.6, 9.2) ],
]


import struct
import itertools

def write_polys(filename, polys):
    # 충돌 박스 계산
    flattened = list(itertools.chain(*polys))
    min_x = min(x for x, y in flattened)
    max_x = max(x for x, y in flattened)
    min_y = min(y for x, y in flattened)
    max_y = max(y for x, y in flattened)

    with open(filename, 'wb') as f:
        f.write(struct.pack('<iddddi',
                            0x1234,
                            min_x, min_y,
                            max_x, max_y,
                            len(polys)))
        for poly in polys:
            size = len(poly) * struct.calcsize('<dd')
            f.write(struct.pack('<i', size+4))
            for pt in poly:
                f.write(struct.pack('<dd', *pt))

# 폴리곤 데이터를 가지고 호출
write_polys('polys.bin', polys)


import struct

def read_polys(filename):
    with open(filename, 'rb') as f:
        # 헤더 읽기
        header = f.read(40)
        file_code, min_x, min_y, max_x, max_y, num_polys = \
            struct.unpack('<iddddi', header)

        polys = []
        for n in range(num_polys):
            pbytes, = struct.unpack('<i', f.read(4))
            poly = []
            for m in range(pbytes // 16):
                pt = struct.unpack('<dd', f.read(16))
                poly.append(pt)
            polys.append(poly)
    return polys


import struct

class StructField:
    '''
    간단한 구조 필드를 나타내는 디스크립터
    '''
    def __init__(self, format, offset):
        self.format = format
        self.offset = offset
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            r = struct.unpack_from(self.format,
                                   instance._buffer, self.offset)
            return r[0] if len(r) == 1 else r

class Structure:
    def __init__(self, bytedata):
        self._buffer = memoryview(bytedata)


class PolyHeader(Structure):
    file_code = StructField('<i', 0)
    min_x = StructField('<d', 4)
    min_y = StructField('<d', 12)
    max_x = StructField('<d', 20)
    max_y = StructField('<d', 28)
    num_polys = StructField('<i', 36)


f = open('polys.bin', 'rb')
phead = PolyHeader(f.read(40))
phead.file_code == 0x1234
# True
phead.min_x
# 0.5
phead.min_y
# 0.5
phead.max_x
# 7.0
phead.max_y
# 9.2
phead.num_polys
# 3


class StructureMeta(type):
    '''
    StructField 디스크립터를 자동으로 만드는 메타클래스
    '''
    def __init__(self, clsname, bases, clsdict):
        fields = getattr(self, '_fields_', [])
        byte_order = ''
        offset = 0
        for format, fieldname in fields:
            if format.startswith(('<','>','!','@')):
                byte_order = format[0]
                format = format[1:]
            format = byte_order + format
            setattr(self, fieldname, StructField(format, offset))
            offset += struct.calcsize(format)
        setattr(self, 'struct_size', offset)

class Structure(metaclass=StructureMeta):
    def __init__(self, bytedata):
        self._buffer = bytedata

    @classmethod
    def from_file(cls, f):
        return cls(f.read(cls.struct_size))


class PolyHeader(Structure):
    _fields_ = [
        ('<i', 'file_code'),
        ('d', 'min_x'),
        ('d', 'min_y'),
        ('d', 'max_x'),
        ('d', 'max_y'),
        ('i', 'num_polys')
    ]


f = open('polys.bin', 'rb')
phead = PolyHeader.from_file(f)
phead.file_code == 0x1234
# True
phead.min_x
# 0.5
phead.min_y
# 0.5
phead.max_x
# 7.0
phead.max_y
# 9.2
phead.num_polys
# 3


class NestedStruct:
    '''
    중첩 구조를 표현하는 디스크립터
    '''
    def __init__(self, name, struct_type, offset):
        self.name = name
        self.struct_type = struct_type
        self.offset = offset
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            data = instance._buffer[self.offset:
                               self.offset+self.struct_type.struct_size]
            result = self.struct_type(data)
            # 결과 구조를 인스턴스에 저장해서 이 단계를
            # 다시 계산하지 않도록 한다.
            setattr(instance, self.name, result)
            return result

class StructureMeta(type):
    '''
    StructField 디스크립터를 자동으로 만드는 메타클래스
    '''
    def __init__(self, clasname, bases, clsdict):
        fields = getattr(self, '_fields_', [])
        byte_order = ''
        offset = 0
        for format, fieldname in fields:
            if isinstance(format, StructureMeta):
                setattr(self, fieldname,
                        NestedStruct(fieldname, format, offset))
                offset += format.struct_size
            else:
                if format.startswith(('<','>','!','@')):
                    byte_order = format[0]
                    format = format[1:]
                format = byte_order + format
                setattr(self, fieldname, StructField(format, offset))
                offset += struct.calcsize(format)
        setattr(self, 'struct_size', offset)

        
class Structure(metaclass=StructureMeta):
    def __init__(self, bytedata):
        self._buffer = bytedata

    @classmethod
    def from_file(cls, f):
        return cls(f.read(cls.struct_size))

    
class Point(Structure):
    _fields_ = [
        ('<d', 'x'),
        ('d', 'y')
    ]

class PolyHeader(Structure):
    _fields_ = [
        ('<i', 'file_code'),
        (Point, 'min'),         # 중첩 구조
        (Point, 'max'),         # 중첩 구조
        ('i', 'num_polys')
    ]


f = open('polys.bin', 'rb')
phead = PolyHeader.from_file(f)
phead.file_code == 0x1234
# True
phead.min    # 중첩구조
# <__main__.Point object at 0x7feffa473cc0>
phead.min.x
# 0.5
phead.min.y
# 0.5
phead.max.x
# 7.0
phead.max.y
# 9.2
phead.num_polys
# 3


class SizedRecord:
    def __init__(self, bytedata):
        self._buffer = memoryview(bytedata)

    @classmethod
    def from_file(cls, f, size_fmt, includes_size=True):
        sz_nbytes = struct.calcsize(size_fmt)
        sz_bytes = f.read(sz_nbytes)
        sz, = struct.unpack(size_fmt, sz_bytes)
        buf = f.read(sz - includes_size * sz_nbytes)
        return cls(buf)

    def iter_as(self, code):
        if isinstance(code, str):
            s = struct.Struct(code)
            for off in range(0, len(self._buffer), s.size):
                yield s.unpack_from(self._buffer, off)
        elif isinstance(code, StructureMeta):
            size = code.struct_size
            for off in range(0, len(self._buffer), size):
                data = self._buffer[off:off+size]
                yield code(data)


f = open('polys.bin', 'rb')
phead = PolyHeader.from_file(f)
phead.num_polys
# 3
polydata = [ SizedRecord.from_file(f, '<i')
             for n in range(phead.num_polys) ]
polydata
# [<__main__.SizedRecord object at 0x7feffa473dd8>,
#  <__main__.SizedRecord object at 0x7feffa473da0>,
#  <__main__.SizedRecord object at 0x7feffa4732e8>]


for n, poly in enumerate(polydata):
    print('Polygon', n)
    for p in poly.iter_as('<dd'):
        print(p)

# Polygon 0
# (1.0, 2.5)
# (3.5, 4.0)
# (2.5, 1.5)
# Polygon 1
# (7.0, 1.2)
# (5.1, 3.0)
# (0.5, 7.5)
# (0.8, 9.0)
# Polygon 2
# (3.4, 6.3)
# (1.2, 0.5)
# (4.6, 9.2)


for n, poly in enumerate(polydata):
    print('Polygon', n)
    for p in poly.iter_as(Point):
        print(p.x, p.y)

# Polygon 0
# 1.0 2.5
# 3.5 4.0
# 2.5 1.5
# Polygon 1
# 7.0 1.2
# 5.1 3.0
# 0.5 7.5
# 0.8 9.0
# Polygon 2
# 3.4 6.3
# 1.2 0.5
# 4.6 9.2


class Point(Structure):
    _fields_ = [
        ('<d', 'x'),
        ('d', 'y')
        ]

class PolyHeader(Structure):
    _fields_ = [
        ('<i', 'file_code'),
        (Point, 'min'),
        (Point, 'max'),
        ('i', 'num_polys')
    ]

def read_polys(filename):
    polys = []
    with open(filename, 'rb') as f:
        phead = PolyHeader.from_file(f)
        for n in range(phead.num_polys):
            rec = SizedRecord.from_file(f, '<i')
            poly = [ (p.x, p.y)
                     for p in rec.iter_as(Point) ]
            polys.append(poly)
    return polys


# 토론

class ShapeFile(Structure):
    _fields_ = [ ('>i', 'file_code'),       # 빅 엔디안
                 ('20s', 'unused'),
                 ('i', 'file_length'),
                 ('<i', 'version'),         # 리틀 엔디안
                 ('i', 'shape_type'),
                 ('d', 'min_x'),
                 ('d', 'min_y'),
                 ('d', 'max_x'),
                 ('d', 'max_y'),
                 ('d', 'min_z'),
                 ('d', 'max_z'),
                 ('d', 'min_m'),
                 ('d', 'max_m') ]
