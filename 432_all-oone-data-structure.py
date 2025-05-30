import collections


class AllOne:

    def __init__(self):
        self.string_count_map = collections.defaultdict(int)
        self.count_string_map = collections.defaultdict(set)

    def inc(self, key: str) -> None:
        prev_count = self.string_count_map[key]
        updated_count = prev_count + 1
        self.string_count_map[key] = updated_count
        self.count_string_map[updated_count].add(key)
        if prev_count:
            self.count_string_map[prev_count].remove(key)
        if (self.count_string_map[prev_count]) == 0:
            del self.count_string_map[prev_count]

    def dec(self, key: str) -> None:
        prev_count = self.string_count_map[key]
        updated_count = prev_count - 1
        self.string_count_map[key] = updated_count
        self.count_string_map[prev_count].remove(key)
        if updated_count > 0:
            self.count_string_map[updated_count].add(key)
        if updated_count == 0:
            del self.string_count_map[key]
        if len(self.count_string_map[prev_count]) == 0:
            del self.count_string_map[prev_count]

    def getMaxKey(self) -> str:
        for i in sorted(self.count_string_map.keys(), reverse=True):
            for v in self.count_string_map[i]:
                return v
        return ""

    def getMinKey(self) -> str:
        for i in sorted(self.count_string_map.keys()):
            for v in self.count_string_map[i]:
                return v
        return ""


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

if __name__ == '__main__':
    a = AllOne()
    a.inc("hello")
    a.inc("hello")
    print(a.getMaxKey())
    print(a.getMinKey())
    print("-----------")
    a.dec("hello")
    print(a.getMaxKey())
    print(a.getMinKey())
    print("-----------")
    a.dec("hello")
    print(a.getMaxKey())
    print(a.getMinKey())
    print("-----------")
    a.inc("leet")
    print(a.getMaxKey())
    print(a.getMinKey())
    print("-----------")
    a.inc("hello")
    print(a.getMaxKey())
    print(a.getMinKey())
    print("-----------")
    a.inc("hello")
    print(a.getMaxKey())
    print(a.getMinKey())
    print("-----------")
    a.dec("leet")
    print(a.getMaxKey())
    print(a.getMinKey())
    print("-----------")
