class EmptyQueue(Exception):
    pass


class ArrayQueue(object):

    def __init__(self):
        DEFAULT_CAPACITY = 10
        self._data = [None] * DEFAULT_CAPACITY  # lista sa fiksnim kapacitetom
        self._size = 0  # broj elemenata u redu
        self._front = 0  # indeks prvog elementa u redu

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise EmptyQueue("Red je prazan")
        return self._data[self._front]

    def dequeue(self):  # uklanja element sa pocetka reda
        if self.is_empty():
            raise EmptyQueue("Red je prazan")
        answer = self._data[self._front]  # indeks prvog elementa - 0
        self._data[self._front] = None  # Uklanja se prvi element,postaje None
        # Novi prvi element ima indeks pomeren za + 1 (0+1) % duzina(10) 1 % 10 = 1
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1  # uklanjas element,smanji duzinu za 1
        return answer  # vrati element koji si uklonila

    def enqueue(self, el):  # dodaje element na kraj reda
        # ako je kapacitet liste popunjen,uvecaj je duplo
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        # saberi 0 sa trenutnom velicinom liste,podeli je sa 10 ili 20 u zavisnosti od toga da li je popunjena
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = el
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1+walk) % len(old)
        self._front = 0

    def __str__(self):
        return str(self._data)


if __name__ == "__main__":
    queue = ArrayQueue()
    queue.enqueue(3)
    queue.enqueue(5)

    print(queue)
    queue.dequeue()
    print(queue)
