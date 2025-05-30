import functools


class Solution:
    def coinChange(self, coins, amount: int) -> int:

        @functools.lru_cache(None)
        def combinations(s):
            if s < 0:
                return float('inf')
            if s == 0:
                return 0
            ans = float('inf')
            for n in coins:
                ans = min(ans, 1 + combinations(s - n))

            return ans

        ans = combinations(amount)
        return ans if ans != float('inf') else -1


if __name__ == '__main__':
    print(Solution().coinChange(coins = [1,2,5], amount = 11))
    print(Solution().coinChange(coins = [2], amount = 3))
    print(Solution().coinChange(coins = [1], amount = 0))
