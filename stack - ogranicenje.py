
class StackError(Exception):
    pass


class LimitedStack(Exception):
    pass


class Stack(object):
    capacity = 5

    def _init_(self):
        self._data = []

    def _len_(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, element):
        if len(self._data) == Stack.capacity:
            raise LimitedStack('Stek je pun')
        self._data.append(element)

    def top(self):
        if self.is_empty():
            raise StackError('Stack error')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise StackError('Stack error')
        return self._data.pop()


if __name__ == '_main_':
    s = Stack()
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.top())
    print(len(s))

    s.pop()
    print(s.is_empty())
