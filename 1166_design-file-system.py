import collections


"""
Accepted 44%
"""
class FileSystem:
    VALUE = "__value"

    def __init__(self):
        Trie = lambda : collections.defaultdict(Trie)
        self.dir = Trie()
        self.dir[""]

    def createPath(self, path: str, value: int) -> bool:
        path.strip(" /")
        path_split = path.split("/")
        temp = self.dir
        for i in range(len(path_split) - 1):
            if path_split[i] in temp:
                temp = temp[path_split[i]]
            else:
                return False
        if path_split[-1] in temp:
            return False
        temp = temp[path_split[-1]]
        temp[self.VALUE] = value
        return True

    def get(self, path: str) -> int:
        path.strip(" /")
        path_split = path.split("/")
        temp = self.dir
        for i in range(len(path_split)):
            if path_split[i] in temp:
                temp = temp[path_split[i]]
            else:
                return -1
        return temp[self.VALUE]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)


if __name__ == '__main__':
    f = FileSystem()
    print(f.createPath("/leet", 1))
    print(f.createPath("/leet/code", 2))
    print(f.get("/leet/code"))
    print(f.createPath("/c/d", 1))
    print(f.get("/c"))
