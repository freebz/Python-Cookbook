# 9.13 인스턴스 생성 조절에 메타클래스 사용

class Spam:
    def __init__(self, name):
        self.name = name

a = Spam('Guido')
b = Spam('Diana')


class NoInstances(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly")

# 예제
class Spam(metaclass=NoInstances):
    @staticmethod
    def grok(x):
        print('Spam.grok')


Spam.grok(42)
# Spam.grok
s = Spam()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "example1.py", line 7, in __call__
#     raise TypeError("Can't instantiate directly")
# TypeError: Can't instantiate directly


class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


# 예제
class Spam(metaclass=Singleton):
    def __init__(self):
        print('Creating Spam')


a = Spam()
# Creating Spam
b = Spam()
a is b
# True
c = Spam()
a is c
# True


import weakref

class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self, *args):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj

# 예제
class Spam(metaclass=Cached):
    def __init__(self, name):
        print('Creating Spam({!r})'.format(name))
        self.name = name


a = Spam('Guido')
# Creating Spam('Guido')
b = Spam('Diana')
# Creating Spam('Diana')
c = Spam('Guido')    # 캐시
a is b
# False
a is c
# True



# 토론

class _Spam:
    def __init__(self):
        print('Creating Spam')

_spam_instance = None
def Spam():
    global _spam_instance
    if _spam_instance is not None:
        return _spam_instance
    else:
        _spam_instance = _Spam()
        return _spam_instance
