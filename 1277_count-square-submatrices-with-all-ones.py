class Solution:
    def countSquares(self, matrix) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        sum = 0
        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                if matrix[row][col] == 1:
                    dp[row][col] = min(dp[row + 1][col], dp[row][col + 1], dp[row + 1][col + 1]) + 1
                    sum += dp[row][col]
        return sum



if __name__ == '__main__':
    print(Solution().countSquares([
  [1,0,1],
  [1,1,0],
  [1,1,0]
]))
