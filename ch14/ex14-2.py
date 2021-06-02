# 14.2 유닛 테스트에서 객체 패치

from unittest.mock import patch
import example

@patch('example.func')
def test1(x, mock_func):
    example.func(x)       # 패치한 example.func 사용
    mock_func.assert_called_with(x)


with patch('example.func') as mock_func:
    example.func(x)      # 패치한 example.func 사용
    mock_func.assert_called_with(x)


p = patch('example.func')
mock_func = p.start()
example.func(x)
mock_func.assert_called_with(x)
p.stop()


@patch('example.func1')
@patch('example.func2')
@patch('example.func3')
def test1(mock1, mock2, mock3):
    ...

def test2():
    with patch('example.patch1') as mock1, \
         patch('example.patch2') as mock2, \
         patch('example.patch3') as mock3:
    ...



# 토론

x = 42
with patch('__main__.x'):
    print(x)

# <MagicMock name='x' id='139657975923856'>
x
# 42


x
# 42
with patch('__main__.x', 'patched_value'):
    print(x)

# patched_value
x
# 42


from unittest.mock import MagicMock
m = MagicMock(return_value = 10)
m(1, 2, debug=True)
# 10
m.assert_called_with(1, 2, debug=True)
m.assert_called_with(1, 2)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/usr/lib/python3.8/unittest/mock.py", line 913, in assert_called_with
#     raise AssertionError(_error_message()) from cause
# AssertionError: expected call not found.
# Expected: mock(1, 2)
# Actual: mock(1, 2, debug=True)

m.upper.return_value = 'HELLO'
m.upper('hello')
# 'HELLO'
assert m.upper.called

m.split.return_value = ['hello', 'world']
m.split('hello world')
# ['hello', 'world']
m.split.assert_called_with('hello world')

m['blah']
# <MagicMock name='mock.__getitem__()' id='139657952551456'>
m.__getitem__.called
# True
m.__getitem__.assert_called_with('blah')


# example.py
from urllib.request import urlopen
import csv

def dowprices():
    u = urlopen('http://finance.yahoo.com/d/quotes.csv?s=@^DJI&f=sl1')
    lines = (line.decode('utf-8') for line in u)
    rows = (row for row csv.reader(lines) if len(row) == 2)
    prices = { name:float(price) for name, price in rows }
    return prices


import unittest
from unittest.mock import patch
import io
import example

sample_data = io.BytesIO(b'''\
"IBM",91.1\r
"AA",13.25\r
"MSFT",27.72\r
\r
''')

class Tests(unittest.TestCase):
    @patch('example.urlopen', return_value=sample_data)
    def test_dowprices(self, mock_urlopen):
        p = example.dowprices()
        self.assertTrue(mock_urlopen.called)
        self.assertEqual(p,
                         {'IBM': 91.1,
                          'AA': 13.25,
                          'MSFT' : 27.72})

if __name__ == '__main__':
    unittest.main()
