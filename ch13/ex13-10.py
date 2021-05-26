# 13.10 환경 설정 파일 읽기

from configparser import ConfigParser
cfg = ConfigParser()
cfg.read('config.ini')
# ['config.ini']
cfg.sections()
# ['installation', 'debug', 'server']
cfg.get('installation','library')
# '/usr/local/lib'
cfg.getboolean('debug','log_errors')
# True
cfg.getint('server','port')
# 8080
cfg.getint('server','nworkers')
# 32
print(cfg.get('server','signature'))
# 
# =================================
# Brought to you by the Python Cookbook
# =================================


cfg.set('server','port','9000')
cfg.set('debug','log_errors','False')
import sys
cfg.write(sys.stdout)
# [installation]
# library = %(prefix)s/lib
# include = %(prefix)s/include
# bin = %(prefix)s/bin
# prefix = /usr/local

# [debug]
# log_errors = False
# show_warnings = False

# [server]
# port = 9000
# nworkers = 32
# pid-file = /tmp/spam.pid
# root = /www/root
# signature = 
# 	=================================
# 	Brought to you by the Python Cookbook
# 	=================================



# 토론

cfg.get('installation','PREFIX')
# '/usr/local'
cfg.get('installation','prefix')
# '/usr/local'


# 기존에 읽은 환경 설정
cfg.get('installation', 'prefix')
# '/usr/local'
# 사용자가 지정한 환경 설정과 합치기
import os
cfg.read(os.path.expanduser('~/.config.ini'))
# ['/Users/beazley/.config.ini']
cfg.get('installation', 'prefix')
# '/Users/beazley/test'
cfg.get('installation', 'library')
# '/Users/beazley/test/lib'
cfg.getboolean('debug', 'log_errors')
# False


cfg.get('installation','library')
# '/Users/beazley/test/lib'
cfg.set('installation','prefix','/tmp/dir')
cfg.get('installation','library')
# '/tmp/dir/lib'
