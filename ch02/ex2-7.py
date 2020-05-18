# 2.7 가장 짧은 매칭을 위한 정규 표현식

str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
str_pat.findall(text1)
# ['no.']
text2 = 'Computer says "no." Phone says "yes."'
str_pat.findall(text2)
# ['no." Phone says "yes.']


str_pat = re.compile(r'\"(.*?)\"')
str_pat.findall(text2)
# ['no.', 'yes.']
