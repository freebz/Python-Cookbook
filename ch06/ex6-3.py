# 6.3 단순한 XML 데이터 파싱

from urllib.request import urlopen
from xml.etree.ElementTree import parse

# RSS 피드를 다운로드하고 파싱한다.
u = urlopen('http://planet.python.org/rss20.xml')
doc = parse(u)

# 관심 있는 태그를 뽑아서 출력한다.
for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')

    print(title)
    print(date)
    print(link)
    print()


# 토론

doc
# <xml.etree.ElementTree.ElementTree object at 0x7ff00183bb00>
e = doc.find('channel/title')
e
# <Element 'title' at 0x7ff0017f6d18>
e.tag
# 'title'
e.text
# 'Planet Python'
e.get('some_attribute')
