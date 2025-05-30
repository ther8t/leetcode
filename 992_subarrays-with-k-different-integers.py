import collections


class Solution:
    def subarraysWithKDistinct(self, nums, k: int) -> int:
        if not nums:
            return 0

        def numSubarraysWithSumAtMost(goal):
            l = 0
            counter = collections.defaultdict(int)

            ans = 0
            for r in range(len(nums)):
                counter[nums[r]] += 1
                while len(counter) > goal and l < r:
                    counter[nums[l]] -= 1
                    if counter[nums[l]] == 0:
                        del counter[nums[l]]
                    l += 1
                ans += r - l + 1 if len(counter) <= goal else 0

            return ans

        return numSubarraysWithSumAtMost(k) - numSubarraysWithSumAtMost(k - 1)


if __name__ == '__main__':
    print(Solution().subarraysWithKDistinct(nums = [1,2,1,2,3], k = 2))
    print(Solution().subarraysWithKDistinct(nums = [1,2,1,3,4], k = 3))
