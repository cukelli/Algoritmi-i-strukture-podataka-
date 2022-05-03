class PQError(Exception):
    pass


class PQItem(object):

    def __init__(self, k, v):
        self._key = k
        self._value = v

    # lower then
    def __lt__(self, x):
        return self._key < x._key

    def __str__(self):
        return "(" + str(self._key) + "," + str(self._value) + ")"


class PQBase(object):

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self) == 0

    def __str__(self):
        return ','.join('(%s,%s)' % (x._key, x._value) for x in self._data)


class SortedPQ(PQBase):

    def __init__(self):
        super().__init__()  # (SortedPQ,self)

    def min(self):
        if self.is_empty():
            raise PQError("Red je prazan")
        min_el = self._data[0]
        return (min_el._key, min_el._value)

    def remove_min(self):
        if self.is_empty():
            raise PQError("Red je prazan")
        min_el = self._data.pop(0)
        return (min_el._key, min_el._value)

    def add(self, k, v):
        new_item = PQItem(k, v)
        last = len(self)-1
        position = 0

        for i in range(last, -1, -1):
            if not new_item < self._data[i]:
                position = i + 1
                break
        self._data.insert(position, new_item)


class Unsorted(PQBase):

    def __init__(self):
        super().__init__()

    def _find_min(self):
        min_el = self._data[0]
        for i in range(len(self)):
            if self._data[i] < min_el:
                min_el = self._data[i]
                index = i
        return min_el

    def min(self):
        return self._find_min()

    def remove_min(self):
        min_el = self._find_min()
        index = self._data.index(min_el)
        el = self._data.pop(index)
        return (el._key, el._value)

    def add(self, k, v):
        new_item = PQItem(k, v)
        self._data.append(new_item)


def pq_sort(A):
    pq = Unsorted()
    size = len(A)
    for i in range(size):
        el = A.pop()
        pq.add(el, el)
    for i in range(size):
        (k, v) = pq.remove_min()
        A.append(k)
    return A


if __name__ == "__main__":
    sqp = SortedPQ()
    sqp.add(3, "abc")
    sqp.add(2, "ab")
    sqp.add(1, "a")
    sqp.add(11, "abcd")
    sqp.add(2, "ad")
    print(sqp)
    print(sqp.min())
    print(sqp.remove_min())
    print(sqp)

    print("---------------")
    uspq = Unsorted()
    uspq.add(3, "abc")
    print(uspq)
    print("-------SORT-------")
    A = [3, 5, 6, 1, 1, 8, 7]
    pq_sort(A)
    print(A)
