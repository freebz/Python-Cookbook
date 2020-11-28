# 9.24 파이썬 코드 파싱, 분석

x = 42
eval('2 + 3*4 + x')
# 56

exec('for i in range(10): print(i)')
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9


import ast
ex = ast.parse('2 + 3*4 + x', mode='eval')
ex
# <_ast.Expression object at 0x7f0d79b06880>
ast.dump(ex)
# "Expression(body=BinOp(left=BinOp(left=Constant(value=2, kind=None), op=Add(), right=BinOp(left=Constant(value=3, kind=None), op=Mult(), right=Constant(value=4, kind=None))), op=Add(), right=Name(id='x', ctx=Load())))"

top = ast.parse('for i in range(10): print(i)', mode='exec')
top
# <_ast.Module object at 0x7f0d79b06340>
ast.dump(top)
# "Module(body=[For(target=Name(id='i', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Constant(value=10, kind=None)], keywords=[]), body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Name(id='i', ctx=Load())], keywords=[]))], orelse=[], type_comment=None)], type_ignores=[])"


import ast

class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.loaded = set()
        self.stored = set()
        self.deleted = set()
    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.loaded.add(node.id)
        elif isinstance(node.ctx, ast.Store):
            self.stored.add(node.id)
        elif isinstance(node.ctx, ast.Del):
            self.deleted.add(node.id)

# 사용 예제
if __name__ == '__main__':
    # 파이썬 코드
    code = '''
for i in range(10):
    print(i)
del i
'''
    # AST로 파싱
    top = ast.parse(code, mode='exec')

    # 이름 사용을 분석하기 위해 AST 제공
    c = CodeAnalyzer()
    c.visit(top)
    print('Loaded:', c.loaded)
    print('Stored:', c.stored)
    print('Deleted:', c.deleted)


# Loaded: {'i', 'print', 'range'}
# Stored: {'i'}
# Deleted: {'i'}


exec(compile(top,'<stdin>', 'exec'))
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9



# 토론

# namelower.py
import ast
import inspect


# 전역적으로 접근하는 이름을 함수 내부의 지역변수로
# 바꿔 주는 노드 비지터
class NameLower(ast.NodeVisitor):
    def __init__(self, lowered_names):
        self.lowered_names = lowered_names

    def visit_FunctionDef(self, node):
        # 할당을 컴파일해서 상수의 레벨을 낮춘다.
        code = '__globals = globals()\n'
        code += '\n'.join("{0} = __globals['{0}']".format(name)
                          for name in self.lowered_names)

        code_ast = ast.parse(code, mode='exec')

        # 함수 내부에 새로운 구문을 추가
        node.body[:0] = code_ast.body

        # 함수 객체 저장
        self.func = node

# 전역 이름을 지역으로 바꾸는 데코레이터
def lower_names(*namelist):
    def lower(func):
        srclines = inspect.getsource(func).splitlines()
        # @lower_names 데코레이터 이전의 소스 생략
        for n, line in enumerate(srclines):
            if '@lower_names' in line:
                break

        src = '\n'.join(srclines[n+1:])
        # 들여쓴 코드를 처리하기 위한 트릭
        if src.startswith((' ','\t')):
            src = 'if 1:\n' + src
        top = ast.parse(src, mode='exec')

        # AST 변형
        cl = NameLower(namelist)
        cl.visit(top)

        # 수정한 AST 실행
        temp = {}
        exec(compile(top,'','exec'), temp, temp)

        # 수정한 코드 객체 추출
        func.__code__ = temp[func.__name__].__code__
        return func
    return lower


INCR = 1
@lower_names('INCR')
def countdown(n):
    while n > 0:
        n -= INCR


def countdown(n):
    __globals = globals()
    INCR = __globals['INCR']
    while n > 0:
        n -= INCR
