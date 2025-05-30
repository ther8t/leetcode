class Solution:
    def numMagicSquaresInside(self, grid) -> int:
        m, n = len(grid), len(grid[0])

        def check(r, c):
            numbers = set()
            for i in range(r, r + 3):
                s = 0
                for j in range(c, c + 3):
                    if 1 <= grid[i][j] <= 9:
                        numbers.add(grid[i][j])
                        s += grid[i][j]
                    else:
                        return False
                if s != 15:
                    return False

            if len(numbers) != 9:
                return False

            for j in range(c, c + 3):
                s = 0
                for i in range(r, r + 3):
                    s += grid[i][j]
                if s != 15:
                    return False

            s = 0
            for i in range(3):
                s += grid[r + i][c + i]
            if s != 15:
                return False

            s = 0
            for i in range(3):
                s += grid[r + i][c + 2 - i]
            if s != 15:
                return False

            return True

        ans = 0
        for i in range(m - 2):
            for j in range(n - 2):
                ans += 1 if check(i, j) else 0

        return ans


if __name__ == '__main__':
    print(Solution().numMagicSquaresInside(grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]))

