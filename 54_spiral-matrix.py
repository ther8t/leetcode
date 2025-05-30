class Solution:
    def spiralOrder(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0

        def neighbour(r, c):
            nonlocal d
            for _ in range(4):
                nr, nc = directions[d]
                if 0 <= r + nr < rows and 0 <= c + nc < cols and (r + nr, c + nc) not in visited:
                    return True
                d = (d + 1) % 4
            return False

        r, c = 0, 0
        visited.add((r, c))
        out = [matrix[0][0]]
        while neighbour(r, c):
            nr = r + directions[d][0]
            nc = c + directions[d][1]
            out.append(matrix[nr][nc])
            visited.add((nr, nc))
            r, c = nr, nc
        return out


    # def spiralOrder(self, matrix):
    #     rows, cols = len(matrix), len(matrix[0])
    #     out = []
    #
    #     def spiral():
    #         for col in range(col_start, col_end + 1):
    #             out.append(matrix[row_start][col])
    #         if row_start == row_end:
    #             return
    #         for row in range(row_start + 1, row_end + 1):
    #             out.append(matrix[row][col_end])
    #         for col in range(col_end - 1, col_start - 1, -1):
    #             out.append(matrix[row_end][col])
    #         if col_start == col_end:
    #             return
    #         for row in range(row_end - 1, row_start, -1):
    #             out.append(matrix[row][col_start])
    #
    #     row_start, row_end, col_start, col_end = 0, rows - 1, 0, cols - 1
    #
    #     while row_end >= row_start and col_end >= col_start:
    #         spiral()
    #         if row_end >= row_start:
    #             row_start += 1
    #             row_end -= 1
    #         if col_end >= col_start:
    #             col_start += 1
    #             col_end -= 1
    #
    #     return out


if __name__ == '__main__':
    print(Solution().spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
    print(Solution().spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
    print(Solution().spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
    print(Solution().spiralOrder([[6, 7, 9]]))
    print(Solution().spiralOrder([[7],[9],[6]]))

