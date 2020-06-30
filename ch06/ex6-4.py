# 6.4 매우 큰 XML 파일 증분 파싱하기

from xml.etree.ElementTree import iterparse

def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    # 뿌리 요소 건너뛰기
    next(doc)

    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
                elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass


from xml.etree.ElementTree import parse
from collections import Counter

potholes_by_zip = Counter()
doc = parse('potholes.xml')
for pothole in doc.iterfind('row/row'):
    potholes_by_zip[pothole.findtext('zip')] += 1

for zipcode, num in potholes_by_zip.most_common():
    print(zipcode, num)


from collections import Counter
potholes_by_zip = Counter()

data = parse_and_remove('potholes.xml', 'row/row')
for pothole in data:
    potholes_by_zip[pothole.findtext('zip')] += 1

for zipcode, num in potholes_by_zip.most_common():
    print(zipcode, num)


# 토론

data = iterparse('potholes.xml',('start','end'))
next(data)
# ('start', <Element 'response' at 0x7ff0010f6ae8>)
next(data)
# ('start', <Element 'row' at 0x7ff0010f6d18>)
next(data)
# ('start', <Element 'row' at 0x7ff0010f6e58>)
next(data)
# ('start', <Element 'creation_date' at 0x7ff0010f6e08>)
next(data)
# ('end', <Element 'creation_date' at 0x7ff0010f6e08>)
next(data)
# ('start', <Element 'status' at 0x7ff0010f6db8>)
next(data)
# ('end', <Element 'status' at 0x7ff0010f6db8>)
