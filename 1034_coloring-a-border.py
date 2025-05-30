class Solution:
    def colorBorder(self, grid, row: int, col: int, color: int):
        rows, cols = len(grid), len(grid[0])
        visited = set()
        visited.add((row, col))
        my_color = grid[row][col]
        border = set()

        def neighbour(r, c):
            for nr, nc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                yield nr, nc

        def dfs(r, c):
            is_border = False
            if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                is_border = True
            else:
                for nr, nc in neighbour(r, c):
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != my_color:
                        is_border = True
                        break

            if is_border:
                border.add((r, c))

            for nr, nc in neighbour(r, c):
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == my_color:
                    visited.add((nr, nc))
                    dfs(nr, nc)

        dfs(row, col)
        for r, c in border:
            grid[r][c] = color
        return grid


if __name__ == '__main__':
    print(Solution().colorBorder(grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2))
    print(Solution().colorBorder(grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3))
    print(Solution().colorBorder(grid = [[1,1],[1,2]], row = 0, col = 0, color = 3))
