# 15.16 알 수 없는 인코딩의 C 문자열 다루기

s = retstr()
s
# 'Spicy Jalapeño\udcae'
print_chars(s)
# 53 70 69 63 79 20 4a 61 6c 61 70 65 c3 b1 6f ae



# 토론

raw = b'Spicy Jalape\xc3\xb1o\xae'
raw.decode('utf-8','ignore')
# 'Spicy Jalapeño'
raw.decode('utf-8','replace')
# 'Spicy Jalapeño?'


raw.decode('utf-8','surrogateescape')
# 'Spicy Jalapeño\udcae'


s = raw.decode('utf-8', 'surrogateescape')
print(s)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# UnicodeEncodeError: 'utf-8' codec can't encode character '\udcae' in position 14: surrogates not allowed


s
# 'Spicy Jalapeño\udcae'
s.encode('utf-8','surrogateescape')
# b'Spicy Jalape\xc3\xb1o\xae'
