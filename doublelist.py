
class EmptyList(Exception):
    pass

class Node:

    def __init__(self, value, next, previous):
        self._value = value
        self._next = next
        self._previous = previous

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value

    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, next):
        self._next = next
    
    @property
    def previous(self):
        return self._previous
    
    @previous.setter
    def previous(self, previous):
        self._previous = previous
    
    def __str__(self) -> str:
        return str(self._value)

class DoubleList:

    def __init__(self):
        self._size = 0
        self._head = Node(None, None, None)
        self._tail = Node(None, None, self._head)
        self._head.next = self._tail    

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size
    
    def get_first(self):
        if self.is_empty():
            raise EmptyList("lista je prazna")
        return self._head.next
    
    def get_last(self):
        if self.is_empty():
            raise EmptyList
        return self._tail.previous

    def add_first(self, value):
        node = Node(value, None, None)

        if self.is_empty():
            self._tail.previous = node
        else:
            self._head.next.previous = node
        node.next = self._head.next
        node.previous = self._head
        self._head.next = node
        self._size += 1
    
    def add_last(self, value):
        node = Node(value, None, None)
        if self.is_empty():
            self._head.next = node
        else:
            self._tail.previous.next = node
        node.next = self._tail
        node.previous = self._tail.previous
        self._tail.previous = node
        self._size += 1

    def get_at(self, index):
        if not 0 <= index <= self._size - 1:
            raise IndexError("Nedozvoljena pozicija")
        counter = 0
        for node in self:
            if counter == index:
                return node
            counter += 1
        
    def remove_first(self):
        if self.is_empty():
            raise EmptyList("Prazna lista!")
        if self._size == 1:
            self._head.next = self._tail
            self._tail.previous = self._head
        else:
            new_first = self._head.next.next
            self._head.next = new_first
            new_first.previous = self._head
        self._size -= 1
    def remove_last(self):
        if self.is_empty():
            raise EmptyList("Prazna lista")
        if self._size == 1:
            self._head.next = self._tail
            self._tail.previous= self._head
        else:
            new_last = self._tail.previous.previous
            new_last.next = self._tail
            self._tail.previous = new_last
        self._size -=1 

    def __iter__(self):
        current_node = self._head.next
        while current_node != self._tail:
            yield current_node
            current_node = current_node.next

    def insert_after(self, node1, value):
        new_node = Node(value, node1, None)
        new_node.next = node1.next
        node1.next.previous = new_node
        node1.next = new_node
        self._size += 1
        return new_node
    
    def insert_before(self, node1, value):
        new_node = Node(value, node1, None)
        new_node.previous = node1.previous
        node1.previous.next = new_node
        node1.previous = new_node
        self._size += 1
        return new_node
    
    def insert_at(self, index, value):
        new_node = Node(value)
        if not 0 <= index <= self._size:
            raise IndexError("index error")

lista = DoubleList()

lista.add_first('b')
lista.add_first('a')
lista.add_last('c')
lista.remove_first()
for node in lista:
    print(node)

# print(lista.get_first())
# print(lista.get_last())

