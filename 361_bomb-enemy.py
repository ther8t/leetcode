class Solution:
    def maxKilledEnemies(self, grid) -> int:
        rows, cols = len(grid), len(grid[0])
        damage = [[0 for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            left, right = 0, 0
            score = 0
            while left < cols:
                if right >= cols or grid[r][right] == 'W':
                    for c in range(left, right):
                        if grid[r][c] == '0':
                            damage[r][c] += score
                    score = 0
                    left = right + 1
                elif grid[r][right] == 'E':
                    score += 1
                right += 1

        for c in range(cols):
            top, bottom = 0, 0
            score = 0
            while top < rows:
                if bottom >= rows or grid[bottom][c] == 'W':
                    for r in range(top, bottom):
                        if grid[r][c] == '0':
                            damage[r][c] += score
                    score = 0
                    top = bottom + 1
                elif grid[bottom][c] == 'E':
                    score += 1
                bottom += 1

        return max([max(damage[i]) for i in range(rows)])


if __name__ == '__main__':
    print(Solution().maxKilledEnemies(grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]))
    print(Solution().maxKilledEnemies(grid = [["W","W","W"],["0","0","0"],["E","E","E"]]))
