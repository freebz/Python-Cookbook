# 13.4 암호 입력 받기

import getpass

user = getpass.getuser()
passwd = getpass.getpass()

if svc_login(user, passwd):  # svc_login()은 직접 작성한다.
    print('Yay!')
else:
    print('Boo!')



# 토론

user = input('Enter your username: ')
