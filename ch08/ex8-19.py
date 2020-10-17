# 8.19 상태 객체 혹은 상태 기계 구현

class Connection:
    def __init__(self):
        self.state = 'CLOSED'

    def read(self):
        if self.state != 'OPEN':
            raise RuntimeError('Not open')
        print('reading')

    def write(self, data):
        if self.state != 'OPEN':
            raise RuntimeError('Not open')
        print('writing')

    def open(self):
        if self.state == 'OPEN':
            raise RuntimeError('Already open')
        self.state = 'OPEN'

    def close(self):
        if self.state == 'CLOSED':
            raise RuntimeError('Already closed')
        self.state = 'CLOSED'


class Connection:
    def __init__(self):
        self.new_state(ClosedConnectionState)

    def new_state(self, newstate):
        self._state = newstate

    # 상태 클래스로 델리게이트
    def read(self):
        return self._state.read(self)

    def write(self, data):
        return self._state.write(self, data)

    def open(self):
        return self._state.open(self)

    def close(self):
        return self._state.close(self)

# 연결 상태 베이스 클래스
class ConnectionState:
    @staticmethod
    def read(conn):
        raise NotImplementedError()

    @staticmethod
    def write(conn, data):
        raise NotImplementedError()

    @staticmethod
    def open(conn):
        raise NotImplementedError()

    @staticmethod
    def close(conn):
        raise NotImplementedError()

# 여러 상태 구현
class ClosedConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        raise RuntimeError('Not open')

    @staticmethod
    def write(conn, data):
        raise RuntimeError('Not open')

    @staticmethod
    def open(conn):
        conn.new_state(OpenConnectionState)

    @staticmethod
    def close(conn):
        raise RuntimeError('Already closed')

class OpenConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        print('reading')

    @staticmethod
    def write(conn, data):
        print('writing')

    @staticmethod
    def open(conn):
        raise RuntimeError('Already open')

    @staticmethod
    def close(conn):
        conn.new_state(ClosedConnectionState)


c = Connection()
c._state
# <class '__main__.ClosedConnectionState'>
c.read()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "example.py", line 10, in read
#     return self._state.read(self)
#   File "example.py", line 43, in read
#     raise RuntimeError('Not open')
# RuntimeError: Not open
c.open()
c._state
# <class '__main__.OpenConnectionState'>
c.read()
# reading
c.write('hello')
# writing
c.close()
c._state
# <class '__main__.ClosedConnectionState'>



# 토론

class Connection:
    def __init__(self):
        self.new_state(ClosedConnection)

    def new_state(self, newstate):
        self.__class__ = newstate

    def read(self):
        raise NotImplementedError()

    def write(self, data):
        raise NotImplementedError()

    def open(self):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()

class ClosedConnection(Connection):
    def read(self):
        raise RuntimeError('Not open')

    def write(self, data):
        raise RuntimeError('Not open')

    def open(self):
        self.new_state(OpenConnection)

    def close(self):
        raise RuntimeError('Already closed')

class OpenConnection(Connection):
    def read(self):
        print('reading')

    def write(self, data):
        print('writing')

    def open(self):
        raise RuntimeError('Already open')

    def close(self):
        self.new_state(ClosedConnection)


c = Connection()
c
# <__main__.ClosedConnection object at 0x7f2b28c56a90>
c.read()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "state.py", line 15, in read
# RuntimeError: Not open
c.open()
c
# <__main__.OpenConnection object at 0x7f2b28c56a90>
c.read()
# reading
c.close()
c
# <__main__.ClosedConnection object at 0x7f2b28c56a90>


# 원본
class State:
    def __init__(self):
        self.state = 'A'
    def action(self, x):
        if state == 'A':
            # A 동작
            ...
            state = 'B'
        elif state == 'B':
            # B 동작
            ...
            state = 'C'
        elif state == 'C':
            # C 동작
            ...
            state = 'A'

# 대안
class State:
    def __init__(self):
        self.new_state(State_A)

    def new_state(self, state):
        self.__class__ = state

    def action(self, x):
        raise NotImplementedError()

class State_A(State):
    def action(self, x):
        # A 동작
        ...
        self.new_state(State_B)

class State_B(State):
    def action(self, x):
        # B 동작
        ...
        self.new_state(State_C)

class State_C(State):
    def action(self, x):
        # C 동작
        ...
        self.new_state(State_A)
