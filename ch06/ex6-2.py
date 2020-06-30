# 6.2 JSON 데이터 읽고 쓰기

import json

data = {
    'name' : 'ACME',
    'shares' : 100,
    'price' : 542.23
}

json_str = json.dumps(data)


data = json.loads(json_str)


# JSON 데이터 쓰기
with open('data.json', 'w') as f:
    json.dump(data, f)

# 데이터 다시 읽기
with open('data.json', 'r') as f:
    data = json.load(f)


# 토론

json.dumps(False)
# 'false'
d = {'a': True,
     'b': 'Hello',
     'c': None}
json.dumps(d)
# '{"a": true, "b": "Hello", "c": null}'


from urllib.request import urlopen
import json
u = urlopen('http://search.twitter.com/search.json?q=python&rpp=5')
resp = json.loads(u.read().decode('utf-8'))
from pprint import pprint
pprint(resp)
{'completed_in': 0.074,
 'max_id': 264043230692245504,
 'max_id_str': '264043230692245504',
 'next_page': '?page=2&max_id=264043230692245504&q=python&rpp=5',
 'page': 1,
 'query': 'python',
 'refresh_url': '?since_id=2640043230692245504&q=python',
 'results': [{'created_at': 'Thu, 01 Nov 2012 16:36:26 +0000',
              'from_user': ...
             },
             {'created_at': 'Thu, 01 Nov 2012 16:36:14 +0000',
              'from_user': ...
             },
             {'created_at': 'Thu, 01 Nov 2012 16:36:13 +0000',
              'from_user': ...
             },
             {'created_at': 'Thu, 01 Nov 2012 16:36:07 +0000',
              'from_user': ...
             },
             {'created_at': 'Thu, 01 Nov 2012 16:36:04 +0000',
              'from_user': ...
             }],
 'results_per_page': 5,
 'since_id': 0,
 'since_id_str': '0'}


s = '{"name": "ACME", "shares": 50, "price": 490.1}'
from collections import OrderedDict
data = json.loads(s, object_pairs_hook=OrderedDict)
data
# OrderedDict([('name', 'ACME'), ('shares', 50), ('price', 490.1)])


class JSONObject:
    def __init__(self, d):
        self.__dict__ = d

data = json.loads(s, object_hook=JSONObject)
data.name
# 'ACME'
data.shares
# 50
data.price
# 490.1


print(json.dumps(data))
# {"name": "ACME", "shares": 100, "price": 542.23}
print(json.dumps(data, indent=4))
# {
#     "name": "ACME",
#     "shares": 100,
#     "price": 542.23
# }


print(json.dumps(data, sort_keys=True))
# {"name": "ACME", "price": 542.23, "shares": 100}


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 3)
json.dumps(p)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/usr/lib/python3.6/json/__init__.py", line 231, in dumps
#     return _default_encoder.encode(obj)
#   File "/usr/lib/python3.6/json/encoder.py", line 199, in encode
#     chunks = self.iterencode(o, _one_shot=True)
#   File "/usr/lib/python3.6/json/encoder.py", line 257, in iterencode
#     return _iterencode(o, 0)
#   File "/usr/lib/python3.6/json/encoder.py", line 180, in default
#     o.__class__.__name__)
# TypeError: Object of type 'Point' is not JSON serializable


def serialize_instance(obj):
    d = { '__classname__' : type(obj).__name__ }
    d.update(vars(obj))
    return d


# 알려지지 않은 클래스에 이름을 매핑하는 딕셔너리
classes = {
    'Point' : Point
}

def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)   # __init__을 호출하지 않고 인스턴스 만들기
        for key, value in d.items():
            setattr(obj, key, value)
            return obj
        else:
            return d


p = Point(2,3)
s = json.dumps(p, default=serialize_instance)
s
# '{"__classname__": "Point", "x": 2, "y": 3}'
a = json.loads(s, object_hook=unserialize_object)
a
# <__main__.Point object at 0x7ff002be2da0>
a.x
# 2
a.y
# 3
