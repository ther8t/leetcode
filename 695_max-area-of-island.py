class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            descendent_count = 0
            for nr, nc in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    descendent_count += dfs(nr, nc)
            return descendent_count + 1

        max_island_size = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 or (r, c) in visited:
                    continue
                visited.add((r, c))
                max_island_size = max(max_island_size, dfs(r, c))

        return max_island_size


if __name__ == '__main__':
    print(Solution().maxAreaOfIsland(grid = [[0,0,0,0,0,0,0,0]]))
