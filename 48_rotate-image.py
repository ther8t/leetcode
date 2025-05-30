class Solution:
    def rotate(self, matrix) -> None:
        n = len(matrix)

        for i in range(n, n//2, -2):
            for j in range(i-1):
                temp = matrix[(n-i)//2 + i - 1 - j][(n-i)//2]
                print((n-i)//2 + j, (n-i)//2 + i - 1, (n-i)//2, (n-i)//2 + j)
                matrix[(n-i)//2 + j][(n-i)//2 + i - 1] = matrix[(n-i)//2][(n-i)//2 + j]
                print((n-i)//2 + i - 1, (n-i)//2 + i - 1 - j, (n-i)//2 + j, (n-i)//2 + i - 1)
                matrix[(n-i)//2 + i - 1][(n-i)//2 + i - 1 - j] = matrix[(n-i)//2 + j][(n-i)//2 + i - 1]
                print((n-i)//2 + i - 1 - j, (n-i)//2, (n-i)//2 + i - 1, (n-i)//2 + i - 1 - j)
                matrix[(n-i)//2 + i - 1 - j][(n-i)//2] = matrix[(n-i)//2 + i - 1][(n-i)//2 + i - 1 - j]
                print((n - i) // 2, (n - i) // 2 + j, (n-i)//2 + i - 1 - j, (n-i)//2)
                matrix[(n - i) // 2][(n - i) // 2 + j] = temp
                print()
        print(matrix)

    # def rotate(self, matrix) -> None:
    #     """
    #     Do not return anything, modify matrix in-place instead.
    #     """
    #
    #     def swap(row1, col1, row2, col2):
    #         temp = matrix[row1][col1]
    #         matrix[row1][col1] = matrix[row2][col2]
    #         matrix[row2][col2] = temp
    #
    #     n = len(matrix)
    #     # find the transpose
    #     for i in range(n):
    #         for j in range(i, n):
    #             swap(i, j, j, i)
    #
    #     # swap columnwise
    #     for col in range(0, n//2):
    #         for row in range(0, n):
    #             swap(row, col, row, n - 1 - col)
    #     return matrix


if __name__ == '__main__':
    print(Solution().rotate(
        [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]))
