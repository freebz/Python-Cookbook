# 13.2 에러 메시지와 함께 프로그램 종료

raise SystemExit('It failed!')



# 토론

import sys
sys.stderr.write('It failed!\n')
raise SystemExit(1)
