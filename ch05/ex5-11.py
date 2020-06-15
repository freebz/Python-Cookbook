# 5.11 경로 다루기

import os
path = '/Users/beazley/Data/data.csv'

# 경로의 마지막 부분 구하기
os.path.basename(path)
# 'data.csv'

# 디렉터리 이름 구하기
os.path.dirname(path)
# '/Users/beazley/Data'

# 각 부분을 합치기
os.path.join('tmp', 'data', os.path.basename(path))
# 'tmp/data/data.csv'

# 사용자의 홈 디렉터리 펼치기
path = '~/Data/data.csv'
os.path.expanduser(path)
# '/Users/beazley/Data/data.csv'

# 파일 확장자 나누기
os.path.splitext(path)
# ('~/Data/data', '.csv')
