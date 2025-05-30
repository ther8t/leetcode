import collections


class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        N = 9
        rows = [{"1", "2", "3", "4", "5", "6", "7", "8", "9"} for _ in range(N)]
        cols = [{"1", "2", "3", "4", "5", "6", "7", "8", "9"} for _ in range(N)]
        boxes = [{"1", "2", "3", "4", "5", "6", "7", "8", "9"} for _ in range(N)]

        def addValue(val, row, col):
            board[row][col] = val

            rows[row].remove(val)
            cols[col].remove(val)
            boxes[row // 3 * 3 + col // 3].remove(val)

        def removeValue(val, row, col):
            board[row][col] = "."

            rows[row].add(val)
            cols[col].add(val)
            boxes[row // 3 * 3 + col // 3].add(val)

        def canAdd(val, row, col):
            return True if val in rows[row] and val in cols[col] and val in boxes[row // 3 * 3 + col // 3] else False

        def initialize():
            for row in range(N):
                for col in range(N):
                    char = board[row][col]
                    if char == ".":
                        continue
                    addValue(char, row, col)

        def backtrack(row=0, col=0):
            if row == N - 1 and col == N - 1:
                if board[row][col] == ".":
                    board[row][col] = rows[N - 1].pop()
                return True

            if board[row][col] != ".":
                if col == N - 1:
                    return backtrack(row + 1, 0)
                else:
                    return backtrack(row, col + 1)

            # fill yourself with some value and backtrack to next value.
            for i in range(1, 10):
                if canAdd(str(i), row, col):
                    addValue(str(i), row, col)
                    isSolved = False
                    if col == N - 1:
                        isSolved = backtrack(row + 1, 0)
                    else:
                        isSolved = backtrack(row, col + 1)

                    if isSolved:
                        return True
                    else:
                        removeValue(str(i), row, col)
            return False

        initialize()
        backtrack()


if __name__ == '__main__':
    Solution().solveSudoku(
        [[".", ".", "9", "7", "4", "8", ".", ".", "."], ["7", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", "2", ".", "1", ".", "9", ".", ".", "."], [".", ".", "7", ".", ".", ".", "2", "4", "."],
         [".", "6", "4", ".", "1", ".", "5", "9", "."], [".", "9", "8", ".", ".", ".", "3", ".", "."],
         [".", ".", ".", "8", ".", "3", ".", "2", "."], [".", ".", ".", ".", ".", ".", ".", ".", "6"],
         [".", ".", ".", "2", "7", "5", "9", ".", "."]])
