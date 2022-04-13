from operator import index


class Empty(Exception):
    pass


class MaxCapacity(Exception):
    pass


class ArrayQueue(object):
    capacity = 5

    def _init_(self):
        self._data = [None]
        self._size = 0
        self._front = 0

    def _len_(self):
        return self._size

    def is_empty(self):
        return len(self._data) == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] == None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, element):
        if self._size == ArrayQueue.capacity:
            raise MaxCapacity('Maximum capacity')
        index = (self._front + self._size) % len(self._data)
        self._data[index] = element
        self._size += 1


if __name__ == "_main_":
    q = ArrayQueue()
    q.enqueue(5)
    q.enqueue(3)
    q.enqueue(8)
    print(len(q))
    q.dequeue()
