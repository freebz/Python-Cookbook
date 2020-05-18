# 2.1 여러 구분자로 문자열 나누기

line = 'asdf fjdk; afed, fjek,asdf,      foo'
import re
re.split(r'[;,\s]\s*', line)
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']


# 토론

fields = re.split(r'(;|,|\s)\s*', line)
fields
# ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']


values = fields[::2]
delimiters = fields[1::2] + ['']
values
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
delimiters
# [' ', ';', ',', ',', ',', '']

# 동일한 구분자로 라인을 구성한다.
''.join(v+d for v,d in zip(values, delimiters))
# 'asdf fjdk;afed,fjek,asdf,foo'


re.split(r'(?:,|;|\s)\s*', line)
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
