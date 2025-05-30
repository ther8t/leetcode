import collections
from collections import deque
import heapq


class Solution:
    # def shortestPath(self, grid, k: int):
    #     rows, cols = len(grid), len(grid[0])
    #     visited = [[[False for _ in range(k + 1)] for _ in range(cols)] for _ in range(rows)]

    # # TLE
    # def shortestPath(self, grid, k: int):
    #     rows, cols = len(grid), len(grid[0])
    #     if rows <= 0 or cols <= 0:
    #         return 0
    #
    #     if k >= rows + cols - 2:
    #         return rows + cols - 2
    #
    #     def bfs(queue):
    #         while queue:
    #             i, j, moves_count, obstacle_count = queue.pop(0)
    #             if i == rows - 1 and j == cols - 1:
    #                 return moves_count
    #             moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    #             for dr, dc in moves:
    #                 if 0 <= i + dr < rows and 0 <= j + dc < cols and not visited[i + dr][j + dc][obstacle_count] and obstacle_count + grid[i][j] <= k:
    #                     visited[i + dr][j + dc][obstacle_count + grid[i][j]] = True
    #                     queue.append((i + dr, j + dc, moves_count + 1, obstacle_count + grid[i][j]))
    #
    #     visited = [[[False for _ in range(k + 1)] for _ in range(cols)] for _ in range(rows)]
    #     visited[0][0][k] = True
    #     queue = [(0, 0, 0, 0)]
    #     ans = bfs(queue)
    #     return ans if ans else -1


    # # A* Algorithm : Accepted
    # def shortestPath(self, grid, k: int):
    #     rows, cols = len(grid), len(grid[0])
    #     if rows <= 0 or cols <= 0:
    #         return 0
    #
    #     visited = [[[False for _ in range(k + 1)] for _ in range(cols)] for _ in range(rows)]
    #     visited[0][0][k] = True
    #
    #     if k >= rows + cols - 2:
    #         return rows + cols - 2
    #
    #     def manhattan_distance(i, j):
    #         return rows - i + cols - j
    #
    #     queue = [(0 + manhattan_distance(0, 0), 0, 0, (0, 0))]
    #
    #     while queue:
    #         estimation, moves_count, obstacle_count, (i, j) = queue.pop(0)
    #         if i == rows - 1 and j == cols - 1:
    #             return moves_count
    #         moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    #         for dr, dc in moves:
    #             next_row = i + dr
    #             next_col = j + dc
    #             if 0 <= next_row < rows and 0 <= next_col < cols and not visited[next_row][next_col][
    #                 obstacle_count] and obstacle_count + grid[i][j] <= k:
    #                 visited[next_row][next_col][obstacle_count + grid[i][j]] = True
    #                 heapq.heappush(queue, (
    #                     moves_count + 1 + manhattan_distance(next_row, next_col), moves_count + 1,
    #                     obstacle_count + grid[i][j],
    #                     (next_row, next_col)))
    #
    #     return -1

    # # TLE
    # def shortestPath(self, grid, k: int):
    #     if len(grid) <= 0 or len(grid[0]) <= 0:
    #         return 0
    #
    #     gridMarker = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    #     dp = [[(float('inf'), 0) for _ in range(len(grid[0]))] for _ in range(len(grid))]
    #
    #     def bestMove(row, col, k):
    #         if row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[0]) - 1:
    #             # reached edge
    #             return (float('inf'), 0)
    #         if gridMarker[row][col] == -1:
    #             # hit already visited or processing node.
    #             return (float('inf'), 0)
    #         if row == len(grid) - 1 and col == len(grid[0]) - 1:
    #             # you win
    #             return (0, 0)
    #         if grid[row][col] == 1 and k < 0:
    #             # got obstacle which can't be eliminated
    #             return (float('inf'), 0)
    #
    #         # minStepsStored = float('inf')
    #         # for ks in dp[row][col].keys():
    #         #     if k >= ks and dp[row][col][ks] < minStepsStored:
    #         #         minStepsStored = dp[row][col][ks]
    #         # if minStepsStored != float('inf'):
    #         #     print(f"Stored {row}, {col}, {minStepsStored}, {k}")
    #         #     return minStepsStored
    #         if dp[row][col][0] != float('inf') and k == dp[row][col][1]:
    #             print(f"Found at {row}, {col}, {dp[row][col]}")
    #             return dp[row][col]
    #
    #         gridMarker[row][col] = -1
    #
    #         if row == 2 and col == 2:
    #             print("Jey hude")
    #         moveUp = moveDown = moveLeft = moveRight = float('inf')
    #         moves = [(float('inf'), 0), (float('inf'), 0), (float('inf'), 0), (float('inf'), 0)]
    #         if row + 1 < len(grid):
    #             # down
    #             if row == 2 and col == 2:
    #                 print("Jey hude")
    #             minSteps, eliminationsNeeded = bestMove(row + 1, col, k) if grid[row + 1][col] == 0 else bestMove(
    #                 row + 1, col, k - 1)
    #             moves[1] = (minSteps, eliminationsNeeded) if grid[row + 1][col] == 0 else (
    #                 minSteps, eliminationsNeeded + 1)
    #         if col - 1 >= 0:
    #             # left
    #             if row == 2 and col == 2:
    #                 print("Jey hude")
    #             minSteps, eliminationsNeeded = bestMove(row, col - 1, k) if grid[row][col - 1] == 0 else bestMove(row,
    #                                                                                                               col - 1,
    #                                                                                                               k - 1)
    #             moves[2] = (minSteps, eliminationsNeeded) if grid[row][col - 1] == 0 else (
    #                 minSteps, eliminationsNeeded + 1)
    #         if col + 1 < len(grid[0]):
    #             # right
    #             if row == 2 and col == 2:
    #                 print("Jey hude")
    #             minSteps, eliminationsNeeded = bestMove(row, col + 1, k) if grid[row][col + 1] == 0 else bestMove(row,
    #                                                                                                               col + 1,
    #                                                                                                               k - 1)
    #             moves[3] = (minSteps, eliminationsNeeded) if grid[row][col + 1] == 0 else (
    #                 minSteps, eliminationsNeeded + 1)
    #         if row - 1 >= 0:
    #             # up
    #             if row == 2 and col == 2:
    #                 print("Jey hude")
    #             minSteps, eliminationsNeeded = bestMove(row - 1, col, k) if grid[row - 1][col] == 0 else bestMove(
    #                 row - 1, col, k - 1)
    #             moves[0] = (minSteps, eliminationsNeeded) if grid[row - 1][col] == 0 else (
    #                 minSteps, eliminationsNeeded + 1)
    #
    #         gridMarker[row][col] = 0
    #
    #         def sortFunc(node):
    #             return node[0]
    #
    #         moves.sort(key=sortFunc)
    #         minMove = moves[0][0]
    #         eliminationsNeeded = moves[0][1]
    #         for i in moves:
    #             if i[0] == minMove and i[1] <= eliminationsNeeded:
    #                 minMove = i[0]
    #                 eliminationsNeeded = i[1]
    #
    #         if dp[row][col][0] > minMove + 1:
    #             dp[row][col] = (minMove + 1, eliminationsNeeded)
    #         return dp[row][col]
    #
    #     leastPath, eliminationsNeeded = bestMove(0, 0, k)
    #     print(dp)
    #     return leastPath if leastPath != float('inf') else -1


    """
    Revision 2 :
    This solution is the basic BFS and this TLEs. I have to figure out a better way to solve this.
    The A* algorithm is much faster. The two advantages it has over the simple BFS is that it prioritized the favorable solutions over the unfavorable ones.
    This means that instead of running the queue till the end the first one to reach the target is the output for the minimum or the maximum. This saves time and computation.
    However and this is a mistake I made. Choice of heuristic is important. I made the choice of (score, manhattan distance) as a heuristic, which doesn't run as well as "score + manhattan_distance".
    """
    def shortestPath(self, grid, k: int):
        rows, cols = len(grid), len(grid[0])
        if k >= rows + cols - 2:
            return rows - 1 + cols - 1
        target = (0, 0)
        visited = set()
        queue = []
        heapq.heappush(queue, (0 + rows - 1 + cols - 1, 0, k, rows - 1, cols - 1))
        visited.add((rows - 1, cols - 1, k))

        while queue:
            h, score, k, r, c = heapq.heappop(queue)
            if (r, c) == target:
                return score

            for nr, nc in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == 1 and k and (nr, nc, k) not in visited:
                        visited.add((nr, nc, k - 1))
                        heapq.heappush(queue, (score + 1 + nr + nc, score + 1, k - 1,  nr, nc))
                    elif grid[nr][nc] == 0 and (nr, nc, k) not in visited:
                        visited.add((nr, nc, k))
                        heapq.heappush(queue, (score + 1 + nr + nc, score + 1, k, nr, nc))

        return -1







if __name__ == '__main__':
    print(Solution().shortestPath([[0,1,0,0,0,0],[0,1,0,1,1,0],[0,1,0,1,1,0],[0,1,0,1,1,0]], 1))
    print(Solution().shortestPath(grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1))
    print(Solution().shortestPath([[0,0,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,1],[0,1,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,1],[0,1,0,1,1,1,1,0,0,0],[0,1,0,0,0,0,0,0,1,0],[0,1,1,1,1,1,1,0,1,0],[0,0,0,0,0,0,0,0,1,0]], 1))
