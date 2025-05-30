import heapq
"""
This question is most similar to 1631_path-with-minimum-effort.
Again a couple of ways to solve this question.
1. A-Star Algo
2. Binary Guess
3. Kruskal Using DSU.

I am solving this question because I want to revise DSU majorly. Plus I would also get a practice for Kruskal.
"""

class DSU:
    def __init__(self, length):
        self.representative = [i for i in range(length)]

    def find(self, a):
        if self.representative[a] != a:
            self.representative[a] = self.find(self.representative[a])
        return self.representative[a]

    def combine(self, a, b):
        self.representative[self.find(b)] = self.find(a)


class Solution:
    """
    Revision 2:
    This is a slightly different way to solve the problem. The logic and everything remains the same but with a slight alteration in how we loop. I must say that this is a bit slower than the previous version, I know not how.
    In the previous iteration I tried to take a pairs of numbers with max between them being the sorting key.

    In the second approach I take just the number itself and connect it to the lower points. This leads to some of the extra iterations and perhaps that is why it's slow. But it is easier to explain and more understandable.
    This approach is more like the A* approach though. We use the same heap and iterate over the same neighbours. It's just the queue changes.
    But the best solution of all of this still A* algo. Use that whenever you can.
    """
    def swimInWater(self, grid) -> int:
        rows, cols = len(grid), len(grid[0])
        target_index = rows * cols - 1

        def index(r, c):
            return r * cols + c

        def expand_index(i):
            return i // cols, i % cols

        dsu = DSU((rows) * (cols))

        queue = []

        for r in range(rows):
            for c in range(cols):
                heapq.heappush(queue, (grid[r][c], r, c, index(r, c)))

        max_min_elevation = max(grid[0][0], grid[rows - 1][cols - 1])
        while queue and dsu.find(0) != dsu.find(target_index):
            elevation, r, c, dsu_index = heapq.heappop(queue)
            max_min_elevation = max(max_min_elevation, elevation)

            for nr, nc in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] <= elevation:
                    dsu.combine(dsu_index, index(nr, nc))

        return max_min_elevation




# class DSU:
#     def __init__(self, length):
#         self.parent = [i for i in range(length)]
#
#     def find(self, x):
#         if self.parent[x] != x:
#             self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]
#
#     def union(self, x, y):
#         xp, yp = self.find(x), self.find(y)
#         if xp == yp:
#             return
#         self.parent[xp] = yp
#
#
# class Solution:
#     def swimInWater(self, grid) -> int:
#         rows, cols = len(grid), len(grid[0])
#
#         def index(r, c):
#             return r * cols + c
#
#         def expand_index(i):
#             return i // cols, i % cols
#
#         dsu = DSU((rows) * (cols))
#
#         queue = []
#
#         for r in range(rows):
#             for c in range(cols):
#                 if r:
#                     heapq.heappush(queue, (max(grid[r][c], grid[r - 1][c]), index(r, c), index(r - 1, c)))
#                 if c:
#                     heapq.heappush(queue, (max(grid[r][c], grid[r][c - 1]), index(r, c), index(r, c - 1)))
#
#         ans = 0
#         while queue and dsu.find(0) != dsu.find(rows * cols - 1):
#             distance, element1, element2 = heapq.heappop(queue)
#             dsu.union(element1, element2)
#             e1r, e1c = expand_index(element1)
#             e2r, e2c = expand_index(element2)
#
#             ans = max(ans, grid[e1r][e1c], grid[e2r][e2c])
#
#         return ans

    # Accepted : 94%
    # def swimInWater(self, grid) -> int:
    #     rows, cols = len(grid), len(grid[0])
    #
    #     queue = []
    #     visited = [[False] * cols for _ in range(rows)]
    #     heapq.heappush(queue, (grid[0][0], (0, 0)))
    #
    #     time = -float('inf')
    #     while queue:
    #         height, (r, c) = heapq.heappop(queue)
    #         time = max(time, height)
    #         if (r, c) == (rows - 1, cols - 1):
    #             break
    #
    #         for nr, nc in [(r, c - 1), (r + 1, c), (r, c + 1), (r - 1, c)]:
    #             if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
    #                 visited[nr][nc] = True
    #                 heapq.heappush(queue, (grid[nr][nc], (nr, nc)))
    #
    #     return time


    """
    Attempt: Fired
    Accepted: 61%
    """
    def swimInWater(self, grid) -> int:
        rows, cols = len(grid), len(grid[0])
        target = (rows - 1, cols - 1)

        h = [(grid[0][0], (0, 0))]
        visited = set()
        visited.add((0, 0))

        while h:
            score, current_node = heapq.heappop(h)
            if current_node == target:
                return score

            r, c = current_node

            for nr, nc in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(h, (max(score, grid[nr][nc]), (nr, nc)))

        return -1


if __name__ == '__main__':
    # print(Solution().swimInWater([[0]]))
    print(Solution().swimInWater(grid = [[0,2],[1,3]]))
    print(Solution().swimInWater(grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))
