class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = set(), set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in cols:
                    matrix[i][j] = 0

        return matrix


if __name__ == '__main__':
    print(Solution().setZeroes(matrix = [[1,1,1],[1,0,1],[1,1,1]]))
    print(Solution().setZeroes(matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
