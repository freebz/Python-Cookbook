# 10.6 모듈 리로드

import spam
import imp
imp.reload(spam)
# <module 'spam' from './spam.py'>



# 토론

# spam.py

def bar():
    print('bar')

def grok():
    print('grok')


import spam
from spam import grok
spam.bar()
# bar
grok()
# grok


def grok():
    print('New grok')


import imp
imp.reload(spam)
# <module 'spam' from './spam.py'>
spam.bar()
# bar
grok()                 # 기존 출력
# grok
spam.grok()            # 새로운 출력
# New grok
