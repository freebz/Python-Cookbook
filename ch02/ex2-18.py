# 2.18 텍스트 토큰화

text = 'foo = 23 + 42 * 10'


tokens = [('NAME', 'foo'), ('EQ', '='), ('NUM', '23'), ('PLUS', '+'),
          ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]


import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM  = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ    = r'(?P<EQ>=)'
WS    = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))


scanner = master_pat.scanner('foo = 42')
scanner.match()
# <_sre.SRE_Match object; span=(0, 3), match='foo'>
_.lastgroup, _.group()
# ('NAME', 'foo')
scanner.match()
# <_sre.SRE_Match object; span=(3, 4), match=' '>
_.lastgroup, _.group()
# ('WS', ' ')
scanner.match()
# <_sre.SRE_Match object; span=(4, 5), match='='>
_.lastgroup, _.group()
# ('EQ', '=')
scanner.match()
# <_sre.SRE_Match object; span=(5, 6), match=' '>
_.lastgroup, _.group()
# ('WS', ' ')
scanner.match()
# <_sre.SRE_Match object; span=(6, 8), match='42'>
_.lastgroup, _.group()
# ('NUM', '42')
scanner.match()
#


from collections import namedtuple

Token = namedtuple('Token', ['type','value'])

def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())

# 사용 예
for tok in generate_tokens(master_pat, 'foo = 42'):
    print(tok)

# 출력 결과물
# Token(type='NAME', value='foo')
# Token(type='WS', value=' ')
# Token(type='EQ', value='=')
# Token(type='WS', value=' ')
# Token(type='NUM', value='42')


tokens = (tok for tok in generate_tokens(master_pat, text)
          if tok.type != 'WS')
for tok in tokens:
    print(tok)


# 토큰

LT = r'(?P<LT><)'
LE = r'(?P<LE><=)'
EQ = r'(?P<EQ>=)'

master_pat = re.compile('|'.join([LE, LT, EQ]))     # 올바름
# master_pat = re.compile('|'.join([LT, LE, EQ]))   # 틀림


PRINT = r'(?P<PRINT>print)'
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'

master_pat = re.compile('|'.join([PRINT, NAME]))

for tok in generate_tokens(master_pat, 'printer'):
    print(tok)

# 출력 :
# Token(type='PRINT', value='print')
# Token(type='NAME', value='er')    
