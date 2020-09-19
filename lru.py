from collections import deque
from data import Data

class Lru:

    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.lookup = dict()
        self.queue = deque()

    def insert(self, key, value):
        if(key in self.lookup):
            data = self.lookup[key]
            self.queue.remove(data)
        else:
            if(len(self.queue) == self.capacity):
                last = self.queue.popleft()
                del self.lookup[last.key]
        data = Data(key, value)
        self.queue.append(data)
        self.lookup[key] = data

    def state_of_cache(self):
        return [[i.key, i.value] for i in self.queue]

lru = Lru(5)

lru.insert(1, "A")
print(lru.state_of_cache())
lru.insert(2, "B")
lru.insert(3, "C")
lru.insert(4, "D")
lru.insert(5, "E")
print(lru.state_of_cache())
lru.insert(6, "F")
print(lru.state_of_cache())
lru.insert(7, "G")
print(lru.state_of_cache())
lru.insert(7, "H")
print(lru.state_of_cache())



    