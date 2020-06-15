# 5.14 파일 이름 인코딩 우회

sys.getfilesystemencoding()
# 'utf-8'


# 유니코드로 파일 이름을 쓴다.
with open('jalape\xf1o.txt', 'w') as f:
    f.write('Spicy!')

# 6
# 디렉터리 리스트 (디코딩됨)
import os
os.listdir('.')
# ['jalapeño.txt']

# 디렉터리 리스트 (디코딩되지 않음)
os.listdir(b'.')                # 바이트 문자열
# [b'jalapen\xcc\x83o.txt']

# 로우 파일 이름으로 파일 열기
with open(b'jalapen\xcc\x83o.txt') as f:
    print(f.read())

# Spicy!
