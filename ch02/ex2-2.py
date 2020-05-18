# 2.2 문자열 처음이나 마지막에 텍스트 매칭

filename = 'spam.txt'
filename.endswith('.txt')
# True
filename.startswith('file:')
# False
url = 'http://www.python.org'
url.startswith('http:')
# True


import os
filenames = os.listdir('.')
filenames
# [ 'Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h' ]
[name for name in filenames if name.endswith(('.c', '.h')) ]
# ['foo.c', 'spam.c', 'spam.h']
any(name.endswith('.py') for name in filenames)
# True


from urllib.request import urlopen

def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


choices = ['http:', 'ftp:']
url = 'http://www.python.rg'
url.startswith(choices)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: startswith first arg must be str or a tuple of str, not list
url.startswith(tuple(choices))
# True


# 토론

filename = 'spam.txt'
filename[-4:] == '.txt'
# True
url = 'http://www.python.org'
url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:'
# True


import re
url = 'http://www.python.org'
re.match('http:|https:ftp:', url)
# <_sre.SRE_Match object; span=(0, 5), match='http:'>


if any(name.endswith(('.c', '.h')) for name in listdir(dirname)):
    ...
