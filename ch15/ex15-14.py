# 15.14 C 라이드러리에 Unicode 문자열 전달

s = 'Spicy Jalape\u00f1o'
print_chars(s)
# 53 70 69 63 79 20 4a 61 6c 61 70 65 c3 b1 6f
print_wchars(s)
# 53 70 69 63 79 20 4a 61 6c 61 70 65 f1 6f



# 토론

import sys
s = 'Spicy Jalape\u00f1o'
sys.getsizeof(s)
# 87
print_chars(s)
# 53 70 69 63 79 20 4a 61 6c 61 70 65 c3 b1 6f
sys.getsizeof(s)
# 103
print_wchars(s)
# 53 70 69 63 79 20 4a 61 6c 61 70 65 f1 6f
sys.getsizeof(s)
# 163
