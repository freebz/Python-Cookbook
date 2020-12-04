# 10.10 문자열로 주어진 모듈 이름 임포트

import importlib
math = importlib.import_module('math')
math.sin(2)
# 0.9092974268256817
mod = importlib.import_module('urllib.request')
u = mod.urlopen('http://www.python.org')


import importlib

# 'from . import b'와 동일
b = importlib.import_module('.b', __package__)



# 토론
