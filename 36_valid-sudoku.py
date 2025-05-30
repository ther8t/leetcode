class Solution:
    def isValidSudoku(self, board):
        # check row
        for i in range(9):
            isRowValid = self.isValidRow(board, i)
            if not isRowValid: return False

        # check column
        for i in range(9):
            isColValid = self.isValidColumn(board, i)
            if not isColValid: return False

        # check box
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                isBoxValid = self.isValidBox(board, i, j)
                if not isBoxValid: return False
        return True

    def isValidRow(self, board, rowNumber):
        hashset = set()
        for i in range(9):
            char = board[rowNumber][i]
            if char == ".":
                continue
            if char in hashset:
                return False
            else:
                hashset.add(char)
        return True

    def isValidColumn(self, board, columnNum):
        hashset = set()
        for i in range(9):
            char = board[i][columnNum]
            if char == ".":
                continue
            if char in hashset:
                return False
            else:
                hashset.add(char)
        return True

    def isValidBox(self, board, rowStart, colStart):
        hashset = set()
        for i in range(rowStart, rowStart + 3):
            for j in range(colStart, colStart + 3):
                char = board[i][j]
                if char == ".":
                    continue
                if char in hashset:
                    return False
                else:
                    hashset.add(char)
        return True


if __name__ == '__main__':
#     print(Solution().isValidSudoku([["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]))
    rows = [set() for _ in range(9)]
    print(rows)
    row = set((1,2))
    print(len(row))
