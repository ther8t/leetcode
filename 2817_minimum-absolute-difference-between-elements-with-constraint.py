import bisect

import sortedcontainers


class Solution:
    def minAbsoluteDifference(self, nums, x: int) -> int:
        n = len(nums)
        a = sortedcontainers.SortedList()

        diff = float('inf')
        for i in range(n - 1, -1, -1):
            if i - x < 0:
                break
            a.add(nums[i])
            index = bisect.bisect_left(a, nums[i - x])
            diff = min(diff, abs(nums[i - x] - a[index - 1]) if 0 <= index - 1 < len(a) else float('inf'), abs(nums[i - x] - a[index]) if 0 <= index < len(a) else float('inf'))

        return diff


if __name__ == '__main__':
    print(Solution().minAbsoluteDifference(nums = [4,3,2,4], x = 2))
    print(Solution().minAbsoluteDifference(nums = [5,3,2,10,15], x = 1))
    print(Solution().minAbsoluteDifference(nums = [1,2,3,4], x = 3))
