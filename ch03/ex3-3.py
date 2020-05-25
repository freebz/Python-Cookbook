# 3.3 출력을 위한 숫자 서식화

x = 1234.56789

# 소수점 둘째 자리 정확도
format(x, '0.2f')
# '1234.57'

# 소수점 한 자리 정확도로 문자 10개 기준 오른쪽에서 정렬
format(x, '>10.1f')
# '    1234.6'

# 왼쪽에서 정렬
format(x, '<10.1f')
# '1234.6    '

# 가운데 정렬
format(x, '^10.1f')
# '  1234.6  '

# 천 단위 구분자 넣기
format(x, ',')
# '1,234.56789'
format(x, '0,.1f')
# '1,234.6'


format(x, 'e')
# '1.234568e+03'
format(x, '0.2E')
# '1.23E+03'


'The value is {:0,.2f}'.format(x)
# 'The value is 1,234.57'


# 토론

x
# 1234.56789
format(x, '0.1f')
# '1234.6'
format(-x, '0.1f')
# '-1234.6'


swap_separators = { ord('.'):',', ord(','):'.' }
format(x, ',').translate(swap_separators)
# '1.234,56789'


'%0.2f' % x
# '1234.57'
'%10.1f' % x
# '    1234.6'
'%-10.1f' % x
# '1234.6    '
