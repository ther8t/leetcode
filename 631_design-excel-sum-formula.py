import re


class Excel:

    def resolve_row(self, index):
        index = int(index)
        return index - 1

    def resolve_col(self, index):
        index = str(index)
        final_index = 0
        for i in range(len(index) - 1, -1, -1):
            base = pow(26, (len(index) - 1) - i)
            final_index += base * (ord(index[i]) - ord('A'))
        return final_index

    def __init__(self, height: int, width: str):
        self.mat = [[0 for _ in range(self.resolve_col(width) + 1)] for _ in range(height + 1)]

    def set(self, row: int, column: str, val: int) -> None:
        self.set_value(row, column, val)

    def get(self, row: int, column: str) -> int:
        resolved_row = self.resolve_row(row)
        resolved_col = self.resolve_col(column)
        if type(self.mat[resolved_row][resolved_col]) is tuple:
            return self.compute_sum(self.mat[resolved_row][resolved_col])
        else:
            return self.mat[resolved_row][resolved_col]

    def sum(self, row: int, column: str, numbers) -> int:
        self.set_value(row, column, (row, column, numbers))
        return self.get(row, column)

    def set_value(self, row, column, value):
        self.mat[self.resolve_row(row)][self.resolve_col(column)] = value

    def compute_sum(self, formula):
        numbers = formula[2]
        sum = 0
        for sub_sum in numbers:
            match = re.match("([A-Z]+)([0-9]+):([A-Z]+)([0-9]+)", sub_sum)
            if match is None:
                match = re.match("([A-Z]+)([0-9]+)", sub_sum)
                start_row = self.resolve_row(match.group(2))
                end_row = self.resolve_row(match.group(2))
                start_col = self.resolve_col(match.group(1))
                end_col = self.resolve_col(match.group(1))
            else:
                start_row = self.resolve_row(match.group(2))
                end_row = self.resolve_row(match.group(4))
                start_col = self.resolve_col(match.group(1))
                end_col = self.resolve_col(match.group(3))
            for i in range(start_row, end_row + 1):
                for j in range(start_col, end_col + 1):
                    value = self.mat[i][j]
                    if type(value) is tuple:
                        value = self.compute_sum(value)
                    sum += value
        return sum


# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)

if __name__ == '__main__':
    # ["Excel", "set", "set", "sum", "sum"]
    # [[26, "Z"], [1, "A", 1], [1, "I", 1], [7, "D", ["A1:D6", "A1:G3", "A1:C12"]],
    #  [10, "G", ["A1:D7", "D1:F10", "D3:I8", "I1:I9"]]]
    excel = Excel(26, "Z")
    excel.set(1, "A", 1)
    excel.set(1, "I", 1)
    print(excel.sum(7, "D", ["A1:D6", "A1:G3", "A1:C12"]))
    print(excel.sum(10, "G", ["A1:D7", "D1:F10", "D3:I8", "I1:I9"]))
