# 7.1 매개변수 개수에 구애 받지 않는 함수 작성

def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))

# 샘플
avg(1, 2)          # 1.5
avg(1, 2, 3, 4)    # 2.5


import html

def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value))
    return element

# 예제
# '<item size="large" quantity="6">Albatross</item>' 생성
make_element('item', 'Albatross', size='large', quantity=6)

# '<p>&lt;spam&gt;</p>' 생성
make_element('p', '<spam>')


def anyargs(*args, **kwargs):
    print(args)      # 튜플
    print(kwargs)    # 딕셔너리


# 토론

def a(x, *args, y):
    pass

def b(x, *args, y, **kwargs):
    pass
