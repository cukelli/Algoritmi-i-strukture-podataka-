class EmptyList(Exception):
    pass


class Node(object):

    def __init__(self, value, next=None):

        self._value = value
        self._next = next

    def __gt__(self, node):
        return self._value < node._value

    @property
    def value(self):
        return self._value

    @property
    def next(self):
        return self._next

    @value.setter
    def value(self, value):
        self._value = value

    @next.setter
    def next(self, next):
        self._next = next

    def __str__(self):
        return str(self.value)


class SinglyLinkedList(object):
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def __iter__(self):
        current_node = self._head

        while current_node:
            yield current_node
            current_node = current_node._next

    def get_first(self):

        if self.is_empty():
            raise EmptyList("Lista je prazna")
        return self._head

    def get_last(self):
        if self.is_empty():
            raise EmptyList("Lista je prazna!")
        return self._tail

    def add_first(self, value):
        new_node = Node(value)

        if self.is_empty():
            self._tail = new_node
        else:
            new_node.next = self._head

        self._head = new_node
        self._size += 1

    def add_last(self, value):
        new_node = Node(value)

        if self.is_empty():
            self._head = new_node
        else:
            self._tail.next = new_node
        self._tail = new_node
        self._size += 1

    def remove_first(self):
        if self.is_empty():
            raise EmptyList("Lista je prazna")
        if self._size == 1:
            self._tail = None

        self._head = self._head.next
        self._size -= 1

    def remove_last(self):
        if self.is_empty():
            raise EmptyList("Lista je prazna")
        if self._size == 1:
            self._head = None
        for node in self:
            if node.next == self._tail:
                node.next = None
                self._tail = node
                break
        self._size -= 1

    def get_at(self, index):
        if not 0 <= index <= self._size-1:
            raise IndexError("Nedozvoljena pozicija")
        counter = 0
        current_node = self._head
        while current_node:
            if counter == index:
                return current_node
            current_node = current_node.next
            counter += 1

    def insert_at(self, index, value):
        new_value = Node(value)

        if index == 0:
            self.add_first(value)
            return
        if index == self._size:
            self.add_last(value)
            return
        previous_node = self.get_at(index-1)
        temp = previous_node.next
        previous_node.next = new_value
        new_value.next = temp
        self._size += 1

    def remove_at(self, index):
        if not 0 <= index <= self._size - 1:
            raise IndexError("Nedozvoljena pozicija")
        if index == 0:
            self.remove_first()
            return
        if index == self._size - 1:
            self.remove_last()
            return
        previous_node = self.get_at(index-1)
        after_node = previous_node.next.next
        previous_node.next = after_node
        self._size -= 1


class QueueError(Exception):
    pass


class UnlimitedQueue:

    def __init__(self):
        self._data = SinglyLinkedList()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def first(self):
        if self.is_empty():
            raise EmptyList("Lista je prazna")
        return self._data.get_first()

    def dequeue(self):
        if self.is_empty():
            raise EmptyList("Lista je prazna")
        element = self._data.get_first()
        self._data.remove_first()
        return element

    def enqueue(self, element):
        self._data.add_last(element)


if __name__ == '__main__':
    queue = UnlimitedQueue()
    queue.enqueue(3)
    queue.enqueue(8)
    queue.enqueue(1)
    print(len(queue))
    print(queue.first())

    queue.dequeue()
    print(len(queue))

    print(queue.first())
    print(queue.is_empty())
