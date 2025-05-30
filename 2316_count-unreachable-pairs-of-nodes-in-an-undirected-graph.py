import collections


class DSU:

    def __init__(self, length):
        self.parent = [i for i in range(length)]
        self.size = [1] * length

    def find(self, a):
        if a != self.parent[a]:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def unite(self, a, b):
        parent_a, parent_b = self.find(a), self.find(b)
        if parent_a == parent_b:
            return
        if self.size[parent_a] < self.size[parent_b]:
            a, b = b, a
            parent_a, parent_b = parent_b, parent_a

        self.parent[parent_b] = parent_a
        self.size[parent_a] += self.size[parent_b]


class Solution:
    def countPairs(self, n: int, edges) -> int:
        dsu = DSU(n)
        for a, b in edges:
            dsu.unite(a, b)

        counter = collections.Counter([dsu.find(i) for i in range(n)])
        count_arr = [counter[i] for i in counter]
        ans = 0
        c_sum = 0
        for i in range(len(count_arr) - 1):
            c_sum += count_arr[i]
            ans += count_arr[i] * (n - c_sum)
        return ans


if __name__ == '__main__':
    print(Solution().countPairs(n = 3, edges = [[0,1],[0,2],[1,2]]))
    print(Solution().countPairs(n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]))
    print(Solution().countPairs(100000, []))
