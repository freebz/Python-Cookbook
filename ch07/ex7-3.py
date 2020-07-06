# 7.3 함수 인자에 메타데이터 넣기

def add(x:int, y:int) -> int:
    return x + y


help(add)
# Help on function add in module __main__:

# add(x:int, y:int) -> int


# 토론

add.__annotations__
# {'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}
