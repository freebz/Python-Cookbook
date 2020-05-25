# 3.11 임의의 요소 뽑기

import random
values = [1, 2, 3, 4, 5, 6]
random.choice(values)
# 2
random.choice(values)
# 3
random.choice(values)
# 1
random.choice(values)
# 4
random.choice(values)
# 6


random.sample(values, 2)
# [6, 2]
random.sample(values, 2)
# [4, 3]
random.sample(values, 3)
# [4, 3, 1]
random.sample(values, 3)
# [5, 4, 1]


random.shuffle(values)
values
# [2, 4, 6, 5, 3, 1]
random.shuffle(values)
values
# [3, 5, 2, 1, 6, 4]


random.randint(0,10)
# 2
random.randint(0,10)
# 5
random.randint(0,10)
# 0
random.randint(0,10)
# 7
random.randint(0,10)
# 10
random.randint(0,10)
# 3


random.random()
# 0.9406677561675867
random.random()
# 0.133129581343897
random.random()
# 0.4144991136919316


random.getrandbits(200)
# 335837000776573622800628485064121869519521710558559406913275


# 토론

random.seed()            # 시스템 시간이나 os.urandom() 시드
random.seed(12345)       # 주어진 정수형 시드
random.seed(b'bytedata') # 바이트 데이터 시드
