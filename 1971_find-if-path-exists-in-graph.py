import collections

class DSU:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]

    def getParent(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.getParent(self.parent[self.parent[x]])
        return self.parent[x]

    def union(self, a, b):
        parent_a, parent_b = self.getParent(a), self.getParent(b)
        self.parent[parent_a] = parent_b

        return parent_b


class Solution:
    def validPath(self, n: int, edges, source: int, destination: int) -> bool:
        neighbours = collections.defaultdict(list)
        for s, d in edges:
            neighbours[s].append(d)
            neighbours[d].append(s)

        visited = set()

        def dfs(node):
            if node == destination:
                return True

            for n in neighbours[node]:
                if n not in visited:
                    visited.add(n)
                    if dfs(n):
                        return True
            return False

        return dfs(source)

    def validPath(self, n: int, edges, source: int, destination: int) -> bool:
        d = DSU(n)
        for src, des in edges:
            d.union(src, des)
            if d.getParent(source) == d.getParent(destination):
                return True

        return d.getParent(source) == d.getParent(destination)



if __name__ == '__main__':
    # print(Solution().validPath(n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2))
    # print(Solution().validPath(n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5))
    print(Solution().validPath(n = 1, edges = [], source = 0, destination = 0))
