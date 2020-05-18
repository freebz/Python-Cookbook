# 2.10 정규 표현식에 유니코드 사용

import re
num = re.compile('\d+')
# 아스키(ASCII) 숫자
num.match('123')
# <_sre.SRE_Match object; span=(0, 3), match='123'>

# 아라비아 숫자
num.match('\u0661\u0662\u0663')
# <_sre.SRE_Match object; span=(0, 3), match='١٢٣'>


arabic = re.compile('[\u06000-\u06ff\u0750-\u077f\u08a0-\u08ff]+')


pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
pat.match(s)              # 일치
# <_sre.SRE_Match object; span=(0, 6), match='straße'>
pat.match(s.upper())      # 불일치
s.upper()                 # 대문자 변환
# 'STRASSE'
