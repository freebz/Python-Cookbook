# 13.7 파일과 디렉터리 복사와 이동

import shutil

# src를 dst에 복사(cp src dst)
shutil.copy(src, dst)

# 파일을 복사, 메타데이터는 보존(cp -p src dst)
shutil.copy2(src, dst)

# 디렉터리 트리 복사(cp -R src dst)
shutil.copytree(src, dst)

# src를 dst로 이동(mv src dst)
shutil.move(src, dst)


shutil.copy2(src, dst, follow_syslinks=False)

shutil.copytree(src, dst, symlinks=True)


def ignore_pyc_files(dirname, filenames):
    return [name in filenames if name.endswith('.pyc')]

shutil.copytree(src, dst, ignore=ignore_pyc_files)


shutils.copytree(src, dst, ignore_shutil.ignore_patterns('*~','*.pyc'))



# 토론

filename = '/Users/guido/programs/spam.py'
import os.path
os.path.basename(filename)
# 'spam.py'
os.path.dirname(filename)
# '/Users/guido/programs'
os.path.split(filename)
# ('/Users/guido/programs', 'spam.py')
os.path.join('/new/dir', os.path.basename(filename))
# '/new/dir/spam.py'
os.path.expanduser('~/guido/programs/spam.py')
# '/Users/guido/guido/programs/spam.py'


try:
    shutil.copytree(src, dst)
except shutil.Error as e:
    for src, dst, msg in e.args[0]:
        # src는 소스 이름
        # dst는 목적지 이름
        # msg는 예외의 에러 메시지
        print(dst, src, msg)
