# 2.12 텍스트 정리

s = 'pýtĥöñ\fis\tawesome\r\n'
s
# 'pýtĥöñ\x0cis\tawesome\r\n'


remap = {
    ord('\t') : ' ',
    ord('\f') : ' ',
    ord('\r') : None        # 삭제됨
}
a = s.translate(remap)
a
# 'pýtĥöñ is awesome\n'


import unicodedata
import sys
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                         if unicodedata.combining(chr(c)))

b = unicodedata.normalize('NFD', a)
b
# 'pýtĥöñ is awesome\n'
b.translate(cmb_chrs)
# 'python is awesome\n'


digitmap = { c: ord('0') + unicodedata.digit(chr(c))
             for c in range(sys.maxunicode)
             if unicodedata.category(chr(c)) == 'Nd' }

len(digitmap)
# 460
# 아라비아 숫자
x = '\u0661\u0662\u0663'
x.translate(digitmap)
# '123'


a
# 'pýtĥöñ is awesome\n'
b = unicodedata.normalize('NFD', a)
b.encode('ascii',  'ignore').decode('ascii')
# 'python is awesome\n'


# 토론

def clean_spaces(s):
    s = s.replace('\r', '')
    s = s.replace('\t', ' ')
    s = s.replace('\f', ' ')
    return s
