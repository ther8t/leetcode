import heapq


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
    def maximumMinimumPath(self, grid) -> int:
        rows, cols = len(grid), len(grid[0])
        dsu = DSU(rows * cols)
        queue = []

        def translate_coordinates(r, c):
            return r * cols + c

        for r in range(rows):
            for c in range(cols):
                for nr, nc in [(r - 1, c), (r, c - 1)]:
                    if 0 <= nr < rows and 0 <= nc < cols:
                        heapq.heappush(queue, (-min(grid[r][c], grid[nr][nc]), translate_coordinates(r, c), translate_coordinates(nr, nc)))

        while queue:
            score, c1, c2 = heapq.heappop(queue)
            dsu.combine(c1, c2)
            if dsu.find(0) == dsu.find(rows * cols - 1):
                return -score

        return -1


if __name__ == '__main__':
    print(Solution().maximumMinimumPath(grid = [[5,4,5],[1,2,6],[7,4,6]]))
    print(Solution().maximumMinimumPath(grid = [[2,2,1,2,2,2],[1,2,2,2,1,2]]))
    print(Solution().maximumMinimumPath(grid = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]))


