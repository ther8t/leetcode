class Solution:
    def rotateGrid(self, grid, k: int):
        rows, cols = len(grid), len(grid[0])
        ans = [[-1 for _ in range(cols)] for _ in range(rows)]

        def read_rotate():
            a = []
            for row in range(row_limit_lo, row_limit_hi + 1):
                a.append(grid[row][col_limit_lo])
            for col in range(col_limit_lo + 1, col_limit_hi + 1):
                a.append(grid[row_limit_hi][col])
            for row in range(row_limit_hi - 1, row_limit_lo - 1, -1):
                a.append(grid[row][col_limit_hi])
            for col in range(col_limit_hi - 1, col_limit_lo, -1):
                a.append(grid[row_limit_lo][col])
            return a

        def write_rotate(a):
            i = 0
            for row in range(row_limit_lo, row_limit_hi + 1):
                ans[row][col_limit_lo] = a[i]
                i += 1
            for col in range(col_limit_lo + 1, col_limit_hi + 1):
                ans[row_limit_hi][col] = a[i]
                i += 1
            for row in range(row_limit_hi - 1, row_limit_lo - 1, -1):
                ans[row][col_limit_hi] = a[i]
                i += 1
            for col in range(col_limit_hi - 1, col_limit_lo, -1):
                ans[row_limit_lo][col] = a[i]
                i += 1

        row_limit_lo, col_limit_lo, row_limit_hi, col_limit_hi = 0, 0, rows - 1, cols - 1
        for i in range(min(rows, cols) // 2):
            current_rows, current_cols = row_limit_hi - row_limit_lo + 1, col_limit_hi - col_limit_lo + 1
            current_k = k % (2 * (current_rows - 1) + 2 * (current_cols - 1))
            a = read_rotate()
            a = a[-current_k:] + a[:-current_k]
            write_rotate(a)
            row_limit_lo += 1
            col_limit_lo += 1
            row_limit_hi -= 1
            col_limit_hi -= 1

        return ans


if __name__ == '__main__':
    print(Solution().rotateGrid(grid = [[40,10],[30,20]], k = 3))
    print(Solution().rotateGrid(grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2))


