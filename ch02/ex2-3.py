# 2.3 쉘 와일드카드 패턴으로 문자열 매칭

from fnmatch import fnmatch, fnmatchcase
fnmatch('foo.txt', '*.txt')
# True
fnmatch('foo.txt', '?oo.txt')
# True
fnmatch('Dat45.csv', 'Dat[0-9]*')
# True
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
[name for name in names if fnmatch(name, 'Dat*.csv')]
# ['Dat1.csv', 'Dat2.csv']


# OS X (Mac)
fnmatch('foo.txt', '*.TXT')
# False

# Windows
fnmatch('foo.txt', '*.TXT')
# True


fnmatchcase('foo.txt', '*.TXT')
# False


addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]


from fnmatch import fnmatchcase
[addr for addr in addresses if fnmatchcase(addr, '* ST')]
# ['5412 N CLARK ST', '1060 W ADDISON ST', '2122 N CLARK ST']
[addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]
# ['5412 N CLARK ST']
