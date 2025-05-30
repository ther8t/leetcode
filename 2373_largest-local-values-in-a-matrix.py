class Solution:
    def largestLocal(self, grid):
        return [[max([max([grid[r][c] for c in range(j - 1, j + 2, 1)]) for r in range(i - 1, i + 2, 1)]) for j in range(1, len(grid[0]) - 1, 1)] for i in range(1, len(grid) - 1, 1)]


if __name__ == '__main__':
    print(Solution().largestLocal(grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]))
