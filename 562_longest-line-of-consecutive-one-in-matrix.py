class Solution:
    def longestLine(self, mat) -> int:
        rows, cols = len(mat), len(mat[0])
        record_keeper = [[[0, 0, 0, 0] for _ in range(cols)] for _ in range(rows)]
        max_length = 0

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    continue
                my_record = [0, 0, 0, 0]
                # horizontal
                if i > 0 and mat[i - 1][j] == 1:
                    my_record[0] = record_keeper[i - 1][j][0] + 1
                else:
                    my_record[0] = 1

                # diagonal
                if i > 0 and j > 0 and mat[i - 1][j - 1] == 1:
                    my_record[1] = record_keeper[i - 1][j - 1][1] + 1
                else:
                    my_record[1] = 1

                # vertical
                if j > 0 and mat[i][j - 1] == 1:
                    my_record[2] = record_keeper[i][j - 1][2] + 1
                else:
                    my_record[2] = 1

                # anti-diagonal
                if i > 0 and j < cols - 1 and mat[i - 1][j + 1] == 1:
                    my_record[3] = record_keeper[i - 1][j + 1][3] + 1
                else:
                    my_record[3] = 1

                max_length = max(my_record + [max_length])
                record_keeper[i][j] = my_record

        return max_length


if __name__ == '__main__':
    print(Solution().longestLine(mat = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]))
