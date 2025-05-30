class Solution:
    def matrixScore(self, grid) -> int:
        m, n = len(grid), len(grid[0])

        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] = 1 if grid[i][j] == 0 else 0

        for j in range(1, n):
            ones = 0
            for i in range(m):
                ones += grid[i][j]
            if ones < m - ones:
                for i in range(m):
                    grid[i][j] = 1 if grid[i][j] == 0 else 0

        return sum([sum([(2 ** (n - 1 - j)) * grid[i][j] for j in range(n)]) for i in range(m)])


if __name__ == '__main__':
    print(Solution().matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]))
    print(Solution().matrixScore([[0]]))
