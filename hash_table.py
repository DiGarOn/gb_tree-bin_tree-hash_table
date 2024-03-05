# @brief самая простая реализация хеш-таблицы с использованием свободной аддресации для решения коллизий
class HashTable:
    def __init__(self, _list):
        self.factor = 870977
        self.table = [None]*self.factor
        self.collision_count = 0

        for i in _list:
            self.add_elem(i.author, i)

    def add_elem(self, key, value):
        i = 0
        if self.table[hash(key) % self.factor + i] != None:
            self.collision_count += 1
        while self.table[hash(key) % self.factor + i] != None:
            i += 1
        self.table[hash(key) % self.factor + i] = value

    def get(self, key):
        i = 0
        while self.table[hash(key) % self.factor + i].author != key:
            i += 1
        return self.table[hash(key) % self.factor + i]

    def remove(self, key):
        i = 0
        while self.table[hash(key) % self.factor + i].author != key:
            i += 1
        self.table[hash(key) % self.factor + i] = None

