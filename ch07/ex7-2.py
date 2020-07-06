# 7.2 키워드 매개변수만 받는 함수 작성

def recv(maxsize, *, block):
    'Receives a message'
    pass

recv(1024, True)       # TypeError
recv(1024, block=True) # Ok


def mininum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

mininum(1, 5, 2, -5, 10)         # -5 반환
mininum(1, 5, 2, -5, 10, clip=0) # 0 반환


# 토론

msg = recv(1024, False)


msg = recv(1024, block=False)


help(recv)
# Help on function recv in module __main__:

# recv(maxsize, *, block)
#     Receives a message

