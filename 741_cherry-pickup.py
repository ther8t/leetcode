import bisect
import collections
import functools
import heapq


class DSU:
    def __init__(self, size):
        self.size = size
        self.parent = [i for i in range(size)]

    def union(self, a, b):
        parent_a = self.get_parent(a)
        parent_b = self.get_parent(b)
        self.parent[parent_a] = parent_b

    def get_parent(self, a):
        if self.parent[a] == a:
            return a
        self.parent[a] = self.parent[self.parent[a]]
        return self.get_parent(self.parent[a])


class Solution:
    """
    This solution doesn't work because it takes into consideration the two paths independently. It tries to optimise both separately.
    This is kind of greedy way to do it. There is a case where the best solution either way is (13 + 1) = 14, but could be (7 + 8) = 15.
    """
    def traverse(self, start, end, dirs):
        moves = [(-self.grid[start[0]][start[1]], start, [start])]
        final_stack = []
        final_score = 0
        visited = set()
        visited.add((-1, -1, start[0], start[1]))
        while moves:
            current_score, (r, c), stack = heapq.heappop(moves)
            if (r, c) == end:
                final_stack = stack
                final_score = current_score
                break
            for dr, dc in dirs:
                nr, nc = (r + dr) % self.rows, (c + dc) % self.cols
                if (r, c, nr, nc) not in visited and 0 <= nr < self.rows and 0 <= nc < self.cols and self.grid[nr][nc] != -1:
                    if (nr, nc) == end:
                        final_stack = stack + [(nr, nc)]
                        final_score = current_score - self.grid[nr][nc]
                        break
                    visited.add((r, c, nr, nc))
                    heapq.heappush(moves, (current_score - self.grid[nr][nc], (nr, nc), stack + [(nr, nc)]))

        for i, j in final_stack:
            self.grid[i][j] = 0

        return final_score

    # def traverse(self, start, end, dirs):
    #     cherry_picked = 0
    #     moves = []
    #     for r in range(self.rows):
    #         for c in range(self.cols):
    #             if self.grid[r][c] == -1:
    #                 continue
    #             for dr, dc in dirs:
    #                 nr, nc = r + dr, c + dc
    #                 if 0 <= r + dr < self.rows and 0 <= c + dc < self.cols and self.grid[nr][nc] != -1:
    #                     heapq.heappush(moves, (-(self.grid[r][c] + self.grid[nr][nc]), (r, c), (nr, nc)))
    #
    #     dsu = DSU(self.rows * self.cols)
    #     while moves:
    #         if dsu.get_parent(start) == dsu.get_parent(end):
    #             return cherry_picked
    #         score, (sr, sc), (er, ec) = heapq.heappop(moves)
    #         cherry_picked += (self.grid[sr][sc] + self.grid[er][ec])
    #         self.grid[sr][sc] = 0
    #         self.grid[er][ec] = 0
    #         dsu.union(self.c_to_i(sr, sc), self.c_to_i(er, ec))
    #
    #     return 0

    def cherryPickup(self, grid) -> int:
        self.grid = grid
        self.rows, self.cols = len(grid), len(grid[0])
        first = self.traverse((0, 0), (self.rows - 1, self.cols - 1), [(1, 0), (0, 1)])
        second = self.traverse((self.rows - 1, self.cols - 1), (0, 0), [(-1, 0), (0, -1)])
        return first + second


class Solution:
    def cherryPickup(self, grid) -> int:
        n = len(grid)
        dirs = [[(1, 0), (0, 1)], [(-1, 0), (0, -1)]]
        h = [(-grid[0][0], (0, 0), [(0, 0)])]
        global_visited = collections.defaultdict(int)

        highest_score = -1
        while h:
            current_score, current_node, visited = heapq.heappop(h)
            if current_node == (0, 0) and (n - 1, n - 1) in visited:
                highest_score = max(highest_score, -current_score)

            direction = 1 if (n - 1, n - 1) in visited else 0
            for dr, dc in dirs[direction]:
                next_node = (current_node[0] + dr, current_node[1] + dc)
                if next_node == (0, 0):
                    highest_score = max(highest_score, -current_score)
                nr, nc = next_node
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] != -1:
                    updated_score = current_score - (grid[nr][nc] if next_node not in visited else 0)
                    if global_visited[(current_node, next_node)] < -updated_score:
                        global_visited[(current_node, next_node)] = updated_score
                        heapq.heappush(h, (updated_score, next_node, visited + [next_node]))

        return highest_score

    """
    This is a difficult question to process. My earlier approaches were all BFS or binary search to find a score and see if we can improve it.
    This is a question of dp.
    The idea is to imagine two people walking to collect cherries instead of one. The equivalent of one path back would be another man walking upwards.
    Given that we only need to calculate once and not twice, halves the problem statement.
    The idea is to see how could two people on (r1, c1) and (r2, c2) reach that path. The question of duplication can be solved by checking if (r1, c1) == (r2, c2)
    """
    def cherryPickup(self, grid) -> int:
        n = len(grid)

        @functools.lru_cache(None)
        def pick(r1, c1, r2, c2):
            for i in [r1, c1, r2, c2]:
                if i < 0 or i >= n:
                    return float('-inf')

            if (r1, c1) == (0, 0) and (r2, c2) == (0, 0):
                return grid[r1][c1]

            if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')

            if r1 == r2 and c1 == c2:
                current_cherries = grid[r1][c1]
            else:
                current_cherries = grid[r1][c1] + grid[r2][c2]

            return current_cherries + max(pick(r1 - 1, c1, r2 - 1, c2), pick(r1, c1 - 1, r2, c2 - 1), pick(r1, c1 - 1, r2 - 1, c2), pick(r1 - 1, c1, r2, c2 - 1))

        ans = pick(n - 1, n - 1, n - 1, n - 1)
        return ans if ans != float('-inf') else 0


if __name__ == '__main__':
    print(Solution().cherryPickup([[0,1,-1],[1,0,-1],[1,1,1]]))
    print(Solution().cherryPickup([[1,1,-1],[1,-1,1],[-1,1,1]]))
    print(Solution().cherryPickup([[1]]))
    print(Solution().cherryPickup([[0,1,1,0,0],[1,1,1,1,0],[-1,1,1,1,-1],[0,1,1,1,0],[1,0,-1,0,0]]))
    print(Solution().cherryPickup([[1,1,1,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,1],[1,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,1,1,1]]))
    print(Solution().cherryPickup([[1,-1,1,-1,1,1,1,1,1,-1],[-1,1,1,-1,-1,1,1,1,1,1],[1,1,1,-1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[-1,1,1,1,1,1,1,1,1,1],[1,-1,1,1,1,1,-1,1,1,1],[1,1,1,-1,1,1,-1,1,1,1],[1,-1,1,-1,-1,1,1,1,1,1],[1,1,-1,-1,1,1,1,-1,1,-1],[1,1,-1,1,1,1,1,1,1,1]]))
