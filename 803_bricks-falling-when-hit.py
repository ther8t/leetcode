class DSU:
    def __init__(self, rows, cols):
        self.parent = [i for i in range(rows * cols + 1)]
        self.rank = [0] * (rows * cols + 1)
        self.size = [1] * (rows * cols + 1)

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.find(self.parent[x])

    def union(self, x, y):
        parent_x, parent_y = self.find(x), self.find(y)
        if parent_x == parent_y:
            return
        if self.rank[parent_x] >= self.rank[parent_y]:
            self.rank[parent_x] += 1
            self.parent[parent_y] = parent_x
            self.size[parent_x] += self.size[parent_y]
        else:
            self.rank[parent_y] += 1
            self.parent[parent_x] = parent_y
            self.size[parent_y] += self.size[parent_x]

    def top(self):
        return self.size[self.find(len(self.size) - 1)] - 1


class Solution:
    def hitBricks(self, grid, hits):
        rows, cols = len(grid), len(grid[0])
        dsu = DSU(rows, cols)

        def index(r, c):
            return r * cols + c

        def neighbours(r, c):
            for nr, nc in [(r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c)]:
                if 0 <= nr < rows and 0 <= nc < cols:
                    yield nr, nc

        A = [row[:] for row in grid]
        for r, c in hits:
            A[r][c] = 0

        for r in range(rows):
            for c in range(cols):
                if A[r][c] == 0:
                    continue
                i = index(r, c)
                if r == 0:
                    dsu.union(i, rows * cols)
                if r > 0 and A[r - 1][c] == 1:
                    dsu.union(i, index(r - 1, c))
                if c > 0 and A[r][c - 1] == 1:
                    dsu.union(i, index(r, c - 1))
                """
                Revision 2:
                This is a surprise to me that the code works with just the above two conditions. i.e. joining a brick above and a brick to the left.
                It sure works for all four sides
                Ok. my bad I was thinking the purpose of the code was different. I now recognise that the code I thought it was requires all four side.
                This code is required to combine all the bricks for the final run. There is no surprise that only two sides are really required because we are traversing the array from the right to left and from up to down.
                """
                # if r + 1< rows and A[r + 1][c] == 1:
                #     dsu.union(i, index(r + 1, c))
                # if c + 1 < cols and A[r][c + 1] == 1:
                #     dsu.union(i, index(r, c + 1))

        ans = []
        for r, c in reversed(hits):
            if grid[r][c] == 0:
                ans.append(0)
            else:
                old = dsu.top()
                if r == 0:
                    dsu.union(rows * cols, index(r, c))
                for nr, nc in neighbours(r, c):
                    if A[nr][nc] == 1:
                        dsu.union(index(r, c), index(nr, nc))
                ans.append(max(0, dsu.top() - old - 1))
                A[r][c] = 1
        return list(reversed(ans))

    # def hitBricks(self, grid, hits):
    #     rows, cols = len(grid), len(grid[0])
    #     degrees = [[set() for _ in range(cols)] for _ in range(rows)]
    #
    #     for i in range(cols):
    #         if grid[0][i] == 0 or grid[1][i] == 0:
    #             continue
    #         visited = [[False] * cols for _ in range(rows)]
    #         degrees[1][i].add((0, i))
    #         queue = [(1, i)]
    #
    #         while queue:
    #             popped = queue.pop(0)
    #             r, c = popped[0], popped[1]
    #             visited[r][c] = True
    #
    #             for nr, nc in [(r, c - 1), (r + 1, c), (r, c + 1)]:
    #                 if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and not visited[nr][nc]:
    #                     visited[nr][nc] = True
    #                     degrees[nr][nc].add((r, c))
    #                     queue.append((nr, nc))
    #
    #     fall_count = []
    #     for r, c in hits:
    #         if grid[r][c] == 0:
    #             fall_count.append(0)
    #             continue
    #         visited = [[False] * cols for _ in range(rows)]
    #         queue = [(r, c)]
    #         grid[r][c] = 0
    #         counter = 0
    #         while queue:
    #             popped = queue.pop(0)
    #             r, c = popped[0], popped[1]
    #             visited[r][c] = True
    #
    #             for nr, nc in [(r, c - 1), (r + 1, c), (r, c + 1)]:
    #                 if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and not visited[nr][nc]:
    #                     visited[nr][nc] = True
    #                     if (r, c) in degrees[nr][nc]:
    #                         degrees[nr][nc].remove((r, c))
    #                     if len(degrees[nr][nc]) == 0:
    #                         grid[nr][nc] = 0
    #                         counter += 1
    #                         queue.append((nr, nc))
    #
    #         fall_count.append(counter)
    #     return fall_count

    # def hitBricks(self, grid, hits):
    #     rows, cols = len(grid), len(grid[0])
    #
    #     fall_count = []
    #     for r, c in hits:
    #         if grid[r][c] == 0:
    #             fall_count.append(0)
    #             continue
    #
    #         grid[r][c] = 0
    #         visited = [[False]*cols for _ in range(rows)]
    #         visited[r][c] = True
    #
    #         def dfs(r, c):
    #             stable = grid[r][c] == 1 and (r == 0 or (r - 1 == 0 and grid[r - 1][c] == 1))
    #             if stable:
    #                 return 0
    #
    #             counter = 0
    #             leaf = True
    #             for nr, nc in [(r, c - 1), (r, c + 1), (r + 1, c)]:
    #                 if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and not visited[nr][nc]:
    #                     leaf = False
    #                     visited[nr][nc] = True
    #                     nodes_removed = dfs(nr, nc)
    #                     counter += nodes_removed
    #
    #             if counter > 0 or leaf:
    #                 removed_count = counter + (1 if grid[r][c] == 1 else 0)
    #                 grid[r][c] = 0
    #                 return removed_count
    #             return 0
    #
    #         fall_count.append(dfs(r, c))
    #     return fall_count


if __name__ == '__main__':
    print(Solution().hitBricks([[0,1,1,1],[0,0,0,1],[0,1,1,1],[1,1,0,0]], [[2,1]]))  # [2]
    # print(Solution().hitBricks([[1, 0, 1], [1, 1, 1]], [[0, 0], [0, 2], [1, 1]]))  # [0, 3, 0]
    # print(Solution().hitBricks([[1, 1, 1], [0, 1, 0], [0, 0, 0]], [[0, 2], [2, 0], [0, 1], [1, 2]]))  # [0, 0, 1, 0]
    # print(Solution().hitBricks(
    #     [[0, 1, 1, 1, 1], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0], [0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0],
    #      [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
    #     [[1, 0], [4, 3], [1, 2], [7, 1], [6, 3], [5, 2], [5, 1], [2, 4], [4, 4],
    #      [7, 3]]))  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # print(Solution().hitBricks(
    #     [[1, 1, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
    #     [[5, 1], [1, 3]]))  # [0, 4]
    # print(Solution().hitBricks(grid=[[1, 0, 0, 0], [1, 1, 1, 0]], hits=[[1, 0]]))  # [2]
    # print(Solution().hitBricks(
    #     [[0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]],
    #     [[1, 3], [3, 5], [0, 3], [3, 3], [1, 1], [4, 2], [1, 0], [3, 0], [4, 5], [2, 1], [4, 4], [4, 0], [2, 4], [2, 5],
    #      [3, 4], [0, 5], [0, 4], [3, 2], [1, 5], [4, 1], [2, 2], [0, 2]]))  # [2]
