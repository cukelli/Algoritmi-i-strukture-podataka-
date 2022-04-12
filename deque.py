class Empty(Exception):
    pass


class Deque:

    def __init__(self, capacity=10):
        self._data = [None]*capacity
        self._first = 0
        self._size = 0
        self._capacity = capacity

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def first(self):
        if self.is_empty():
            raise Empty("Deque je prazan")
        return self._data[self._first]

    def last(self):
        if self.is_empty():
            raise Empty("Deque je prazan")
        last = (self._first + self._size - 1) % self._capacity
        return self._data[last]

    def add_last(self, el):
        if self._size == self._capacity:
            self._resize(2*self._capacity)
        index = (self._first + self._size) % self._capacity
        self._data[index] = el
        self._size += 1

    def add_first(self, el):
        if self._size == self._capacity:
            self._resize(2*self._capacity)
        index = (self._first - 1) % self._capacity
        self._first = (self._first - 1) % self._capacity
        self._data[index] = el
        self._first = index
        self._size += 1

    def remove_first(self):
        el = self._data[self.first]
        self._data[self._first] = None
        self._first = (self._first + 1) % self._capacity

    def remove_last(self):
        if self.is_empty():
            raise Empty("Deque je prazan")
        index = (self._first + self._size - 1) % self._capacity
        el = self._data[index]
        self._data[index] = None
        self._size -= 1

    def enqueue(self, el):
        if self._size == self._capacity:
            self._resize(2*self._capacity)
        last = (self._first + self._size) % self._capacity
        self._data[last] = el
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty("Deque je prazan")
        el = self._data[self._first]
        self._data[self._first] = None
        self._first = (self._first + 1) % self._capacity
        self._size -= 1
        if self._size < self._capacity//4:
            self._resize(self._capacity//2)
        return el

    def _resize(self, cap):
        current_data = self._data
        current_first = self._first
        self._data = [None] * cap
        for i in range(self._size):
            self._data[i] = current_data[current_first]
            current_first = (current_first + 1) % self._capacity
        self._first = 0
        self._capacity = cap


if __name__ == "__main__":
    deque = Deque()

    deque.add_last(5)
    deque.add_first(3)
    print("Kapacitet je:" + str(deque._capacity))
    print(len(deque))
    deque.add_last(7)
    print("Kapacitet je:" + str(deque._capacity))
