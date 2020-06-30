# 6.5 딕셔너리를 XML로 바꾸기

from xml.etree.ElementTree import Element

def dict_to_xml(tag, d):
    '''
    간단한 dict를 XML로 변환하기
    '''
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem


s = { 'name': 'GOOG', 'shares': 100, 'price':490.1 }
e = dict_to_xml('stock', s)
e
# <Element 'stock' at 0x7ff0010c8f98>


from xml.etree.ElementTree import tostring
tostring(e)
# b'<stock><name>GOOG</name><shares>100</shares><price>490.1</price></stock>'


e.set('_id','1234')
tostring(e)
# b'<stock _id="1234"><name>GOOG</name><shares>100</shares><price>490.1</price></stock>'


# 토론

def dict_to_xml_str(tag, d):
    '''
    간단한 dict를 XML로 변환하기
    '''
    parts = ['<{}>'.format(tag)]
    for key, val in d.items():
        parts.append('<{0}>{1}</{0}>'.format(key,val))
    parts.append('</{}>'.format(tag))
    return ''.join(parts)


d = { 'name' : '<spam>' }

# 문자열 생성
dict_to_xml_str('item',d)
# '<item><name><spam></name></item>'

# 올바른 XML 생성
e = dict_to_xml('item',d)
tostring(e)
# b'<item><name>&lt;spam&gt;</name></item>'


from xml.sax.saxutils import escape, unescape
escape('<spam>')
# '&lt;spam&gt;'
unescape(_)
# '<spam>'
