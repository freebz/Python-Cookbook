# 13.15 웹 브라우저 실행

import webbrowser
webbrowser.open('http://www.python.org')
# True


# 새 창에서 페이지 열기
webbrowser.open_new('http://www.python.org')
# True

# 새 탭에서 페이지 열기
webbrowser.open_new_tab('http://www.python.org')
# True


c = webbrowser.get('firefox')
c.open('http://www.python.org')
# True
c.open_new_tab('http://docs.python.org')
# True



# 토론
