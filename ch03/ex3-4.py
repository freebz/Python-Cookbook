# 3.4 2진수, 8진수, 16진수 작업

x = 1234
bin(x)
# '0b10011010010'
oct(x)
# '0o2322'
hex(x)
# '0x4d2'


format(x, 'b')
# '10011010010'
format(x, 'o')
# '2322'
format(x, 'x')
# '4d2'


x = -1234
format(x, 'b')
# '-10011010010'
format(x, 'x')
# '-4d2'


x = -1234
format(2**32 + x, 'b')
# '11111111111111111111101100101110'
format(2**32 + x, 'x')
# 'fffffb2e'


int('4d2', 16)
# 1234
int('10011010010', 2)
# 1234


# 토론

import os
# os.chmod('script.py', 0755)
#   File "<stdin>", line 1
#     os.chmod('script.py', 0755)
#                              ^
# SyntaxError: invalid token


os.chmod('script.py', 0o755)
