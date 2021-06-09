# 15.12 함수 포인터를 호출 가능하도록 만들기

import ctypes
lib = ctypes.cdll.LoadLibrary(None)
# C math 라이브러리의 sin()의 주소를 구한다.
addr = ctypes.cast(lib.sin, ctypes.c_void_p).value
addr
# 4352992

# 주소를 호출 가능한 함수로 바꾼다.
functype = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
func = functype(addr)
func
# <CFunctionType object at 0x7f97183dff40>

# 결과 함수를 호출한다.
func(2)
# 0.9092974268256817
func(0)
# 0.0



# 토론

from llvm.core import Module, Function, Type, Builder
mod = Module.new('example')
f = Function.new(mod,Type.function(Type.double(), \
                 [Type.double(), Type.double()], False), 'foo')
block = f.append_basic_block('entry')
builder = Builder.new(block)
x2 = builder.fmul(f.args[0],f.args[0])
y2 = builder.fmul(f.args[1],f.args[1])
r = builder.fadd(x2,y2)
builder.ret(r)
# <llvm.core.Instruction object at 0x10078e990>
from llvm.ee import ExecutionEngine
engine = ExecutionEngine.new(mod)
ptr = engine.get_pointer_to_function(f)
ptr
# 4325863440
foo = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)(ptr)

# 결과 함수 호출
foo(2,3)
# 13.0
foo(4,5)
# 41.0
foo(1,2)
# 5.0
