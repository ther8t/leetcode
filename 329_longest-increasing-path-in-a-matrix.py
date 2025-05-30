class Solution:
    """
    Revision 2:
    My first thought on seeing the question : Backtracking + DP.
    It turns out that I was not satisfied with this algo. So I thought why a simple up-left search for greater number not work.
    Then I tried to find a test case where this would be flawed and I did find it.
    There are times when the sequence would be found going downwards. And I say sequence because it is a sequence and direction matters otherwise there would be cases like 3 <- 2 -> 4.
    Not just that there could be winding cases like
    1    4 -> 5    8
    |    |    |    |
    2 -> 3    6 -> 7
    """
    def longestIncreasingPath(self, matrix) -> int:
        rows, cols = len(matrix), len(matrix[0])
        stack = []
        dp = [[-1 for _ in range(cols)] for _ in range(rows)]

        def dfs(matrix, row, col):
            if dp[row][col] != -1:
                return dp[row][col]
            max_length = 0
            tried = False
            if row - 1 >= 0 and matrix[row - 1][col] > matrix[row][col]:
                tried = True
                stack.append(matrix[row - 1][col])
                length = dfs(matrix, row - 1, col)
                max_length = max(max_length, length)
                stack.pop()
            if row + 1 < rows and matrix[row + 1][col] > matrix[row][col]:
                tried = True
                stack.append(matrix[row + 1][col])
                length = dfs(matrix, row + 1, col)
                max_length = max(max_length, length)
                stack.pop()
            if col - 1 >= 0 and matrix[row][col - 1] > matrix[row][col]:
                tried = True
                stack.append(matrix[row][col - 1])
                length = dfs(matrix, row, col - 1)
                max_length = max(max_length, length)
                stack.pop()
            if col + 1 < cols and matrix[row][col + 1] > matrix[row][col]:
                tried = True
                stack.append(matrix[row][col + 1])
                length = dfs(matrix, row, col + 1)
                max_length = max(max_length, length)
                stack.pop()

            if not tried:
                dp[row][col] = 0
                return 0
            else:
                dp[row][col] = max_length + 1
                return max_length + 1

        max_number = -1
        min_number = float('inf')
        numbers = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                numbers.add(matrix[i][j])
                min_number = min(min_number, matrix[i][j])
                max_number = max(max_number, matrix[i][j])

        numbers = sorted(list(numbers))

        max_length = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if max_length == len(numbers):
                    return max_length
                if max_length < (len(numbers) - numbers.index(matrix[i][j])):
                    stack.append(matrix[i][j])
                    length = dfs(matrix, i, j)
                    max_length = max(max_length, length + 1)
                    stack.pop()

        return max_length


    def longestIncreasingPath(self, matrix) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[-1 for _ in range(cols)] for _ in range(rows)]



if __name__ == '__main__':
    print(Solution().longestIncreasingPath(matrix = [[3,4,5],[3,2,6],[2,2,1]]))
