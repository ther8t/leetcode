class Solution:

    # # TLE 80/85
    # def shortestDistance(self, grid) -> int:
    #     rows, cols = len(grid), len(grid[0])
    #     queue = []
    #     visited = [[set() for _ in range(cols)] for _ in range(rows)]
    #     distances = [[0] * cols for _ in range(rows)]
    #
    #     one_count = 0
    #     for r in range(rows):
    #         for c in range(cols):
    #             if grid[r][c] == 1:
    #                 queue.append((0, (r, c), (r, c)))
    #                 one_count += 1
    #
    #     min_distance = float('inf')
    #     end_distance = float('inf')
    #     while queue and queue[0][0] < end_distance:
    #         d, source, current = queue.pop(0)
    #         r, c = current
    #         for nr, nc in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
    #             if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and source not in visited[nr][nc]:
    #                 visited[nr][nc].add(source)
    #                 distances[nr][nc] += d + 1
    #                 if len(visited[nr][nc]) == one_count:
    #                     min_distance = min(min_distance, distances[nr][nc])
    #                     end_distance = min(end_distance, d + 1)
    #                 queue.append((d + 1, source, (nr, nc)))
    #
    #     return -1 if min_distance == float('inf') else min_distance

    def shortestDistance(self, grid) -> int:
        rows, cols = len(grid), len(grid[0])
        buildings_counter = [[0]*cols for _ in range(rows)]
        moves = [[0]*cols for _ in range(rows)]
        total_buildings = 0
        buildings_discovered = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    total_buildings += 1
                    queue = [((row, col), 0)]
                    visited = set()
                    while queue:
                        (r, c), distance = queue.pop(0)
                        for nr, nc in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == buildings_discovered and (nr, nc) not in visited:
                                visited.add((nr, nc))
                                grid[nr][nc] = buildings_discovered - 1
                                buildings_counter[nr][nc] += 1
                                moves[nr][nc] += (distance + 1)
                                queue.append(((nr, nc), distance + 1))
                    buildings_discovered -= 1

        min_distance = float('inf')
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] not in [1, 2] and buildings_counter[row][col] == total_buildings:
                    min_distance = min(moves[row][col], min_distance)

        return min_distance if min_distance != float('inf') else -1

    # # TLE
    # def shortestDistance(self, grid) -> int:
    #     rows, cols = len(grid), len(grid[0])
    #     buildings_counter = [[0]*cols for _ in range(rows)]
    #     moves = [[0]*cols for _ in range(rows)]
    #     total_buildings = 0
    #
    #     for row in range(rows):
    #         for col in range(cols):
    #             if grid[row][col] == 1:
    #                 total_buildings += 1
    #                 queue = [((row, col), 0)]
    #                 visited = set()
    #                 while queue:
    #                     (r, c), distance = queue.pop(0)
    #                     for nr, nc in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
    #                         if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
    #                             visited.add((nr, nc))
    #                             buildings_counter[nr][nc] += 1
    #                             moves[nr][nc] += (distance + 1)
    #                             queue.append(((nr, nc), distance + 1))
    #
    #     min_distance = float('inf')
    #     for row in range(rows):
    #         for col in range(cols):
    #             if grid[row][col] == 0 and buildings_counter[row][col] == total_buildings:
    #                 min_distance = min(moves[row][col], min_distance)
    #
    #     return min_distance if min_distance != float('inf') else -1


    # # TLE : Much too complicated Solution. But it explores some interesting ways to tackle the problem. Must read this as well.
    # # The idea is to get the paths from a single source to all the buildings and store it. These paths are then updated with each move along 0's using bfs
    # def shortestDistance(self, grid) -> int:
    #     rows, cols = len(grid), len(grid[0])
    #     buildings = []
    #     blocks = []
    #
    #     for r in range(rows):
    #         for c in range(cols):
    #             if grid[r][c] == 1:
    #                 buildings.append((r, c))
    #             elif grid[r][c] == 2:
    #                 blocks.append((r, c))
    #
    #     def manhattan_distance(point1, point2):
    #         return abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])
    #
    #     def new_directions(moves, new_direction_moved):
    #         opposites = {"u": "d", "d": "u", "l": "r", "r": "l"}
    #         if new_direction_moved == moves[0]:
    #             return moves[1:]
    #         else:
    #             if len(moves) > 1 and new_direction_moved == moves[1]:
    #                 return [moves[0]] + moves[2:]
    #             else:
    #                 return [opposites[new_direction_moved]] + moves
    #
    #     def bfs(source, target):
    #         queue = [(source, [])]
    #         visited = set()
    #         visited.add(source)
    #         while queue:
    #             popped, moves = queue.pop(0)
    #
    #             r, c = popped
    #             for nr, nc, direction in [(r - 1, c, "u"), (r, c - 1, "l"), (r + 1, c, "d"), (r, c + 1, "r")]:
    #                 if (nr, nc) == target:
    #                     return moves + [direction]
    #                 elif 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
    #                     visited.add((nr, nc))
    #                     queue.append(((nr, nc), moves + [direction]))
    #         return None
    #
    #     source = None
    #     visited = set()
    #     buildings_visited = set()
    #     for r in range(rows):
    #         if source:
    #             break
    #         for c in range(cols):
    #             if grid[r][c] == 0 and (r, c) not in visited:
    #                 source = (r, c)
    #                 building_count = 0
    #
    #                 queue = [source]
    #                 visited.add(source)
    #                 while queue:
    #                     popped = queue.pop(0)
    #                     r, c = popped
    #                     for nr, nc in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
    #                         if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr, nc) not in buildings_visited:
    #                             buildings_visited.add((nr, nc))
    #                             building_count += 1
    #
    #                     for nr, nc in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
    #                         if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
    #                             visited.add((nr, nc))
    #                             queue.append((nr, nc))
    #
    #
    #                 if building_count != len(buildings):
    #                     buildings_visited = set()
    #                     source = None
    #                 else:
    #                     break
    #
    #     if not source:
    #         return -1
    #
    #     paths = []
    #     moves_sum = 0
    #     for target in buildings:
    #         moves = bfs(source, target)
    #         paths.append(moves)
    #         moves_sum += len(moves)
    #
    #     min_distance = moves_sum
    #     queue = [(source, paths)]
    #     visited = set()
    #     visited.add(source)
    #     while queue:
    #         current_source, current_paths = queue.pop(0)
    #         r, c = current_source
    #
    #         for nr, nc, direction in [(r - 1, c, "u"), (r, c - 1, "l"), (r + 1, c, "d"), (r, c + 1, "r")]:
    #             if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
    #                 visited.add((nr, nc))
    #                 new_paths = []
    #                 moves_sum = 0
    #                 for p in current_paths:
    #                     updated_path = new_directions(p, direction)
    #                     moves_sum += len(updated_path)
    #                     new_paths.append(updated_path)
    #                 if moves_sum == 9223:
    #                     print(new_paths)
    #                 min_distance = min(min_distance, moves_sum)
    #                 queue.append(((nr, nc), new_paths))
    #
    #     return min_distance if min_distance != float('inf') else -1


    # # TLE : Obviously, Duhh!!!
    # def shortestDistance(self, grid) -> int:
    #     rows, cols = len(grid), len(grid[0])
    #     buildings = []
    #     blocks = []
    #
    #     for r in range(rows):
    #         for c in range(cols):
    #             if grid[r][c] == 1:
    #                 buildings.append((r, c))
    #             elif grid[r][c] == 2:
    #                 blocks.append((r, c))
    #
    #     def manhattan_distance(point1, point2):
    #         return abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])
    #
    #     def new_directions(moves, new_direction_moved):
    #         opposites = {"u": "d", "d": "u", "l": "r", "r": "l"}
    #         if new_direction_moved == moves[0]:
    #             return moves[1:]
    #         else:
    #             if len(moves) > 1 and new_direction_moved == moves[1]:
    #                 return [moves[0]] + moves[2:]
    #             else:
    #                 return [opposites[new_direction_moved]] + moves
    #
    #     def bfs(source, target):
    #         queue = [(source, [])]
    #         visited = set()
    #         visited.add(source)
    #         while queue:
    #             popped, moves = queue.pop(0)
    #
    #             r, c = popped
    #             for nr, nc, direction in [(r - 1, c, "u"), (r, c - 1, "l"), (r + 1, c, "d"), (r, c + 1, "r")]:
    #                 if (nr, nc) == target:
    #                     return moves + [direction]
    #                 elif 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
    #                     visited.add((nr, nc))
    #                     queue.append(((nr, nc), moves + [direction]))
    #         return None
    #
    #     min_distance = float('inf')
    #     for r in range(rows):
    #         for c in range(cols):
    #             if grid[r][c] == 0:
    #                 distance = 0
    #                 source = (r, c)
    #                 for target in buildings:
    #                     moves = bfs(source, target)
    #                     if moves:
    #                         distance += len(moves)
    #                     else:
    #                         distance = float('inf')
    #                         break
    #                 min_distance = min(min_distance, distance)
    #
    #     return min_distance if min_distance != float('inf') else -1






# # Wrong Answer : This code was done to check a few unwritten/questionable assumptions.
    # def shortestDistance(self, grid) -> int:
    #     rows, cols = len(grid), len(grid[0])
    #     buildings = []
    #     blocks = []
    #
    #     for r in range(rows):
    #         for c in range(cols):
    #             if grid[r][c] == 1:
    #                 buildings.append((r, c))
    #             elif grid[r][c] == 2:
    #                 blocks.append((r, c))
    #
    #     def manhattan_distance(point1, point2):
    #         return abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])
    #
    #     min_distance = float('inf')
    #     for r in range(rows):
    #         for c in range(cols):
    #             if grid[r][c] == 0:
    #                 distance = 0
    #                 for br, bc in buildings:
    #                     distance += manhattan_distance((r, c), (br, bc))
    #                 min_distance = min(min_distance, distance)
    #
    #     return min_distance if min_distance != float('inf') else -1


if __name__ == '__main__':
    print(Solution().shortestDistance(grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]])) #7
    print(Solution().shortestDistance(grid = [[1,0]]))
    print(Solution().shortestDistance(grid = [[1,2,0]]))
    print(Solution().shortestDistance(grid = [[1]]))
    print(Solution().shortestDistance(grid = [[1,1,1,1,1,0],[0,0,0,0,0,1],[0,1,1,0,0,1],[1,0,0,1,0,1],[1,0,1,0,0,1],[1,0,0,0,0,1],[0,1,1,1,1,0]])) #88
    print(Solution().shortestDistance(grid = [[2,2,2,2,0,2,2,0,0,0,2,0,0,0,0,0,0,0,0,0,2,2,0,1,0,0,0,0,0,2,2,2,0,0,0,0,0,2,2,2,0,2,0,0],[0,0,2,2,0,0,0,2,0,0,2,2,0,0,0,0,2,0,2,1,0,2,0,1,2,2,2,0,0,2,0,2,2,0,0,0,0,2,2,0,2,1,2,0],[1,0,0,0,0,2,2,0,0,2,0,0,1,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,0,1,0,0,2,0,2,2,2,0,2,0,2,2,0],[1,0,2,0,0,2,0,0,2,0,0,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,2,0,0,2,0,0,0,0,2,0,0,0,0,0,0,0],[0,0,2,0,0,0,0,0,0,0,2,0,2,0,1,0,2,2,2,0,0,0,2,2,2,2,2,0,0,0,0,0,0,0,2,0,2,0,1,0,2,2,0,2],[2,0,0,0,0,2,0,0,2,2,2,2,0,0,2,2,2,0,0,0,0,2,0,0,0,0,2,0,2,0,2,0,1,2,0,2,2,0,0,0,2,0,0,2],[0,0,0,2,2,2,0,2,0,0,0,2,0,0,2,0,2,0,2,0,0,2,0,2,0,1,0,2,2,0,0,2,0,0,0,2,2,2,2,0,0,0,2,0],[2,0,0,2,0,2,2,2,2,0,0,2,2,0,2,0,0,0,1,2,0,2,2,0,2,0,2,1,2,0,1,0,2,1,2,0,0,0,0,0,0,0,2,2],[0,0,2,2,0,2,0,0,0,2,0,2,0,2,2,0,2,0,0,0,0,0,0,0,2,0,0,2,1,2,0,0,0,2,1,0,2,2,2,0,0,0,2,0],[2,0,0,0,0,2,0,0,2,2,2,2,0,2,0,0,2,0,0,0,0,2,0,0,0,0,0,2,1,0,0,2,2,2,1,2,2,0,0,0,0,0,2,2],[0,1,0,2,0,0,2,0,0,2,0,0,0,0,0,0,1,2,0,2,2,2,2,0,0,2,2,2,0,2,0,2,2,2,0,0,2,0,0,0,0,0,2,2],[0,2,0,0,0,2,0,2,2,2,0,0,1,2,0,0,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,2,0,0,2],[2,2,2,2,2,2,0,0,0,0,0,2,0,2,2,2,0,2,0,2,0,2,2,0,2,0,0,0,2,0,0,2,2,2,2,2,0,0,0,2,0,2,2,0],[0,0,2,0,2,2,0,0,0,0,0,0,2,2,0,2,0,2,2,0,0,0,0,0,2,2,1,0,0,1,2,0,2,0,0,0,0,2,0,2,0,2,0,0],[0,2,2,0,0,0,0,2,0,0,0,2,0,2,2,0,0,2,0,0,0,0,0,2,0,0,0,0,0,2,0,0,0,0,2,0,0,0,0,2,0,2,0,0],[0,0,0,0,0,2,2,0,2,2,0,0,0,2,2,2,0,2,2,0,2,0,2,0,2,2,0,1,0,2,0,2,0,0,2,0,0,0,0,0,0,2,0,2],[2,2,0,2,0,0,1,2,0,1,0,2,0,0,2,0,1,2,1,2,2,0,2,0,0,0,0,2,2,2,0,2,0,2,0,2,0,0,0,0,0,0,0,2],[0,2,2,0,2,0,0,1,0,0,0,0,2,0,0,0,0,0,2,2,0,2,0,0,2,0,0,0,0,0,2,0,0,2,0,0,0,0,0,2,2,0,2,2],[0,2,2,0,0,2,2,0,2,0,0,0,0,0,2,2,0,0,0,2,2,2,1,0,2,2,0,2,0,0,2,0,0,0,1,2,0,2,2,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0,0,0,2,0,0,0,2,2,2,0,0,0,2,2,1,0,0,2,2,0,2,0,2,0,1,0,2,0,0,0,0,2,0,2],[0,0,2,2,0,0,2,0,2,0,2,2,0,0,2,0,0,0,0,0,0,2,0,0,0,0,0,0,2,0,0,2,0,0,2,0,2,0,0,0,0,0,0,0],[0,2,2,2,2,0,0,2,0,0,2,2,0,0,0,2,0,0,2,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,1,2],[2,2,2,0,0,2,0,0,0,0,0,2,0,0,2,2,0,0,2,0,2,0,0,0,2,0,2,2,0,0,0,2,2,0,0,2,0,0,2,0,2,2,0,2],[2,0,0,2,2,2,0,0,0,2,2,0,0,0,0,0,2,0,0,0,0,0,2,0,0,2,0,1,0,1,0,0,2,0,2,0,2,0,2,1,0,2,0,0],[2,0,0,2,2,0,0,0,0,0,2,0,0,0,2,2,2,0,0,2,0,0,2,0,0,2,2,2,2,2,2,0,0,0,2,0,0,2,2,1,0,0,0,2],[1,0,2,0,2,0,0,2,0,0,0,2,0,1,0,0,2,2,0,0,2,0,2,0,2,2,0,0,0,2,0,0,0,0,2,2,2,2,0,2,2,2,0,2],[0,0,0,0,2,2,2,0,0,1,0,2,2,2,0,0,0,1,2,0,0,0,2,0,0,0,0,0,2,0,2,0,0,0,0,0,2,0,0,1,0,0,0,2],[0,2,2,0,2,0,2,1,2,2,1,0,0,0,0,0,0,0,0,0,0,0,2,2,2,0,2,2,2,0,0,2,0,2,0,2,0,0,0,2,0,0,0,0],[0,2,2,0,2,2,0,2,2,0,0,0,1,2,2,0,0,2,0,0,2,2,2,0,2,2,2,0,2,0,0,0,2,2,0,0,0,0,2,2,0,2,2,2],[0,0,2,0,0,0,1,2,0,2,2,2,0,0,2,2,0,0,0,2,0,0,2,0,0,2,2,2,0,2,2,0,0,0,0,2,0,0,0,0,0,0,2,2]]))
    print(Solution().shortestDistance(grid = [[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,2,1,0,0,2,0,0,0,0,0,1,2,0,0,0,0,0,1,2,0,0,0,0,0,0,0,0,1,0,0,2,1,2,0,0],[0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,2,1,0,2,0,0,2,0,0,0,1,1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,2,2,0,0,1,2,1,0,0,0,0,0,2,0,2,1,0,0,0,0,0,0,0],[0,1,0,0,1,0,0,0,0,0,0,0,2,0,0,2,0,0,0,0,0,0,1,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,1,0,0,0,2,0,2,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,2,1,0],[2,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,2,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[1,0,2,0,0,1,0,0,2,0,0,1,0,0,0,1,0,0,0,2,0,2,0,0,0,0,0,0,2,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1,0,0,2,0,0],[0,2,0,1,0,0,0,1,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,2,0,0,0,0,0,2,0,0,0,0,1,0,0,0,0,2,0,0,0,0,0,1,0,0,0,0,0,0,0,0,2,0,1,0,0,0,0,0,0,0,0,0],[2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,2,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,2,0,0,0,0,0],[0,0,0,2,0,0,0,2,0,1,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,2,0,2,0,0,1,0,0,0,1,2,0,0,0,0,0,0,1],[1,0,0,0,0,1,1,2,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,0,0,2,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,2,2,0,0,0,0,2,0,1,1,0,0],[0,2,0,0,0,1,1,0,0,0,2,0,0,0,0,0,0,0,0,1,0,1,0,0,0,2,1,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0],[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,1,0,0,0,0,0,0,0,0,1,0,0,0,2,0,0,1,2,0,0,0,2,0,0,1],[0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,2,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,2,0,0,0,0,0,2],[0,2,0,2,0,2,0,0,0,0,0,0,0,0,1,2,0,0,0,0,0,0,1,0,1,0,0,2,0,0,1,0,1,0,0,0,0,0,0,0,1,0,2,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1,0,0,1,2,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,2,0,2,0,0,0,1,0,2,0,0,0,0,0,1,2,2,0,0,0,0],[0,0,2,0,0,0,0,0,0,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,2],[0,0,1,0,0,0,1,0,2,0,0,0,0,0,0,0,0,0,0,2,0,1,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,2,0,0,0,0,2,0,0,0,0,0,0],[0,0,0,0,1,2,0,0,0,0,0,1,2,0,0,0,2,0,1,0,0,2,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0],[0,2,0,1,0,0,0,2,2,2,0,0,0,0,0,0,0,0,1,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,2,0,1,0,0,0,0,0,2,0,1,2,0,0,0,0,0,0,2,0,0,0,0,2,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],[2,0,0,0,2,1,2,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,2,0,2,0,2,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[0,2,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,1,2,0,0,0,0,0,1,0,0,0,0,0,0,0,2,0,0],[0,0,2,0,0,1,1,0,0,0,0,0,0,0,0,0,0,2,0,1,0,0,2,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,2],[1,0,0,2,1,0,0,0,0,0,0,0,2,1,0,0,0,0,0,2,0,0,0,0,2,0,0,0,0,0,1,0,0,0,0,2,0,0,0,0,0,1,0,1,0,0,0,0,0,2],[2,0,0,0,1,0,0,0,2,0,0,0,2,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,2,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,1,0,0,2,0,1,0,0,1,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,1,0,2,0,0,0,0,0,1,2,0,0,1,0],[1,0,0,0,0,0,0,0,2,0,2,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,2,2,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,2,0,0,0,2,0,0,0,1,0,0,2,0,1,2],[0,2,0,0,0,0,0,0,0,0,1,0,0,0,0,0,2,0,1,0,0,0,0,0,2,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,2,1,0,0,0],[0,0,0,0,0,0,0,0,2,0,0,0,0,0,1,0,0,0,0,0,0,2,1,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0],[0,1,0,0,0,0,0,0,2,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,2,2,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,2,1,1,0,0,1,0,0,0,0,0,0,0,0,2,0,2,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0],[0,0,1,0,1,0,0,0,2,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,2,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,0,0,0,0,2,0,0,0,0,0,1,0,0],[0,0,0,0,2,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,0,1,2,0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,2,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1,2,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,2,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,2,0,0,1,0,0,0,0,0,2,0,0,1,0,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,2,2,0,2,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,2,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,2,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,1,0,0,0,0,0,1,1,2,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,2,0,0,2,0,0,0,2,0,0,0,0,0,2,0,2,0,0],[0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,2,0,0,1,0,0,2,2,0,0,2,0,0,0,1,1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,1,0,0,1,2,0,0,2,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,1,0,0,2,0],[0,0,0,0,0,2,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,2,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,0,2,0,0,0,0,0,0,0],[0,0,0,0,2,0,0,0,1,1,0,0,0,0,0,0,2,0,0,2,0,0,0,1,1,0,0,0,0,2,0,0,2,0,2,0,2,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0,2,0,0,2,0,1]])) #6321
