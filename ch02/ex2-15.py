# 2.15 문자열에 변수 사용

s = '{name} has {n} messages.'
s.format(name='Guido', n=37)
# 'Guido has 37 messages.'


name = 'Guido'
n = 37
s.format_map(vars())
# 'Guido has 37 messages.'


class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

a = Info('Guido',37)
s.format_map(vars(a))
# 'Guido has 37 messages.'


s.format(name='Guido')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'n'


class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'


del n     # n이 정의되지 않도록 한다.
s.format_map(safesub(vars()))
# 'Guido has {n} messages.'


import sys

def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))


name = 'Guido'
n = 37
print(sub('Hello {name}'))
# Hello Guido
print(sub('You have {n} messages.'))
# 'You have 37 messages.'
print(sub('Your favorite color is {color}'))
# Your favorite color is {color}


# 토론

name = 'Guido'
n = 37
'%(name) has %(n) messages.' % vars()


import string
s = string.Template('$name has $n messages.')
s.substitute(vars())
# 'Guido has 37 messages.'
