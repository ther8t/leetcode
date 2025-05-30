import collections

from sortedcontainers import SortedSet


class LFUCache:
    # def __init__(self, capacity: int):
    #     self.order = SortedSet()
    #     self.key_value_map = {}
    #     self.key_order_map = {}
    #     self.use_count = 0
    #     self.capacity = capacity
    #
    # def get(self, key: int) -> int:
    #     self.use_count += 1
    #     if key not in self.key_value_map:
    #         return -1
    #     old_order = self.key_order_map[key]
    #     del self.key_order_map[key]
    #     self.order.remove(old_order)
    #
    #     order = list(old_order)
    #     order[0] += 1
    #     order[1] = self.use_count
    #     order = tuple(order)
    #     self.key_order_map[key] = order
    #     self.order.add(order)
    #     return self.key_value_map[key]
    #
    # def put(self, key: int, value: int) -> None:
    #     if self.capacity == 0:
    #         return
    #     self.use_count += 1
    #     if len(self.key_value_map) >= self.capacity and key not in self.key_value_map:
    #         to_be_removed_order = self.order.pop(0)
    #         to_be_removed_key = to_be_removed_order[2]
    #         del self.key_value_map[to_be_removed_key]
    #         del self.key_order_map[to_be_removed_key]
    #
    #     order = (0, self.use_count, key)
    #     if key in self.key_value_map:
    #         order = self.key_order_map[key]
    #         self.order.remove(order)
    #
    #     order = list(order)
    #     order[0] += 1
    #     order[1] = self.use_count
    #     order = tuple(order)
    #     self.key_order_map[key] = order
    #     self.order.add(order)
    #     self.key_value_map[key] = value


    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_freq = collections.defaultdict(int)
        self.freq_key = collections.defaultdict(collections.OrderedDict)
        self.min_freq = 1

    def get(self, key: int) -> int:
        if key not in self.key_freq:
            return -1
        freq = self.key_freq[key]
        value = self.freq_key[freq][key]
        del self.freq_key[freq][key]
        self.freq_key[freq + 1][key] = value
        self.freq_key[freq + 1].move_to_end(key)
        self.key_freq[key] += 1
        if self.min_freq == freq and not self.freq_key[freq]:
            self.min_freq += 1
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.key_freq:
            self.get(key)
            self.freq_key[self.key_freq[key]][key] = value
        else:
            if self.key_freq and len(self.key_freq) == self.capacity:
                popped = self.freq_key[self.min_freq].popitem(last=False)
                del self.key_freq[popped[0]]
            if self.capacity > 0:
                self.min_freq = 1
                self.freq_key[1][key] = value
                self.key_freq[key] = 1


if __name__ == '__main__':
    # Your LFUCache object will be instantiated and called as such:
    # obj = LFUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)
    obj = LFUCache(0)
    obj.put(0, 0)
    print(obj.get(0))
    obj.put(2, 2)
    obj.put(3, 3)
    print(obj.get(2))
    print(obj.get(3))
    obj.put(4, 4)
    print(obj.get(1))
    print(obj.get(3))
    print(obj.get(4))
    # obj.put(4, 4)
    # print(obj.get(3))
    # print(obj.get(4))
