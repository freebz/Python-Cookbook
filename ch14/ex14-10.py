# 14.10 마지막 예외 다시 발생

def example():
    try:
        int('N/A')
    except ValueError:
        print("Didn't work")
        raise

example()
# Didn't work
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 3, in example
# ValueError: invalid literal for int() with base 10: 'N/A'



# 토론

try:
    ...
except Exception as e:
    # 예외 정보 처리
    ...

    # 예외 전파
    raise
