class Solution:
    """
    Although a classic backtracking problem, this question posed a different sort of challenge.
    It was to get the code working in time.
    The usual place the queen and check by loop to see if it clashes doesn't work. In that sense this question is similar to 1275_find-winner-on-a-tic-tac-toe-game.
    The idea is to capture rows, cols, diagonals and anti-diagonals.
    """
    def solveNQueens(self, n: int):
        out = {}
        queen_positions = set()
        rows, cols, diagonals, antidiagonals = set(), set(), set(), set()

        def place_queen(n_queen, r, start_row, start_col):
            if n_queen == 0:
                board = []
                key = ""
                for r in range(n):
                    row = ""
                    for c in range(n):
                        if (r, c) in queen_positions:
                            row += "Q"
                            key += "Q"
                        else:
                            row += "."
                            key += "."
                    board.append(row)
                out[key] = board
                return
            for c in range(n):
                if r < start_row:
                    continue
                if r not in rows and c not in cols and (r - c) not in diagonals and (r + c) not in antidiagonals:
                    queen_positions.add((r, c))
                    rows.add(r)
                    cols.add(c)
                    diagonals.add(r - c)
                    antidiagonals.add(r + c)
                    place_queen(n_queen - 1, r + 1, r, c)
                    rows.remove(r)
                    cols.remove(c)
                    diagonals.remove(r - c)
                    antidiagonals.remove(r + c)
                    queen_positions.remove((r, c))

        place_queen(n, 0, 0, 0)
        return list(out.values())


if __name__ == '__main__':
    print(Solution().solveNQueens(9))
    # print(Solution().solveNQueens(3))

