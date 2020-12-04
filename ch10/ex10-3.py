# 10.3 상대 경로 패키지 서브모듈 임포트

mypackage/
    __init__.py
    A/
        __init__.py
        spam.py
        grok.py
    B/
        __init__.py
        bar.py


# mypackage/A/spam.py

from . import grok


# mypackage/A/spam.py

from ..B import bar



# 토론

# mypackage/A/spam.py

from mypackage.A import grok    # OK
from . import grok              # OK
import grok                     # Error (찾을 수 없음)


from . import grok    # OK
import .grok          # ERROR


% python3 mypackage/A/spam.py   # 상대적 임포트가 실패한다.

% python3 -m mypackage.A.spam   # 상대적 임포트가 동작한다.
