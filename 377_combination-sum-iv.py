import functools


class Solution:
    def combinationSum4(self, nums, target: int) -> int:

        @functools.lru_cache(None)
        def combinations(s):
            if s < 0:
                return 0
            if s == 0:
                return 1
            ans = 0
            for n in nums:
                ans += combinations(s - n)

            return ans

        return combinations(target)


if __name__ == '__main__':
    print(Solution().combinationSum4(nums = [1,2,3], target = 4))
    print(Solution().combinationSum4(nums = [9], target = 3))
