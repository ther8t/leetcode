import collections
import heapq


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            self.cache.move_to_end(key)
            self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    l = LRUCache(2)
    l.put(1, 1)
    l.put(2, 2)
    print(l.get(1))
    l.put(3, 3)
    print(l.get(2))
    l.put(4, 4)
    print(l.get(1))
    print(l.get(3))
    print(l.get(4))