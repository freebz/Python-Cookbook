# 15.21 세그멘테이션 오류 진단

import faulthandler
faulthandler.enable()


# % python3 -Xfaulthandler program.py


# Fatal Python error: Segmentation fault
# Current thread 0x00007fff71106cc0:
#   File "example.py", line 6 in foo
#   File "example.py", line 10 in bar
#   File "example.py", line 14 in spam
#   File "example.py", line 19 in <module>
# Segmentation fault



# 토론
