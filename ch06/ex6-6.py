# 6.6 XML 파싱, 수정, 저장

from xml.etree.ElementTree import parse, Element
doc = parse('pred.xml')
root = doc.getroot()
root
# <Element 'stop' at 0x7ff0010f6cc8>

# 요소 몇 개 제거하기
root.remove(root.find('sri'))
root.remove(root.find('cr'))

# <nm>...</nm> 뒤에 요소 몇 개 삽입하기
root.getchildren().index(root.find('nm'))
# 1
e = Element('spam')
e.text = 'This is a test'
root.insert(2, e)

# 파일에 쓰기
doc.write('newpred.xml', xml_declaration=True)
