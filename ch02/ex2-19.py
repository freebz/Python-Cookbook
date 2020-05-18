# 2.19 간단한 재귀 파서 작성

'''
expr :: = expr + term
     |    expr - term
     |    term

term ::= term * factor
     |   term / factor
     |   factor

factor ::= ( expr )
       |   NUM
'''


'''
expr ::= term { (+|-) term }*

term ::= factor { (*|/) factor }*

factor ::= ( expr )
       |   NUM
'''


# NUM + NUM * NUM


'''
expr
expr ::= term { (+|-) term }*
expr ::= factor { (*|/) factor }* { (+|-) term }*
expr ::= NUM { (*|/) factor }* { (+|-) term }*
expr ::= NUM { (+|-) TERM }*
expr ::= NUM + term { (+|-) term }*
expr ::= NUM + factor { (*|/) factor }* { (+|-) term }*
expr ::= NUM + NUM { (*|/) factor }* { (+|-) term }*
expr ::= NUM + NUM * factor { (*|/) factor }* { (+|-) term }*
expr ::= NUM + NUM * NUM { (*|/) factor }* { (+|-) term }*
expr ::= NUM + NUM * NUM { (+|-) term }*
expr ::= NUM + NUM * NUM
'''


import re
import collections

# 토큰 스펙화
NUM    = r'(?P<NUM>\d+)'
PLUS   = r'(?P<PLUS>\+)'
MINUS  = r'(?P<MINUS>-)'
TIMES  = r'(?P<TIMES>\*)'
DIVIDE = r'(?P<DIVIDE>/)'
LPAREN = r'(?P<LPAREN>\()'
RPAREN = r'(?P<RPAREN>\))'
WS     = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NUM, PLUS, MINUS, TIMES,
                                  DIVIDE, LPAREN, RPAREN, WS]))

# 토큰화
Token = collections.namedtuple('Token', ['type', 'value'])

def generate_tokens(text):
    scanner = master_pat.scanner(text)
    for m in iter(scanner.match, None):
        tok = Token(m.lastgroup, m.group())
        if tok.type != 'WS':
            yield tok

# 파서
class ExpressionEvaluator:
    '''
    재귀 파서 구현, 모든 메소드는 하나의 문법 규칙을 구현한다.
    현재 룩어헤드 토큰을 받고 테스트하는 용도로 ._accept()를 사용한다.
    입력 받은 내역에 완벽히 매칭하고 다음 토큰을 무시할 때는
    ._expect()를 사용한다(혹시 매칭하지 않는 경우에는 SyntaxError를
    발생한다).
    '''

    def parse(self, text):
        self.tokens = generate_tokens(text)
        self.tok = None             # 마지막 심볼 소비
        self.nexttok = None         # 다음 심볼 토큰화
        self._advance()             # 처음 룩어헤드 토큰 불러오기
        return self.expr()

    def _advance(self):
        'Advance one token ahead'
        self.tok, self.nexttok = self.nexttok, next(self.tokens, None)

    def _accept(self, toktype):
        'Test and consume the next token if it matches toktype'
        if self.nexttok and self.nexttok.type == toktype:
            self._advance()
            return True
        else:
            return False

    def _expect(self, toktype):
        'Consume next token if it matches toktype or raise SyntaxError'
        if not self._accept(toktype):
            raise SyntaxError('Expected ' + toktype)

    # 문법 규칙

    def expr(self):
        "expression ::= term { ('+'|'-') term }*"

        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                exprval += right
            elif op == 'MINUS':
                exprval -= right
        return exprval

    def term(self):
        "term ::= factor { ('*'|'/') factor }*"

        termval = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self.factor()
            if op == 'TIMES':
                termval *= right
            elif op == 'DIVIDE':
                termval /= right
        return termval

    def factor(self):
        "factor ::= NUM | ( expr )"

        if self._accept('NUM'):
            return int(self.tok.value)
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._expect('RPAREN')
            return exprval
        else:
            raise SyntaxError('Expected Number or LPAREN')



e = ExpressionEvaluator()
e.parse('2')
# 2
e.parse('2 + 3')
# 5
e.parse('2 + 3 * 4')
# 14
e.parse('2 + (3 + 4) * 5')
# 37
e.parse('2 + (3 + * 4)')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "exprparse.py", line 40, in parse
#     return self.expr()
#   File "exprparse.py", line 67, in expr
#     right = self.term()
#   File "exprparse.py", line 77, in term
#     termval = self.factor()
#   File "exprparse.py", line 93, in factor
#     exprval = self.expr()
#   File "exprparse.py", line 67, in expr
#     right = self.term()
#   File "exprparse.py", line 77, in term
#     termval = self.factor()
#   File "exprparse.py", line 97, in factor
#     raise SyntaxError('Expected Number or LPAREN')
# SyntaxError: Expected Number or LPAREN


class ExpressionTreeBuilder(ExpressionEvaluator):
    def expr(self):
        "expression ::= term { ('+'|'-') term }"

        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                exprval = ('+', exprval, right)
            elif op == 'MINUS':
                exprval = ('-', exprval, right)
        return exprval

    def term(self):
        "term ::= factor { ('*'|'/') factor }"

        termval = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self.factor()
            if op == 'TIMES':
                termval = ('*', termval, right)
            elif op == 'DIVIDE':
                termval = ('/', termval, right)
        return termval

    def factor(self):
        'factor ::= NUM | (expr)'

        if self._accept('NUM'):
            return int(self.tok.value)
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._expect('RPAREN')
            return exprval
        else:
            raise SyntaxError('Expected NUMBER or LPAREN')


e = ExpressionTreeBuilder()
e.parse('2 + 3')
# ('+', 2, 3)
e.parse('2 + 3 * 4')
# ('+', 2, ('*', 3, 4))
e.parse('2 + (3 + 4) * 5')
# ('+', 2, ('*', ('+', 3, 4), 5))
e.parse('2 + 3 + 4')
# ('+', ('+', 2, 3), 4)


# 토론

'''
expr ::= term { ('+'|'-') term }*

term ::= factor { ('*'|'/') factor }*

factor ::= '(' expr ')'
       :   NUM
'''


class ExpressionEvaluator:
    ...
    def expr(self):
        ...

    def term(self):
        ...

    def factor(self):
        ...


def items(self):
    itemsval = self.items()
    if itemsval and self._accept(','):
        itemsval.append(self.item())
    else:
        itemsval = [ self.item() ]


'''
expr ::= factor { ('+'|'-'|'*'|'/') factor }*

factor ::= '(' expression ')'
       :   NUM
'''


from ply.lex import lex
from ply.yacc import yacc

# 토큰 리스트
tokens = [ 'NUM', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN' ]

# 무시 문자

t_ignore = ' \t\n'

# 토큰 스펙(정규 표현식으로)
t_PLUS   = r'\+'
t_MINUS  = r'\-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# 토큰화 함수
def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

# 에러 핸들러
def t_error(t):
    print('Bad character: {!r}'.format(t.value[0]))
    t.skip(1)

# 렉서(lexer) 만들기
lexer = lex()

# 문법 규칙과 핸들러 함수
def p_expr(p):
    '''
    expr : expr PLUS term
         | expr MINUS term
    '''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]

def p_expr_term(p):
    '''
    expr : term
    '''
    p[0] = p [1]

def p_term(p):
    '''
    term : term TIMES factor
         | term DIVIDE factor
    '''
    if p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

def p_term_factor(p):
    '''
    term : factor
    '''
    p[0] = p[1]

def p_factor(p):
    '''
    factor : NUM
    '''
    p[0] = p[1]

def p_factor_group(p):
    '''
    factor : LPAREN expr RPAREN
    '''
    p[0] = p[2]

def p_error(p):
    print('Syntax error')

parser = yacc()


parser.parse('2')
# 2
parser.parse('2+3')
# 5
parser.parse('2+(3+4)*5')
# 37
