class MapElement(object):
    def __init__(self, k, v):
        self._key = k
        self._value = v

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, new_value):
        self._key = new_value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value


class Map(object):

    def __init__(self):
        self._data = []

    def __getitem__(self, k):
        for item in self._data:
            if k == item.key:
                return item.value
        raise KeyError("Ne postoji prosledjeni kljuc")

    def __setitem__(self, k, v):
        for item in self._data:
            if k == item.key:
                item.value = v
                return

        self._data.append(MapElement(k, v))

    def __delitem__(self, k):  # brisanje
        length = len(self._data)
        for i in range(length):
            if k == self._data[i].key:
                self._data.pop(i)
                return
        raise KeyError("Ne postoji prosledjeni kljuc")

    def len(self):
        return len(self._data)

    def __iter__(self):
        for item in self._data:
            yield item.key

    def __contains__(self, k):
        for key in self:
            if k == key:
                return True
        return False

    def keys(self):
        keys = []
        for key in self:
            keys.append(key)
        return keys

    def values(self):
        values = []
        for key in self:
            values.append(self[key])
        return values

    def items(self):
        for item in self._data:
            yield item.key, item.value

    def clear(self):
        self._data = []


if __name__ == "__main__":
    mapa = Map()
    mapa['a'] = 2
    mapa['b'] = 5
    mapa['abc'] = 22
    print("Iscitaj po kljucu: " + str(mapa['b']))
    print(mapa.items())
    print(mapa.values())
    del mapa['abc']
    print(mapa.values())
