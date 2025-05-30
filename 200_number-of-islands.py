class Solution:
    def numIslands(self, grid) -> int:
        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def bfs(r, c):
            queue = [(r, c)]
            visited = set()
            visited.add((r, c))
            while queue:
                r, c = queue.pop(0)
                grid[r][c] = ""

                for nr, nc in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1' and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    island_count += 1
                    bfs(r, c)

        return island_count


    """
    """
    def numIslands(self, grid) -> int:
        rows, cols = len(grid), len(grid[0])
        island_count = 0
        visited = set()

        def bfs(r, c):
            queue = [(r, c)]
            visited.add((r, c))
            while queue:
                r, c = queue.pop(0)

                for nr, nc in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1' and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    island_count += 1
                    bfs(r, c)

        return island_count


if __name__ == '__main__':
    print(Solution().numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))
