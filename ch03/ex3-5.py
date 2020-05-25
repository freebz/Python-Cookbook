# 3.5 바이트에서 큰 숫자를 패킹/언패킹

data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'


len(data)
# 16
int.from_bytes(data, 'little')
# 69120565665751139577663547927094891008
int.from_bytes(data, 'big')
# 94522842520747284487117727783387188


x = 94522842520747284487117727783387188
x.to_bytes(16, 'big')
# b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
x.to_bytes(16, 'little')
# b'4\x00#\x00\x01\xef\xcd\x00\xab\x90x\x00V4\x12\x00'


# 토론

data
# b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
import struct
hi, lo = struct.unpack('>QQ', data)
(hi << 64) + lo
# 94522842520747284487117727783387188


x = 0x01020304
x.to_bytes(4, 'big')
# b'\x01\x02\x03\x04'
x.to_bytes(4, 'little')
# b'\x04\x03\x02\x01'


x = 523 ** 23
x
# 335381300113661875107536852714019056160355655333978849017944067
x.to_bytes(16, 'little')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# OverflowError: int too big to convert
x.bit_length()
# 208
nbytes, rem = divmod(x.bit_length(), 8)
if rem:
    nbytes += 1
    
x.to_bytes(nbytes, 'little')
# b'\x03X\xf1\x82iT\x96\xac\xc7c\x16\xf3\xb9\xcf\x18\xee\xec\x91\xd1\x98\xa2\xc8\xd9R\xb5\xd0'
