class Solution:
    def getFood(self, grid) -> int:
        rows, cols = len(grid), len(grid[0])
        source = None
        queue = []
        visited = set()

        for i in range(rows):
            if source:
                break
            for j in range(cols):
                if grid[i][j] == "*":
                    source = (i, j)
                    break

        queue.append((0, source))
        visited.add(source)

        while queue:
            d, (r, c) = queue.pop(0)

            for nr, nc in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == "#":
                        return d + 1
                    if grid[nr][nc] == "O" and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((d + 1, (nr, nc)))

        return -1


if __name__ == '__main__':
    print(Solution().getFood(grid = [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]))
    print(Solution().getFood(grid = [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]))
    print(Solution().getFood(grid = [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]]))
