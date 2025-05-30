import heapq


class Solution:
    def minPushBox(self, grid) -> int:
        rows, cols = len(grid), len(grid[0])
        target, box, shopkeeper = (0, 0), (0, 0), (0, 0)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "T":
                    target = (r, c)
                elif grid[r][c] == "B":
                    box = (r, c)
                elif grid[r][c] == "S":
                    shopkeeper = (r, c)

        box_visited = set()

        def manhattan_distance(point1, point2):
            return abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])

        def dfs(r, c):
            if (r, c) == shopkeeper_destination:
                return True
            visited[r][c] = True
            for nr, nc in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#' and (nr, nc) != box_position and not visited[nr][nc]:
                    visited[nr][nc] = True
                    if dfs(nr, nc):
                        return True
            return False

        queue = [(0, manhattan_distance(box, target), box, shopkeeper)]

        while queue:
            moves, m_distance, box_position, shopkeeper_position = heapq.heappop(queue)
            r, c = box_position
            for dr, dc, direction in [(-1, 0, 'u'), (0,  -1, 'l'), (1, 0, 'd'), (0, 1, 'r')]:
                nr, nc = r + dr, c + dc
                visited = [[False] * cols for _ in range(rows)]
                visited[shopkeeper_position[0]][shopkeeper_position[1]] = True
                shopkeeper_destination = (r - dr, c - dc)
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#' and (nr, nc, direction) not in box_visited and 0 <= r - dr < rows and 0 <= c - dc < cols and grid[r - dr][c - dc] != '#' and dfs(shopkeeper_position[0], shopkeeper_position[1]):
                    if (nr, nc) == target:
                        return moves + 1
                    box_visited.add((nr, nc, direction))
                    heapq.heappush(queue, (moves + 1, manhattan_distance((nr, nc), target), (nr, nc), shopkeeper_destination))

        return -1



    # # Wrong Answer : I didn't consider that the box could not move in certain cases.
    # def minPushBox(self, grid) -> int:
    #     rows, cols = len(grid), len(grid[0])
    #     target, box, shopkeeper = (0, 0), (0, 0), (0, 0)
    #     for r in range(rows):
    #         for c in range(cols):
    #             if grid[r][c] == "T":
    #                 target = (r, c)
    #             elif grid[r][c] == "B":
    #                 box = (r, c)
    #             elif grid[r][c] == "S":
    #                 shopkeeper = (r, c)
    #
    #     visited = [[False] * cols for _ in range(rows)]
    #
    #     visited[box[0]][box[1]] = True
    #     paths = []
    #
    #     def backtrack(r, c, stack):
    #         if (r, c) == target:
    #             paths.append(stack)
    #             return
    #         for nr, nc, direction in [(r - 1, c, 'u'), (r, c - 1, 'l'), (r + 1, c, 'd'), (r, c + 1, 'r')]:
    #             if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#' and grid[nr][nc] != 'B' and not visited[nr][nc]:
    #                 visited[nr][nc] = True
    #                 backtrack(nr, nc, stack + [direction])
    #                 visited[nr][nc] = False
    #
    #     def dfs(r, c):
    #         if (r, c) == shopkeeper_target:
    #             return True
    #         visited[r][c] = True
    #         for nr, nc in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
    #             if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#' and (nr, nc)!=box_position and not visited[nr][nc]:
    #                 visited[nr][nc] = True
    #                 if dfs(nr, nc):
    #                     return True
    #         return False
    #
    #     backtrack(box[0], box[1], [])
    #     paths.sort(key=len)
    #     for path in paths:
    #         box_position = box
    #         is_path_valid = True
    #         for d in path:
    #             push_map = {"u": (-1, 0), "l": (0, -1), "d": (1, 0), "r": (0, 1)}
    #             shopkeeper_target = (box_position[0] - push_map[d][0], box_position[1] - push_map[d][1])
    #             if 0 > shopkeeper_target[0] >= rows or 0 > shopkeeper_target[1] >= cols or grid[shopkeeper_target[0]][shopkeeper_target[1]] == '#':
    #                 is_path_valid = False
    #                 break
    #             shopkeeper_source = shopkeeper
    #             visited = [[False] * cols for _ in range(rows)]
    #
    #             if not dfs(shopkeeper_source[0], shopkeeper_source[1]):
    #                 is_path_valid = False
    #                 break
    #             box_position = (box_position[0] + push_map[d][0], box_position[1] + push_map[d][1])
    #         if is_path_valid:
    #             return len(path)
    #     return -1


if __name__ == '__main__':
    print(Solution().minPushBox([["#","#",".","#",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".","T",".","#"],[".",".",".",".",".","#",".","."],[".",".",".",".",".","#",".","."],[".",".",".",".",".",".","S","."],[".",".",".","B",".",".",".","."],[".",".",".",".",".",".",".","."]]))
