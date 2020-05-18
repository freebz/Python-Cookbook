# 2.4 텍스트 패턴 매칭과 검색

text =  'yeah, but no, but yeah, but no, but yeah'

# 정확한 매칭
text == 'yeah'
# False

# 처음이나 끝에 매칭
text.startswith('yeah')
# True
text.endswith('no')
# False

# 처음 나타난 곳 검색
text.find('no')
# 10


text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re
# 간단한 매칭: \d+는 하나 이상의 숫자를 의미
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

# yes
if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')

# no


datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')

# yes
if datepat.match(text2):
    print('yes')
else:
    print('no')

# no


text =  'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat.findall(text)
# ['11/27/2012', '3/13/2013']


datepat = re.compile(r'(\d+)/(\d+)/(\d+)')


m = datepat.match('11/27/2012')
m
# <_sre.SRE_Match object; span=(0, 10), match='11/27/2012'>

# 각 그룹에서 내용 추출
m.group(0)
# '11/27/2012'
m.group(1)
# '11'
m.group(2)
# '27'
m.group(3)
# '2012'
m.groups()
# ('11', '27', '2012')
month, day, year = m.groups()

# 전체 매칭 찾기(튜플로 나눈다.)
text
# 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat.findall(text)
# [('11', '27', '2012'), ('3', '13', '2013')]
for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))

# 2012-11-27
# 2013-3-13
    

for m in datepat.finditer(text):
    print(m.groups())

# ('11', '27', '2012')
# ('3', '13', '2013')


# 토론

m = datepat.match('11/27/2012abcdef')
m
# <_sre.SRE_Match object; span=(0, 10), match='11/27/2012'>
m.group()
# '11/27/2012'


datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
datepat.match('11/27/2012abcdef')
datepat.match('11/27/2012')
# <_sre.SRE_Match object; span=(0, 10), match='11/27/2012'>


re.findall(r'(\d+)/(\d+)/(\d+)', text)
# [('11', '27', '2012'), ('3', '13', '2013')]
