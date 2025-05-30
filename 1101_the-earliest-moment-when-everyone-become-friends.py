from unionfind import unionfind


class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)
        if xp == yp:
            """
            Revision 2:
            This is a crucial condition. I forgot this line is second attempt.
            The error this causes is not with union, but with size. It adds the size of itself to itself doubling it.
            """
            return self.size[yp]
        if self.size[xp] > self.size[yp]:
            xp, yp = yp, xp
        self.parent[xp] = yp
        self.size[yp] += self.size[xp]

        return self.size[yp]


# class DSU:
#     def __init__(self, n):
#         self.parent = [i for i in range(n)]
#         self.size = [1 for _ in range(n)]
#
#     def find(self, x):
#         if self.parent[x] != x:
#             self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]
#
#     def union(self, x, y):
#         xp, yp = self.find(x), self.find(y)
#         if xp == yp:
#             return self.size[xp]
#         self.parent[yp] = xp
#         self.size[xp] += self.size[yp]
#         return self.size[xp]


class Solution:
    def earliestAcq(self, logs, n: int) -> int:
        logs.sort()
        dsu = DSU(n)
        for time, x, y in logs:
            if dsu.union(x, y) == n:
                return time
        return -1


    # def earliestAcq(self, logs, n: int) -> int:
    #     logs.sort()
    #     u = unionfind(n)
    #     for time, x, y in logs:
    #         u.unite(x, y)
    #         if len(u.groups()) == 1:
    #             return time
    #     return -1


if __name__ == '__main__':
    print(Solution().earliestAcq([[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], 6))
