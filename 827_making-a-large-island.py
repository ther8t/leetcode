class DSU:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def get_size(self, i):
        return self.size[self.find(i)]

    def union(self, i1, i2):
        i1_parent = self.find(i1)
        i2_parent = self.find(i2)
        if self.size[i1_parent] > self.size[i2_parent]:
            self.parent[i2_parent] = i1_parent
            self.size[i1_parent] += self.size[i2_parent]
        else:
            self.parent[i1_parent] = i2_parent
            self.size[i2_parent] += self.size[i1_parent]


class Solution:
    def largestIsland(self, grid) -> int:
        rows, cols, n = len(grid), len(grid[0]), len(grid)
        ones, zeros = 0, 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]: ones += 1
                else: zeros += 1

        if ones == n * n:
            return n * n

        if zeros == n * n:
            return 1

        def bfs(r, c, id):
            queue = [(r, c)]
            grid[r][c] = id
            size_map[id] = 1

            while queue:
                r, c = queue.pop(0)

                for nr, nc in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        grid[nr][nc] = id
                        size_map[id] += 1
        size_map = {}
        latest_id = 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    latest_id += 1
                    bfs(r, c, latest_id)

        largest_island_size = -float('inf')
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    combined_island_size = 0
                    visited = set()
                    for nr, nc in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 0 and grid[nr][nc] not in visited:
                            combined_island_size += size_map[grid[nr][nc]]
                            visited.add(grid[nr][nc])
                    largest_island_size = max(largest_island_size, combined_island_size + 1)
                else:
                    largest_island_size = max(largest_island_size, size_map[grid[r][c]])

        return largest_island_size

    # def largestIsland(self, grid) -> int:
    #     rows, cols, n = len(grid), len(grid[0]), len(grid)
    #     dsu = DSU(rows * cols)
    #     ones, zeros = 0, 0
    #     for r in range(rows):
    #         for c in range(cols):
    #             if grid[r][c]: ones += 1
    #             else: zeros += 1
    #
    #     if ones == n * n:
    #         return n * n
    #
    #     if zeros == n * n:
    #         return 1
    #
    #     def bfs(r, c):
    #         queue = [(r, c)]
    #         visited.add((r, c))
    #
    #         while queue:
    #             r, c = queue.pop(0)
    #
    #             for nr, nc in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
    #                 if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr, nc) not in visited:
    #                     visited.add((nr, nc))
    #                     queue.append((nr, nc))
    #                     dsu.union(r * n + c, nr * n + nc)
    #
    #     visited = set()
    #     for r in range(rows):
    #         for c in range(cols):
    #             if grid[r][c] == 1 and (r, c) not in visited: bfs(r, c)
    #
    #     largest_island_size = -float('inf')
    #     for r in range(rows):
    #         for c in range(cols):
    #             if grid[r][c] == 0:
    #                 combined_island_size = 0
    #                 visited = set()
    #                 for nr, nc in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
    #                     if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and dsu.find(nr * n + nc) not in visited:
    #                         combined_island_size += dsu.get_size(nr * n + nc)
    #                         visited.add(dsu.find(nr * n + nc))
    #                 largest_island_size = max(largest_island_size, combined_island_size + 1)
    #             else:
    #                 largest_island_size = max(largest_island_size, dsu.get_size(r * n + c))
    #
    #     return largest_island_size

    def largestIsland(self, grid) -> int:
        rows, cols, n = len(grid), len(grid[0]), len(grid)
        ones, zeros = 0, 0
        latest_island_id = 0
        island_size_counter = {}
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]: ones += 1
                else: zeros += 1

        if ones >= n * n - 1:
            return n * n

        if zeros == n * n:
            return 1

        def bfs(r, c):
            queue = [(r, c)]
            grid[r][c] = latest_island_id

            while queue:
                r, c = queue.pop(0)
                island_size_counter[latest_island_id] += 1

                for nr, nc in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = latest_island_id
                        queue.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    latest_island_id -= 1
                    island_size_counter[latest_island_id] = 0
                    bfs(r, c)

        largest_island_size = island_size_counter[max(island_size_counter, key=lambda x: island_size_counter[x])]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    combined_island_size = 0
                    surrounding_islands = set()
                    for nr, nc in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 0 and grid[nr][nc] not in surrounding_islands:
                            surrounding_islands.add(grid[nr][nc])
                            combined_island_size += island_size_counter[grid[nr][nc]]
                    largest_island_size = max(largest_island_size, combined_island_size + 1)

        return largest_island_size


if __name__ == '__main__':
    print(Solution().largestIsland(grid = [[1,0],[0,1]]))
    print(Solution().largestIsland(grid = [[1,1],[1,0]]))
    print(Solution().largestIsland(grid = [[1,1],[1,1]]))
