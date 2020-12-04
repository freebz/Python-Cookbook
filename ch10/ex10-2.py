# 10.2 일괄 임포트 제어

# somemodule.py

def spam():
    pass

def grok():
    pass

blah = 42

# 'spam'과 'grok'만 내보낸다.
__all__ = ['spam', 'grok']



# 토론

from module import *
