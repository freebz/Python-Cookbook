# 10.8 패키지의 데이터 파일 읽기

mypackage/
    __init__.py
    somedata.dat
    spam.py


# spam.py

import pkgutil
data = pkgutil.get_data(__package__, 'somedata.dat')
