# 2.9 유니코드 텍스트 노멀화

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
s1
# 'Spicy Jalapeño'
s2
# 'Spicy Jalapeño'
s1 == s2
# False
len(s1)
# 14
len(s2)
# 15


import unicodedata
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
t1 == t2
# True
print(ascii(t1))
# 'Spicy Jalape\xf1o'

t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
t3 == t4
# True
print(ascii(t3))
# 'Spicy Jalapen\u0303o'


s = '\ufb01'    # 단일 문자
s
# 'ﬁ'
unicodedata.normalize('NFD', s)
# 'ﬁ'

# 합쳐 놓은 문자가 어떻게 분리되는지 살펴보자.
unicodedata.normalize('NFKD', s)
# 'fi'
unicodedata.normalize('NFKC', s)
# 'fi'


# 토론

t1 = unicodedata.normalize('NFD', s1)
''.join(c for c in t1 if not unicodedata.combining(c))
# 'Spicy Jalapeno'
