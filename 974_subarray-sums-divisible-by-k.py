import collections
import functools


class Solution:
    """
    This is the correct and elegant solution to the problem statement, just not the problem statement which was asked to solve.
    """
    def subarraysDivByK(self, nums, k: int) -> int:
        sum_map = {}

        for i in nums:
            diff = collections.defaultdict(int)
            for j in sum_map.keys():
                diff[i + j] = (sum_map[i + j] if i + j in sum_map else 0) + (sum_map[j] if j in sum_map else 0)
            diff[i] += 1

            for j in diff.keys():
                sum_map[j] = diff[j]

        ans = 0
        for i in sum_map.keys():
            if i % k == 0:
                ans += sum_map[i]

        return ans


    """
    TLE
    """
    def subarraysDivByK(self, nums, k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                if current_sum % k == 0:
                    ans += 1

        return ans



    """
    This is a pretty interesting solution to this.
    The fundamental key to this problem is the fact that a % k = c and b % k = c will only form multiples of k such that (a + b) % k = c
    Rest is easy to follow.
    if there are a, b, c subarrays whose sum is multiple of k, then the comibnations of those will also be multiples so, (a, b) (c, a), (b, c) - 3 
    """
    def subarraysDivByK(self, nums, k: int) -> int:
        ans = 0
        current_sum = 0
        remainder_map = collections.defaultdict(list)
        for i, num in enumerate(nums):
            current_sum += num
            ans += len(remainder_map[current_sum % k])
            remainder_map[current_sum % k].append(i)

        return ans + len(remainder_map[0])


if __name__ == '__main__':
    print(Solution().subarraysDivByK(nums = [4,5,0,-2,-3,1], k = 5))
    print(Solution().subarraysDivByK(nums = [5], k = 9))
