# 14.9 다른 예외에 대한 응답으로 예외 발생

def example():
    try:
        int('N/A')
    except ValueError as e:
        raise RuntimeError('A parsing error occurred') from e

example()
# Traceback (most recent call last):
#   File "<stdin>", line 3, in example
# ValueError: invalid literal for int() with base 10: 'N/A'

# The above exception was the direct cause of the following exception:

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 5, in example
# RuntimeError: A parsing error occurred


try:
    example()
except RuntimeError as e:
    print("It didn't work:", e)
    if e.__cause__:
        print('Cause:', e.__cause__)


def example2():
    try:
        int('N/A')
    except ValueError as e:
        print("Couldn't parse:", err)

example2()
# Traceback (most recent call last):
#   File "<stdin>", line 3, in example2
# ValueError: invalid literal for int() with base 10: 'N/A'

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 5, in example2
# NameError: name 'err' is not defined


def example3():
    try:
        int('N/A')
    except ValueError:
        raise RuntimeError('A parsing error occurred') from None

example3()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 5, in example3
# RuntimeError: A parsing error occurred



# 토론

try:
    ...
except SomeException as e:
    raise DifferentException() from e


try:
    ...
except SomeException:
    raise DifferentException()
