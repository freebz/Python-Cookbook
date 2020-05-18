# 2.6 대소문자를 구별하지 않는 검색과 치환

text = 'UPPER PYTHON, lower python, Mixed Python'
re.findall('python', text, flags=re.IGNORECASE)
# ['PYTHON', 'python', 'Python']
re.sub('python', 'snake', text, flags=re.IGNORECASE)
# 'UPPER snake, lower snake, Mixed snake'


def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace


re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
# 'UPPER SNAKE, lower snake, Mixed Snake'
