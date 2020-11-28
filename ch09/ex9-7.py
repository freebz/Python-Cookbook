# 9.7 데코레이터를 사용해서 함수에서 타입 확인 강제

@typeassert(int, int)
def add(x, y):
    return x + y


add(2, 3)
# 5
add(2, 'hello')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "contract.py", line 33, in wrapper
# TypeError: Argument y must be <class 'int'>


from inspect import signature
from functools import wraps

def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        # 디버그 모드가 아니면 타입 확인을 비활성화한다.
        if not __debug__:
            return func

        # 매개변수 이름을 지원할 타입에 매핑한다.
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            # 지원하는 매개변수만 사용하도록 강제한다.
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                            'Argument {} must be {}'.format(name, bound_types[name])
                        )
            return func(*args, **kwargs)
        return wrapper
    return decorate


@typeassert(int, z=int)
def spam(x, y, z=42):
    print(x, y, z)

spam(1, 2, 3)
# 1 2 3
spam(1, 'hello', 3)
# 1 hello 3
spam(1, 'hello', 'world')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "contract.py", line 33, in wrapper
# TypeError: Argument z must be <class 'int'>



# 토론

...
def decorate(func):
    # 최적화 모드에서는 타입 확인을 하지 않는다.
    if not __debug__:
        return func
    ...


from inspect import signature
def spam(x, y, z=42):
    pass

sig = signature(spam)
print(sig)
# (x, y, z=42)
sig.parameters
# mappingproxy(OrderedDict([('x', <Parameter "x">),
# ('y', <Parameter "y">), ('z', <Parameter "z=42">)]))
sig.parameters['z'].name
# 'z'
sig.parameters['z'].default
# 42
sig.parameters['z'].kind
# <_ParameterKind.POSITIONAL_OR_KEYWORD: 1>


bound_types = sig.bind_partial(int,z=int)
bound_types
# <BoundArguments (x=<class 'int'>, z=<class 'int'>)>
bound_types.arguments
# OrderedDict([('x', <class 'int'>), ('z', <class 'int'>)])


bound_values = sig.bind(1, 2, 3)
bound_values.arguments
# OrderedDict([('x', 1), ('y', 2), ('z', 3)])


for name, value in bound_values.arguments.items():
    if name in bound_types.arguments:
        if not isinstance(value, bound_types.arguments[name]):
            raise TypeError()


@typeassert(int, list)
def bar(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items
bar(2)
# [2]
bar(2,3)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "contract.py", line 33, in wrapper
# TypeError: Argument items must be <class 'list'>
bar(4, [1, 2, 3])
# [1, 2, 3, 4]


@typeassert
def spam(x:int, y, z:int = 42):
    print(x,y,z)
