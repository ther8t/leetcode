import collections
import functools
import heapq


class Solution:

    """
    Attempt: Fired
    TLE
    """
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        h = [(0, abs(y - x), x)]

        while h:
            moves, dist, number = heapq.heappop(h)

            if number == y:
                return moves

            if number % 11 == 0:
                if number // 11 == y:
                    return moves + 1
                heapq.heappush(h, (moves + 1, abs(number // 11 - y), number // 11))
            if number % 5 == 0:
                if number // 5 == y:
                    return moves + 1
                heapq.heappush(h, (moves + 1, abs(number // 5 - y), number // 5))

            if number + 1 == y:
                return moves + 1
            heapq.heappush(h, (moves + 1, abs(number + 1 - y), number + 1))

            if number - 1 == y:
                return moves - 1
            heapq.heappush(h, (moves + 1, abs(number - 1 - y), number - 1))

        return -1


    def minimumOperationsToMakeEqual(self, x: int, y: int):
        min_moves = collections.defaultdict(lambda: float('inf'))

        def dfs(number, moves):
            if number < y:
                min_moves[y] = min(min_moves[y], moves + y - number)
                return
            if min_moves[number] <= moves:
                return
            if number == y:
                min_moves[number] = moves
                return

            min_moves[number] = moves
            if number % 11 == 0:
                dfs(number // 11, moves + 1)

            if number % 5 == 0:
                dfs(number // 5, moves + 1)

            dfs(number - 1, moves + 1)

        dfs(x, 0)
        return min_moves[y]


    # def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
    #     @functools.lru_cache(None)
    #     def dfs(number, moves, max_moves):
    #         if moves > max_moves:
    #             return False
    #         if number == y:
    #             return True
    #
    #         reached = False
    #         if number % 11 == 0:
    #             reached = dfs(number // 11, moves + 1, max_moves)
    #         if reached:
    #             return True
    #
    #         if number % 5 == 0:
    #             reached = dfs(number // 5, moves + 1, max_moves)
    #         if reached:
    #             return True
    #
    #         reached = dfs(number - 1, moves + 1, max_moves)
    #         if reached:
    #             return True
    #
    #         reached = dfs(number + 1, moves + 1, max_moves)
    #         if reached:
    #             return True
    #
    #         return reached
    #
    #     lo, hi = 0, 450
    #     while lo < hi:
    #         mid = (lo + hi) // 2
    #         if dfs(x, 0, mid):
    #             hi = mid
    #         else:
    #             lo = mid + 1
    #
    #     return hi

if __name__ == '__main__':
    print(Solution().minimumOperationsToMakeEqual(26, 1))
    print(Solution().minimumOperationsToMakeEqual(x = 54, y = 2))
    print(Solution().minimumOperationsToMakeEqual(x = 25, y = 30))
    print(Solution().minimumOperationsToMakeEqual(1, 17))
    print(Solution().minimumOperationsToMakeEqual(1, 1))
    print(Solution().minimumOperationsToMakeEqual(275, 698))
