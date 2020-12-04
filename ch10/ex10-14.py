# 10.14 새로운 파이썬 환경 생성

bash % pyvenv Spam
bash %


bash % cd Spam
bash % ls
bin                include              lib              pyvenv.cfg
bash %


bash % Spam/bin/python3

from pprint import pprint
import sys
pprint(sys.path)
# ['',
#  '/usr/lib/python38.zip',
#  '/usr/lib/python3.8',
#  '/usr/lib/python3.8/lib-dynload',
#  '/Users/beazley/Spam/lib/python3.8/site-packages']



# 토론

bash % pyvenv --system-site-packages Spam
bash %
