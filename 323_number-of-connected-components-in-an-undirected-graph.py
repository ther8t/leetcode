class DSU:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]

    def getParent(self, a):
        if self.parent[a] == a:
            return a
        self.parent[a] = self.getParent(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        parent_a, parent_b = self.getParent(a), self.getParent(b)
        self.parent[parent_a] = parent_b

    def size(self):
        return len(set([self.getParent(i) for i in range(self.n)]))


class Solution:
    def countComponents(self, n: int, edges) -> int:
        dsu = DSU(n)
        for a, b in edges:
            dsu.union(a, b)

        return dsu.size()


if __name__ == '__main__':
    print(Solution().countComponents(n = 5, edges = [[0,1],[1,2],[3,4]]))
