# 15.19 C에서 파일 같은 객체 읽기

import io
f = io.StringIO('Hello\nWorld\n')
import sample
sample.consume_file(f)
# Hello
# World



# 토론
