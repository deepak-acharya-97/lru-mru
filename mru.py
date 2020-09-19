from collections import deque
from data import Data

class Mru:
    
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
                last = self.queue.pop()
                del self.lookup[last.key]
        data = Data(key, value)
        self.queue.append(data)
        self.lookup[key] = data
        print(self.state_of_cache())

    def state_of_cache(self):
        return [[i.key, i.value] for i in self.queue]

mru = Mru()
#A B C D E F C G B
mru.insert("A", 1)
mru.insert("B", 1)
mru.insert("C", 1)
mru.insert("D", 1)
mru.insert("E", 1)
mru.insert("F", 1)
mru.insert("C", 1)
mru.insert("G", 1)
mru.insert("B", 1)