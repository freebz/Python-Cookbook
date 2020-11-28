# 9.25 파이썬 바이트 코드 디스어셈블

def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
    print('Blastoff!')

import dis
dis.dis(countdown)
#   4     >>    0 LOAD_FAST                0 (n)
#               2 LOAD_CONST               1 (0)
#               4 COMPARE_OP               4 (>)
#               6 POP_JUMP_IF_FALSE       28

#   5           8 LOAD_GLOBAL              0 (print)
#              10 LOAD_CONST               2 ('T-minus')
#              12 LOAD_FAST                0 (n)
#              14 CALL_FUNCTION            2
#              16 POP_TOP

#   6          18 LOAD_FAST                0 (n)
#              20 LOAD_CONST               3 (1)
#              22 INPLACE_SUBTRACT
#              24 STORE_FAST               0 (n)
#              26 JUMP_ABSOLUTE            0

#   7     >>   28 LOAD_GLOBAL              0 (print)
#              30 LOAD_CONST               4 ('Blastoff!')
#              32 CALL_FUNCTION            1
#              34 POP_TOP
#              36 LOAD_CONST               0 (None)
#              38 RETURN_VALUE



# 토론

countdown.__code__.co_code
# b'|\x00d\x01k\x04r\x1ct\x00d\x02|\x00\x83\x02\x01\x00|\x00d\x038\x00}\x00q\x00t\x00d\x04\x83\x01\x01\x00d\x00S\x00'


c = countdown.__code__.co_code
import opcode
opcode.opname[c[0]]
opcode.opname[c[0]]
# 'SETUP_LOOP'
opcode.opname[c[3]]
# 'LOAD_FAST'


import opcode

def generate_opcodes(codebytes):
    extended_arg = 0
    i = 0
    n = len(codebytes)
    while i < n:
        op = codebytes[i]
        i += 1
        if op >= opcode.HAVE_ARGUMENT:
            oparg = codebytes[i] + codebytes[i+1]*256 + extended_arg
            extended_arg = 0
            i += 2
            if op == opcode.EXTENDED_ARG:
                extended_arg = oparg * 65536
                continue
        else:
            oparg = None
        yield (op, oparg)


for op, oparg in generate_opcodes(countdown.__code__.co_code):
    print(op, opcode.opname[op], oparg)
    
# 124 LOAD_FAST 25600
# 1 POP_TOP None
# 107 COMPARE_OP 29188
# 28 INPLACE_FLOOR_DIVIDE None
# 116 LOAD_GLOBAL 25600
# 2 ROT_TWO None
# 124 LOAD_FAST 33536
# 2 ROT_TWO None
# 1 POP_TOP None
# 0 <0> None
# 124 LOAD_FAST 25600
# 3 ROT_THREE None
# 56 INPLACE_SUBTRACT None
# 0 <0> None
# 125 STORE_FAST 28928
# 0 <0> None
# 116 LOAD_GLOBAL 25600
# 4 DUP_TOP None
# 131 CALL_FUNCTION 257
# 0 <0> None
# 100 LOAD_CONST 21248
# 0 <0> None


def add(x, y):
    return x + y

c = add.__code__
c
# <code object add at 0x7f0d79aae450, file "/home/fx/work/Python Cookbook/ch09/ex9-25.py", line 100>
c.co_code
# b'|\x00|\x01\x17\x00S\x00'

# 가짜 바이트 코드로 완전히 새로운 코드 객체를 만든다.
import types
newbytecode = b'xxxxxxx'
nc = types.CodeType(c.co_argcount, c.co_posonlyargcount, c.co_kwonlyargcount,
    c.co_nlocals, c.co_stacksize, c.co_flags, newbytecode, c.co_consts,
    c.co_names, c.co_varnames, c.co_filename, c.co_name,
    c.co_firstlineno, c.co_lnotab)
nc
# <code object add at 0x7f0d79a2ca80, file "/home/fx/work/Python Cookbook/ch09/ex9-25.py", line 100>
add.__code__ = nc
add(2,3)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     return x + y
# SystemError: unknown opcode
