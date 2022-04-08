class EmptyStack(Exception):
    pass


class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, el):
        self._data.append(el)

    def top(self):
        if self.is_empty():
            raise EmptyStack("Stek je prazan")
        else:
            return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise EmptyStack("Stek je prazan")
        return self._data.pop()

    def __str__(self):
        return str(self._data)


# uparivanje zagrada
def is_matched(expr):
    lefty = '({['
    righty = ')}]'
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()


if __name__ == "__main__":

    expr = '(())'
    print(is_matched(expr))
