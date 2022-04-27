
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


class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.parent = None  # roditelj
        self.children = []  # lista potomaka,prvo je prazna,ne znamo da li je list ili nije

    def is_root(self):  # koren,nema roditelja
        return self.parent is None

    def is_leaf(self):  # list,nema decu
        return len(self.children) == 0

    def __str__(self):
        return str(self.data)

    def add_child(self, x):
        self.children.append(x)
        x.parent = self


class Tree(object):

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def depth(self, x):
        if x.is_root():
            return 0
        else:
            1 + self.depth(x.parent)

    def _height(self, x):
        if x.is_leaf():
            return 0
        return 1 + max(self._height(ch) for ch in x.children)

    def height(self):
        return self._height(self.root)

    def preorder(self, x, func):
        if not self.is_empty():
            func(x.data)
            for ch in x.children:
                self.preorder(ch, func)

    def postorder(self, x):
        if not self.is_empty():
            for ch in x.children:
                self.postorder(ch)
            print(x)

    def breath_first(self):
        q = ArrayQueue()
        q.enqueue(self.root)
        while not q.is_empty():
            el = q.dequeue()
            print(el)
            for ch in el.children:
                q.enqueue(ch)  # ispis 1 2 3 4 5


if __name__ == "__main__":
    t = Tree()
    t.root = TreeNode(0)

    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)

    t.root.add_child(a)
    t.root.add_child(b)
    a.add_child(c)
    a.add_child(d)
    c.add_child(e)

    print("Dubina cvora: " + str(t.depth(t.root)))
    print("Visina stabla: " + str(t.height()))

    #t.preorder(t.root, print)
    t.postorder(t.root)
