import collections
import heapq


class Solution:
    # TLE
    def calculateMinimumHP(self, dungeon) -> int:
        rows, cols = len(dungeon), len(dungeon[0])
        target = (rows - 1, cols - 1)

        queue = [(abs(dungeon[0][0]) if dungeon[0][0] < 0 else 0, dungeon[0][0], (0, 0))]

        while queue:
            abs_max_negative, health_sum, current_position = heapq.heappop(queue)
            if current_position == target:
                return abs_max_negative + 1

            r, c = current_position

            for dr, dc in [(1, 0), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    new_health_sum = health_sum + dungeon[nr][nc]
                    new_abs_max_negative = max(abs_max_negative, abs(new_health_sum) if new_health_sum < 0 else 0)
                    heapq.heappush(queue, (new_abs_max_negative, new_health_sum, (nr, nc)))

        return -1

    def calculateMinimumHP(self, dungeon) -> int:
        rows, cols = len(dungeon), len(dungeon[0])
        target = (rows - 1, cols - 1)

        def dfs(r, c, current_health, prev_abs_max_neg_health):
            if (r, c) == target:
                return prev_abs_max_neg_health <= mid

            for dr, dc in [(1, 0), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    new_health_sum = current_health + dungeon[nr][nc]
                    abs_max_neg_health = max(prev_abs_max_neg_health, abs(new_health_sum) if new_health_sum < 0 else 0)
                    if abs_max_neg_health <= mid:
                        can_be_reached = dfs(nr, nc, new_health_sum, abs_max_neg_health)
                        if can_be_reached:
                            return True
            return False

        lo, hi = 0, 400000
        while lo < hi:
            mid = (lo + hi) // 2
            if dfs(0, 0, dungeon[0][0], abs(dungeon[0][0]) if dungeon[0][0] < 0 else 0):
                hi = mid
            else:
                lo = mid + 1
        return hi + 1



if __name__ == '__main__':
    print(Solution().calculateMinimumHP(dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]))
    print(Solution().calculateMinimumHP(dungeon = [[0]]))
    print(Solution().calculateMinimumHP(dungeon = [[100]]))
    print(Solution().calculateMinimumHP([[-3,5]]))
    print(Solution().calculateMinimumHP([[0,0,0],[1,1,-1]]))
    print(Solution().calculateMinimumHP([[-200]]))
