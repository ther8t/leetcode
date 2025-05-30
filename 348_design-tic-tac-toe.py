class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [{1: 0, 2: 0} for _ in range(n)]
        self.cols = [{1: 0, 2: 0} for _ in range(n)]
        self.diagonal1 = {1: 0, 2: 0}
        self.diagonal2 = {1: 0, 2: 0}

    def move(self, row: int, col: int, player: int) -> int:
        self.rows[row][player] += 1
        self.cols[col][player] += 1
        if row == col:
            self.diagonal1[player] += 1
        if row + col == self.n - 1:
            self.diagonal2[player] += 1
        if self.rows[row][player] == self.n or self.cols[col][player] == self.n:
            return player
        if (row == col and self.diagonal1[player] == self.n) or (row + col == self.n - 1 and self.diagonal2[player] == self.n):
            return player

        return 0


if __name__ == '__main__':
    # Your TicTacToe object will be instantiated and called as such:
    obj = TicTacToe(3)
    print(obj.move(0, 0, 1))
    print(obj.move(0, 2, 2))
    print(obj.move(2, 2, 1))
    print(obj.move(1, 1, 2))
    print(obj.move(2, 0, 1))
    print(obj.move(1, 0, 2))
    print(obj.move(2, 1, 1))
