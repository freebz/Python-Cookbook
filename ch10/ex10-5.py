# 10.5 공통된 네임스페이스에 코드 임포트 디렉터리 만들기

foo-package/
    spam/
        blah.py

bar-package/
    spam/
        grok.py


import sys
sys.path.extend(['foo-package', 'bar-package'])
import spam.blah
import spam.grok



# 토론

import spam
spam.__path__
# _NamespacePath(['foo-backage/spam', 'bar-package/spam'])


my-package
    spam/
        custom.py


import spam.custom
import spam.grok
import spam.blah


spam.__file__
# Traceback (most recent call last0:
#   File "<stdin>", line 1, in <module>
# AttributeError: 'module' object has no attribute '__file__'

spam
# <module 'spam' (namespace)>
