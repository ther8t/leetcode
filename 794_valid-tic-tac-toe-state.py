class Solution:
    def validTicTacToe(self, board) -> bool:
        x_count, o_count, space_count = 0, 0, 0
        for row in board:
            for cell in row:
                x_count += 1 if cell == 'X' else 0
                o_count += 1 if cell == 'O' else 0
                space_count += 1 if cell == ' ' else 0

        if x_count - o_count not in {0, 1}:
            return False

        if ((board[0] == 'XXX' or board[1] == 'XXX' or board[2] == 'XXX') or (
                board[0][0] == board[1][0] == board[2][0] == "X" or board[0][1] == board[1][1] == board[2][1] == "X" or
                board[0][2] == board[1][2] == board[2][2] == "X") or (
                        board[0][0] == board[1][1] == board[2][2] == 'X') or (
                        board[0][2] == board[1][1] == board[2][0] == 'X')) and x_count - o_count != 1:
            return False
        if ((board[0] == 'OOO' or board[1] == 'OOO' or board[2] == 'OOO') or (
                board[0][0] == board[1][0] == board[2][0] == "O" or board[0][1] == board[1][1] == board[2][1] == "O" or
                board[0][2] == board[1][2] == board[2][2] == "O") or (
                        board[0][0] == board[1][1] == board[2][2] == 'O') or (
                        board[0][2] == board[1][1] == board[2][0] == 'O')) and x_count - o_count != 0:
            return False

        return True


if __name__ == '__main__':
    print(Solution().validTicTacToe(board=["XOX", "O O", "XOX"]))
