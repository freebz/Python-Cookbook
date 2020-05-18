# 2.13 텍스트 정렬

text = 'Hello World'
text.ljust(20)
# 'Hello World         '
text.rjust(20)
# '         Hello World'
text.center(20)
# '    Hello World     '


text.rjust(20,'=')
# '=========Hello World'
text.center(20,'*')
# '****Hello World*****'


format(text, '>20')
# '         Hello World'
format(text, '<20')
# 'Hello World         '
format(text, '^20')
# '    Hello World     '


format(text, '=>20s')
# '=========Hello World'
format(text, '*^20s')
# '****Hello World*****'


'{:>10s} {:>10s}'.format('Hello',  'World')
'     Hello      World'


x = 1.2345
format(x,   '>10')
# '    1.2345'
format(x,   '^10.2f')
# '   1.23   '


# 토론
'%-20s ' % text
# 'Hello World          '
'%20s ' % text
# '         Hello World '
