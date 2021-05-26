# 13.12 라이브러리에 로그 추가

# somelib.py

import logging
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

# 예제 함수 (테스팅)
def func():
    log.critical('A Critical Error!')
    log.debug('A debug message')


import somelib
somelib.func()


import logging
logging.basicConfig()
somelib.func()
# CRITICAL:somelib:A Critical Error!



# 토론

import logging
logging.basicConfig(level=logging.ERROR)
import somelib
somelib.func()
# CRITICAL:somelib:A Critical Error!

# 'somelib'의 로깅 레벨 변경
logging.getLogger('somelib').level=logging.DEBUG
somelib.func()
# CRITICAL:somelib:A Critical Error!
# DEBUG:somelib:A debug message
