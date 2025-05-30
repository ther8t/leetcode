import functools
import sys


class recursionlimit:
    def __init__(self, limit):
        self.limit = limit

    def __enter__(self):
        self.old_limit = sys.getrecursionlimit()
        sys.setrecursionlimit(self.limit)

    def __exit__(self, type, value, tb):
        sys.setrecursionlimit(self.old_limit)


class Solution:
    # def tilingRectangle(self, n: int, m: int) -> int:
    #     squares = [side * side for side in range(1, 14)]
    #     dp = {}
    #
    #     def tile(area):
    #         if area < 0:
    #             return float('inf')
    #         if area == 0:
    #             return 0
    #         if area in dp:
    #             return dp[area]
    #         min_squares = float('inf')
    #         for i in range(len(squares) - 1, -1, -1):
    #             if squares[i] > area:
    #                 continue
    #             min_squares = min(min_squares, tile(area - squares[i]) + 1)
    #         if min_squares != float('inf'):
    #             dp[area] = min_squares
    #         return min_squares
    #
    #     return tile(m * n)

    """
    Don't know about this because I never tested this code. It takes an enormously long time to execute.
    """
    def tilingRectangle(self, n: int, m: int) -> int:

        def perimeter(index, doubled, total):
            if index >= len(stack):
                return False
            if total == m + n and doubled:
                return True
            if total > m + n:
                return False
            ans = perimeter(index + 1, doubled, total + stack[index])
            if ans:
                return True
            if not doubled:
                ans = perimeter(index + 1, True, total + 2 * stack[index])
                if ans:
                    return True
            return False

        def tile(area):
            if area > m * n:
                return float('inf')
            if area == m * n:
                if perimeter(0, False, 0):
                    return 0
                return float('inf')

            min_squares = float('inf')
            for i in range(1, min(m, n) + 1):
                stack.append(i)
                min_squares = min(min_squares, tile(area + i * i) + 1)
                stack.pop()

            return min_squares

        stack = []
        return tile(0)


    @functools.lru_cache(None)
    def tilingRectangle(self, n: int, m: int) -> int:
        if m == n:
            return 1
        if m == 1:
            return n
        if n == 1:
            return m
        if n > m:
            return self.tilingRectangle(m, n)

        ans = m * n
        for i in range(1, m):
            ans = min(ans, self.tilingRectangle(n, i) + self.tilingRectangle(m - i, n))

        for i in range(1, n):
            ans = min(ans, self.tilingRectangle(m, i) + self.tilingRectangle(n - i, m))

        for sq in range(1, min(n, m)):
            for x in range(1, m - sq):
                for y in range(1, n - sq):
                    partition1 = self.tilingRectangle(y, x + sq)
                    partition2 = self.tilingRectangle(x, n - y)
                    partition3 = self.tilingRectangle(n - sq - y, m - x)
                    partition4 = self.tilingRectangle(sq + y, m - x - sq)
                    ans = min(ans, partition1 + partition2 + partition3 + partition4 + 1)

        return ans






if __name__ == '__main__':
    # with recursionlimit(10000):
    print(Solution().tilingRectangle(n = 2, m = 3))
    print(Solution().tilingRectangle(n = 5, m = 8))
    print(Solution().tilingRectangle(11, 13))
