# 2.11 문자열에서 문자 잘라내기

# 공백문 잘라내기
s = '    hello world \n'
s.strip()
# 'hello world'
s.lstrip()
# 'hello world \n'
s.rstrip()
# '    hello world'

# 문자 잘라내기
t = '-----hello====='
t.lstrip('-')
# 'hello====='
t.strip('-=')
# 'hello'


# 토론

s = ' hello        world     \n'
s = s.strip()
s
# 'hello        world'


s.replace(' ', '')
# 'helloworld'
import re
re.sub('\s+', ' ', s)
# 'hello world'


with open(filename) as f:
    lines = (line.strip() for line in f)
    for line in lines:
        ...
