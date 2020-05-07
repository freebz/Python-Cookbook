# 1.14 기본 비교 기능 없이 객체 정렬

class User:
    def __init__(self, user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(23), User(3), User(99)]
users
# [User(23), User(3), User(99)]
sorted(users, key=lambda u: u.user_id)
# [User(3), User(23), User(99)]


from operator import attrgetter
sorted(users, key=attrgetter('user_id'))
# [User(3), User(23), User(99)]


# 토론

by_name = sorted(users, key=attrgetter('last_name', 'first_name'))


min(users, key=attrgetter('user_id'))
# User(3)
max(users, key=attrgetter('user_id'))
# User(99)
