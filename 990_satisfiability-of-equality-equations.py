import collections


class DSU:

    def __init__(self):
        self.parent = [i for i in range(26)]

    def union(self, a, b):
        parent_a = self.getParent(a)
        parent_b = self.getParent(b)

        self.parent[parent_a] = parent_b

    def getParent(self, a):
        if self.parent[a] == a:
            return a
        self.parent[a] = self.getParent(self.parent[a])
        return self.parent[a]

    def getMembers(self, a):
        parent_a = self.getParent(a)
        a_mem = []
        for i in range(26):
            if self.getParent(i) == parent_a:
                a_mem.append(i)
        return a_mem


class Solution:
    def equationsPossible(self, equations) -> bool:
        dsu = DSU()
        not_equal_map = collections.defaultdict(list)

        for s in equations:
            first, equals, second = s[0], s[1:3] == "==", s[3]
            first_index, second_index = ord(first) - ord('a'), ord(second) - ord('a')
            if equals:
                for neighbour in dsu.getMembers(first_index) + [first_index]:
                    if second_index in not_equal_map[neighbour]:
                        return False
                for neighbour in dsu.getMembers(second_index) + [second_index]:
                    if first_index in not_equal_map[neighbour]:
                        return False
                dsu.union(first_index, second_index)
            else:
                if dsu.getParent(first_index) == dsu.getParent(second_index):
                    return False
                not_equal_map[first_index].append(second_index)
                not_equal_map[second_index].append(first_index)

        return True


if __name__ == '__main__':
    # print(Solution().equationsPossible(["a==b","b!=a"]))
    # print(Solution().equationsPossible(["b==a","a==b"]))
    # print(Solution().equationsPossible(["a==b","b!=c","c==a"]))
    # print(Solution().equationsPossible(["a==b","b!=c","d==a", "d==c"]))
    print(Solution().equationsPossible(["a==b","b==c","d==e","e==f","d==a","f!=a"]))
