class NumMatrix:

    def __init__(self, matrix):
        self.rows, self.cols = len(matrix), len(matrix[0])
        self.matrix = matrix

    def update(self, row: int, col: int, val: int) -> None:
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.matrix[row][col] = val

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        rs = max(0, min(row1, row2))
        re = min(self.rows, max(row1 + 1, row2 + 1))
        cs = max(0, min(col1, col2))
        ce = min(self.cols, max(col1 + 1, col2 + 1))

        sum = 0
        for r in range(rs, re):
            for c in range(cs, ce):
                sum += self.matrix[r][c]

        return sum


if __name__ == '__main__':
    # Your NumMatrix object will be instantiated and called as such:
    obj = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    print(obj.sumRegion(2, 1, 4, 3))
    obj.update(3, 2, 2)
    print(obj.sumRegion(2, 1, 4, 3))
