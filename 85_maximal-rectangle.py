import functools


class Solution:
    """
    Attempt: Fired
    TLE
    """
    def maximalRectangle(self, matrix) -> int:
        m, n = len(matrix), len(matrix[0])
        r_sum = [[0] * (n + 1) for _ in range(m)]

        for i in range(m):
            for j in range(n):
                r_sum[i][j] = r_sum[i][j - 1] + int(matrix[i][j] == "1")

        @functools.lru_cache(None)
        def get_height(x, y, w):
            for i in range(x, m):
                if r_sum[i][y + w - 1] - r_sum[i][y - 1] != w:
                    return i - x

            return m - x

        max_area = 0
        for i in range(m):
            lo, hi = 0, 0
            while lo < n:
                if matrix[i][lo] == "0":
                    lo += 1
                    continue

                hi = lo
                while hi < n and matrix[i][hi] == "1":
                    if r_sum[i][hi] - r_sum[i][lo] == hi - lo:
                        max_area = max(max_area, (hi - lo) * get_height(i, lo, hi - lo))
                        hi += 1
                    max_area = max(max_area, (hi - lo) * get_height(i, lo, hi - lo))
                lo += 1

        return max_area

    # def maximalRectangle(self, matrix) -> int:
        # m, n = len(matrix), len(matrix[0])
        # end = [[(i, j) for j in range(n)] for i in range(m)]
        #
        # max_area = 0
        # end[m - 1][n - 1] = (m, n) if matrix == "1" else (m - 1, n - 1)
        # for i in range(m - 1, -1, -1):
        #     for j in range(n - 1, -1, -1):
        #         if matrix[i][j] == "0":
        #             end[i][j] = (i, j)
        #             continue
        #         er = min(end[i + 1][j][0] if 0 <= i + 1 < m and matrix[i + 1][j] == "1" else m, end[i][j + 1][0] if 0 <= j + 1 < n and matrix[i][j + 1] == "1" else i)
        #         ec = min(end[i + 1][j][1] if 0 <= i + 1 < m and matrix[i + 1][j] == "1" else j, end[i][j + 1][1] if 0 <= j + 1 < n and matrix[i][j + 1] == "1" else n)
        #         end[i][j] = (er, ec)
        #         max_area = max(max_area, (er - i + 1) * (ec - j + 1))
        #
        # return max_area

    def maximalRectangle(self, matrix) -> int:
        m, n = len(matrix), len(matrix[0])
        width = [[0] * (n + 1) for _ in range(m + 1)]
        max_area = 0

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == "0":
                    width[i][j] = 0
                    continue
                width[i][j] = width[i][j + 1] + 1
                k = i
                max_width = n
                while k < m and matrix[k][j] == "1":
                    max_width = min(max_width, width[k][j])
                    k += 1
                    max_area = max(max_area, max_width * (k - i))

        return max_area





if __name__ == '__main__':
    print(Solution().maximalRectangle(matrix = [["1","0","1","0","0"],
                                                ["1","0","1","1","1"],
                                                ["1","1","1","1","1"],
                                                ["1","0","0","1","0"]]))
    print(Solution().maximalRectangle(matrix = [["0"]]))
    print(Solution().maximalRectangle(matrix = [["1"]]))
    print(Solution().maximalRectangle([["1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","0"],["1","1","1","1","1","0","0","0"],["0","1","1","1","1","0","0","0"]]))
    print(Solution().maximalRectangle([["1","0","1","1","0","1"],["1","1","1","1","1","1"],["0","1","1","0","1","1"],["1","1","1","0","1","0"],["0","1","1","1","1","1"],["1","1","0","1","1","1"]]))
