# 5.15 망가진 파일 이름 출력

def bad_filename(filename):
    return repr(filename)[1:-1]

try:
    print(filename)
except UnicodeEncodeError:
    print(bad_filename(filename))


# 토론

import os
files = os.listdir('.')
files
# ['spam.py', 'b\udce4d.txt', 'foo.txt']


for name in files:
    print(name)

# spam.py
# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
# UnicodeEncodeError: 'utf-8' codec can't encode character '\udce4' in position 1: surrogates not allowed


for name in files:
    try:
        print(name)
    except UnicodeEncodeError:
        print(bad_filename(name))

# spam.py
# b\udce4d.txt
# foo.txt


def bad_filename(filename):
    temp = filename.encode(sys.getfilesystemencoding(), errors='surrogateescape')
    return temp.decode('latin-1')


for name in files:
    try:
        print(name)
    except UnicodeEncodeError:
        print(bad_filename(name))

# spam.py
# bäd.txt
# foo.txt
