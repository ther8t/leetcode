import collections


class Solution:
    """
    The reason this algo doesn't work is because there might be a cell which could accommodate by more than one number but if you look closely the rows and columns would allow just one number out of them to really be there.
    For example the rightmost topmost cell in the example could contain {2, 3, 5}, but 2 cannot be placed anywhere else in the box. It is bound to contain 2 only.
    """
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        N = 9
        solver = [[{"1", "2", "3", "4", "5", "6", "7", "8", "9"} for _ in range(N)] for _ in range(N)]
        filledValues = 0

        def addValue(val, row, col):
            # remove from column
            a = solver[row][col]
            solver[row][col] = {}

            for i in range(9):
                try:
                    solver[row][i].remove(val)
                except:
                    pass

            # remove from row
            for i in range(9):
                try:
                    solver[i][col].remove(val)
                except:
                    pass

            # remove from box
            for i in range(row // 3 * 3, row // 3 * 3 + 3):
                for j in range(col // 3 * 3, col // 3 * 3 + 3):
                    try:
                        solver[i][j].remove(val)
                    except:
                        pass

        for row in range(N):
            for col in range(N):
                char = board[row][col]
                if char == ".":
                    continue
                filledValues += 1
                addValue(char, row, col)

        while filledValues != 81:
            for row in range(N):
                for col in range(N):
                    if len(solver[row][col]) == 1:
                        char = solver[row][col].pop()
                        board[row][col] = char
                        addValue(char, row, col)
                        filledValues += 1




    # def solveSudoku(self, board):
    #     """
    #     Do not return anything, modify board in-place instead.
    #     """
    #     N = 9
    #     cells = [[{"1", "2", "3", "4", "5", "6", "7", "8", "9"} for _ in range(N)] for _ in range(N)]
    #     rows = [[9, 9, 9, 9, 9, 9, 9, 9, 9] for _ in range(N)]
    #     cols = [[9, 9, 9, 9, 9, 9, 9, 9, 9] for _ in range(N)]
    #     boxes = [[9, 9, 9, 9, 9, 9, 9, 9, 9] for _ in range(N)]
    #
    #     def addValue(val, row, col):
    #         cells[row][col] = {}
    #
    #         # remove from column
    #         for i in range(9):
    #             try:
    #                 cells[row][i].remove(val)
    #             except:
    #                 pass
    #         cols[col][int(val) - 1] -= 1
    #
    #         # remove from row
    #         for i in range(9):
    #             try:
    #                 cells[i][col].remove(val)
    #             except:
    #                 pass
    #         rows[row][int(val) - 1] -= 1
    #
    #         # remove from box
    #         for i in range(row // 3 * 3, row // 3 * 3 + 3):
    #             for j in range(col // 3 * 3, col // 3 * 3 + 3):
    #                 try:
    #                     cells[i][j].remove(val)
    #                 except:
    #                     pass
    #         boxes[row // 3 * 3 + col // 3][int(val) - 1] -= 1
    #
    #     def removeValue(val, row, col):
    #         # remove from column
    #         for i in range(9):
    #             try:
    #                 cells[row][i].add(val)
    #             except:
    #                 pass
    #         cols[col].add(val)
    #
    #         # remove from row
    #         for i in range(9):
    #             try:
    #                 cells[i][col].add(val)
    #             except:
    #                 pass
    #         rows[row].add(val)
    #
    #         # remove from box
    #         for i in range(row // 3 * 3, row // 3 * 3 + 3):
    #             for j in range(col // 3 * 3, col // 3 * 3 + 3):
    #                 try:
    #                     cells[i][j].add(val)
    #                 except:
    #                     pass
    #         boxes[row // 3 * 3 + col // 3].add(val)
    #
    #     filledValues = 0
    #     for row in range(N):
    #         for col in range(N):
    #             char = board[row][col]
    #             if char == ".":
    #                 continue
    #             filledValues += 1
    #             addValue(char, row, col)
    #     print(boxes)
    #
    #     while filledValues != 81:
    #         cellsFilled = 0
    #         for row in range(N):
    #             for col in range(N):
    #                 if board[row][col] == "." and len(cells[row][col]) == 1:
    #                     char = cells[row][col].pop()
    #                     board[row][col] = char
    #                     addValue(char, row, col)
    #                     filledValues += 1
    #                     cellsFilled += 1
    #         if cellsFilled == 0:
    #             # print(board)
    #             # print(cells)
    #             # print(rows)
    #             # print(cols)
    #             print(boxes)
    #
    #             break


if __name__ == '__main__':
    Solution().solveSudoku(
        [[".", ".", "9", "7", "4", "8", ".", ".", "."], ["7", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", "2", ".", "1", ".", "9", ".", ".", "."], [".", ".", "7", ".", ".", ".", "2", "4", "."],
         [".", "6", "4", ".", "1", ".", "5", "9", "."], [".", "9", "8", ".", ".", ".", "3", ".", "."],
         [".", ".", ".", "8", ".", "3", ".", "2", "."], [".", ".", ".", ".", ".", ".", ".", ".", "6"],
         [".", ".", ".", "2", "7", "5", "9", ".", "."]])
