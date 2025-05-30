class Solution:
    def countServers(self, grid) -> int:
        rows, cols = len(grid), len(grid[0])
        connected = 0
        row_counter, col_counter = [0] * rows, [0] * cols
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    row_counter[r] += 1
                    col_counter[c] += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (row_counter[r] > 1 or col_counter[c] > 1):
                    connected += 1

        return connected

    # # Accepted : 36%
    # def countServers(self, grid) -> int:
    #     rows, cols = len(grid), len(grid[0])
    #
    #     def bfs(r, c):
    #         queue = [(r, c)]
    #         current_connected = 0
    #         while queue:
    #             r, c = queue.pop(0)
    #             current_connected += 1
    #             for nr in range(rows):
    #                 if 0 <= nr < rows and 0 <= c < cols and grid[nr][c] == 1:
    #                     grid[nr][c] = -1
    #                     queue.append((nr, c))
    #             for nc in range(cols):
    #                 if 0 <= r < rows and 0 <= nc < cols and grid[r][nc] == 1:
    #                     grid[r][nc] = -1
    #                     queue.append((r, nc))
    #         return current_connected
    #
    #     connected = 0
    #     for r in range(rows):
    #         for c in range(cols):
    #             if grid[r][c] == 1:
    #                 grid[r][c] = -1
    #                 current_connected = bfs(r, c)
    #                 if current_connected > 1:
    #                     connected += current_connected
    #     return connected


if __name__ == '__main__':
    print(Solution().countServers(grid = [[1,0],[0,1]]))
    print(Solution().countServers(grid = [[1,0],[1,1]]))
    print(Solution().countServers(grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]))
    print(Solution().countServers([[1,0,0,1,0],[0,0,0,0,0],[0,0,0,1,0]]))
