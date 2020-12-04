# 10.9 sys.path에 디렉터리 추가

bash % env PYTHONPATH=/some/dir:/other/dir python3

imporr.sys
sys.path
['', '/some/dir', '/other/dir', ...]


# myapplication.path
/some/dir
/other/dir



# 토론

import sys
sys.path.insert(0, '/some/dir')
sys.path.insert(0, '/other/dir')


import sys
from os.path import abspath, join, dirname
sys.path.insert(0, abspath(dirname('__file__'), 'src'))
