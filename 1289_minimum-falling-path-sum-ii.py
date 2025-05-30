import functools
import heapq


class Solution:
    """
    Wrong answer
    """
    def minFallingPathSum(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return grid[m - 1][n - 1]

        h = []
        for i in range(n):
            heapq.heappush(h, (grid[0][i], 0, i))

        while h:
            min_sum, current_row, current_col = heapq.heappop(h)
            if current_row == m:
                return min_sum

            for i in range(n):
                if i == current_col:
                    continue
                heapq.heappush(h, (min_sum + (0 if current_row == m - 1 else grid[current_row + 1][i]), current_row + 1, i))

        return -1

    """
    Wrong answer: For negative values, let's say the answer was -267, the sum starts at 0, so terminal condition is already met.
    """
    def minFallingPathSum(self, grid) -> int:
        m, n = len(grid), len(grid[0])

        def check(row, s, prev_col):
            if row == m and s > mid:
                return True
            for i in range(n):
                if i == prev_col:
                    continue
                if check(row + 1, s + grid[row][i], i):
                    return True

            return False

        lo, hi = -200 * 100, 200 * 100
        while lo < hi:
            mid = (lo + hi) // 2
            if check(0, 0, -1):
                hi = mid
            else:
                lo = mid + 1

        return hi

    def minFallingPathSum(self, grid) -> int:
        m, n = len(grid), len(grid[0])

        @functools.lru_cache(None)
        def dfs(index, last_col):
            if index == m:
                return 0

            min_sum = float('inf')
            for i in range(n):
                if i == last_col:
                    continue
                min_sum = min(min_sum, grid[index][i] + dfs(index + 1, i))

            return min_sum

        return dfs(0, -1)


if __name__ == '__main__':
    print(Solution().minFallingPathSum(grid = [[1,2,3],[4,5,6],[7,8,9]]))
    print(Solution().minFallingPathSum(grid = [[7]]))
    print(Solution().minFallingPathSum(grid = [[-37,51,-36,34,-22],[82,4,30,14,38],[-68,-52,-92,65,-85],[-49,-3,-77,8,-19],[-60,-71,-21,-62,-73]]))
