# 13.1 리다이렉션, 파이프, 입력 파일을 통한 스크립트 입력 받기

#!/usr/bin/env python3
import fileinput

with fileinput.input() as f_input:
    for line in f_input:
        print(line, end='')



# 토론

import fileinput
with fileinput.input('/etc/passwd') as f:
    for line in f:
        print(f.filename(), f.lineno(), line, end='')
