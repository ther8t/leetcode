import bisect
import math


class Solution:
    def waysToSplit(self, nums) -> int:
        n = len(nums)
        prev_sum = [0] * n
        s = 0

        for i in range(n):
            s += nums[i]
            prev_sum[i] = s

        def search_end(start, left_sum_end_index):
            left, right = start, n
            while left < right:
                mid_end_index = math.ceil((left + right) / 2)
                mid_sum = prev_sum[mid_end_index] - prev_sum[left_sum_end_index]
                end_sum = prev_sum[n - 1] - prev_sum[mid_end_index]
                if end_sum >= mid_sum:
                    left = mid_end_index
                else:
                    right = mid_end_index - 1

            return left

        ans = 0
        MOD = 10 ** 9 + 7
        for i in range(1, n - 1):
            left_end_index = i - 1
            left_sum = prev_sum[left_end_index]
            mid_range_start = bisect.bisect_left(prev_sum, 2 * left_sum, lo=left_end_index + 1) + 1
            mid_range_end = search_end(mid_range_start, left_end_index)
            if mid_range_end == n:
                continue
            ans += (mid_range_end - mid_range_start + 1)
            ans %= MOD

        return ans


if __name__ == '__main__':
    # print(Solution().waysToSplit(nums = [1,1,1]))
    print(Solution().waysToSplit(nums = [1,2,2,2,5,0]))
    # print(Solution().waysToSplit(nums = [3,2,1]))
