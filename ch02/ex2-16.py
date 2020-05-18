# 2.16 덱스트 열의 개수 고정

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."


import textwrap
print(textwrap.fill(s, 70))
# Look into my eyes, look into my eyes, the eyes, the eyes, the eyes,
# not around the eyes, don't look around the eyes, look into my eyes,
# you're under.

print(textwrap.fill(s, 40))
# Look into my eyes, look into my eyes,
# the eyes, the eyes, the eyes, not around
# the eyes, don't look around the eyes,
# look into my eyes, you're under.

print(textwrap.fill(s, 40, initial_indent='    '))
#     Look into my eyes, look into my
# eyes, the eyes, the eyes, the eyes, not
# around the eyes, don't look around the
# eyes, look into my eyes, you're under.

print(textwrap.fill(s, 40, subsequent_indent='    '))
# Look into my eyes, look into my eyes,
#     the eyes, the eyes, the eyes, not
#     around the eyes, don't look around
#     the eyes, look into my eyes, you're
#     under.


# 토론

import os
os.get_terminal_size().columns
# 80
