# 13.8 압축 파일 생성과 해제

import shutil
shutil.unpack_archive('Python-3.3.0.tgz')
shutil.make_archive('py33','zip','Python-3.3.0')
# '/Users/beazley/Downloads/py33.zip'


shutil.get_archive_formats()
# [('bztar', "bzip2'ed tar-file"), ('gztar', "gzip'ed tar-file"), ('tar', 'uncompressed tar file'), ('xztar', "xz'ed tar-file"), ('zip', 'ZIP file')]



# 토론
