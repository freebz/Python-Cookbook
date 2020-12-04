# 10.7 디렉터리나 Zip 파일을 실행 가능하게 만들기

myapplication/
    spam.py
    bar.py
    grok.py
    __main__.py


bash % python3 myapplication


bash % ls
spam.py    bar.py   grok.py   _main__.py
bash % zip -r myapp.zip *.py
bash % python3 myapp.zip
... output from __main__.py ...



# 토론

#!/usr/bin/env python3 /usr/local/bin/myapp.zip
