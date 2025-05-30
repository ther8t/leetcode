class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ptr = 0
        direction = 1
        a = [[] for _ in range(numRows)]
        for i in range(len(s)):
            a[ptr].append(s[i])
            if ptr == 0:
                direction = 1
            if ptr == numRows - 1:
                direction = -1
            if numRows == 1:
                direction = 0
            ptr += direction

        out = ""
        for i in range(numRows):
            out += "".join(a[i])

        return out


    # def convert(self, s: str, numRows: int) -> str:
    #     ss = ""
    #     for i in range(0, numRows):
    #         ss+=self.getRow(s, i, numRows)
    #
    #     return ss
    #
    # def getRow(self, s, row, numRows):
    #     if numRows == 1:
    #         return s
    #     freq = 2 * numRows - 2
    #     index = 0
    #     ss = ""
    #     for index in range(0, len(s) + row, freq):
    #         if row == 0 or row % (numRows - 1) == 0:
    #             ss += s[index + row: index + row + 1]
    #         else:
    #             if (index - row) >= 0 and (index - row + 1) >= 0:
    #                 ss += s[index - row: index - row + 1]
    #             if (index + row) < len(s) and (index + row + 1) <= len(s):
    #                 ss += s[index + row: index + row + 1]
    #     return ss


if __name__ == '__main__':
    # print(Solution().convert(s = "PAYPALISHIRING", numRows = 3))
    print(Solution().convert(s = "ABC", numRows = 1))
