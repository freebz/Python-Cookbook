# 2.8 여러 줄에 걸친 정규 표현식 사용

comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
              multiline comment */
'''

comment.findall(text1)
# [' this is a comment ']
comment.findall(text2)
# []


comment = re.compile(r'/\*((?:.|\n)*?)\*/')
comment.findall(text2)
# [' this is a\n              multiline comment ']


# 토론

comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
comment.findall(text2)
# [' this is a\n              multiline comment ']
