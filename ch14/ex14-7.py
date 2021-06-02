# 14.7 모든 예외 캐치

try:
    ...
except Exception as e:
    ...
    log('Reason:', e)           # 중요!



# 토론

def parse_int(s):
    try:
        n = int(v)
    except Exception:
        print("Couldn't parse")


parse_int('n/a')
# Couldn't parse
parse_int('42')
# Couldn't parse


def parse_int(s):
    try:
        n = int(v)
    except Exception as e:
        print("Couldn't parse")
        print('Reason:', e)


parse_int('42')
# Couldn't parse
# Reason: name 'v' is not defined
