# 10.1 모듈의 계층적 패키지 만들기

graphics/
    __init__.py
    primitive/
        __init__.py
        line.py
        fill.py
        text.py
    formats/
        __init__.py
        png.py
        jpg.py


import graphics.primitive.line
from graphics.primitive import line
import graphics.formats.jpg as jpg



# 토론

# graphics/format/__init__.py

from . import jpg
from . import png
