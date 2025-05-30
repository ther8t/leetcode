import collections

class DSU:
    def __init__(self, length):
        self.representative = [i for i in range(length)]

    def find(self, a):
        if self.representative[a] != a:
            self.representative[a] = self.find(self.representative[a])
        return self.representative[a]

    def combine(self, a, b):
        self.representative[self.find(b)] = self.find(a)


class Solution:
    def removeStones(self, stones) -> int:
        same_row, same_col = collections.defaultdict(list), collections.defaultdict(list)

        for index, (r, c) in enumerate(stones):
            same_row[r].append(index)
            same_col[c].append(index)

        dsu = DSU(len(stones))
        for i, (r, c) in enumerate(stones):
            for index in same_row[r] + same_col[c]:
                dsu.combine(i, index)

        counter = collections.defaultdict(set)
        for i in range(len(stones)):
            counter[dsu.find(i)].add(i)
        ans = 0
        for e in counter:
            ans += len(counter[e]) - 1
        return ans


if __name__ == '__main__':
    print(Solution().removeStones(stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))
    print(Solution().removeStones(stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]))
    print(Solution().removeStones([[3,2],[3,1],[4,4],[1,1],[0,2],[4,0]]))
    print(Solution().removeStones([[4,4],[5,5],[3,1],[1,4],[1,1],[2,3],[0,3],[2,4],[3,5]]))


