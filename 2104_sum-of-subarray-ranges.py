import collections


class Solution:
    # def subArrayRanges(self, nums) -> int:
    #     n = len(nums)
    #     res = 0
    #     stack = []
    #
    #     nextsmaller = [n] * n
    #     for i in range(n):
    #         while stack and nums[stack[-1]] > nums[i]:
    #             nextsmaller[stack.pop()] = i
    #         stack.append(i)
    #
    #     stack = []
    #     prevsmaller = [-1] * n
    #     for i in range(n - 1, -1, -1):
    #         while stack and nums[stack[-1]] >= nums[i]:
    #             prevsmaller[stack.pop()] = i
    #         stack.append(i)
    #
    #     stack = []
    #     nextgreater = [n] * n
    #     for i in range(n):
    #         while stack and nums[stack[-1]] < nums[i]:
    #             nextgreater[stack.pop()] = i
    #         stack.append(i)
    #
    #     stack = []
    #     prevgreater = [-1] * n
    #     for i in range(n - 1, -1, -1):
    #         while stack and nums[stack[-1]] <= nums[i]:
    #             prevgreater[stack.pop()] = i
    #         stack.append(i)
    #
    #     minsum = 0
    #     for i in range(n):
    #         minsum += (prevsmaller[i] - i) * (i - nextsmaller[i]) * nums[i]
    #
    #     maxsum = 0
    #     for i in range(n):
    #         maxsum += (prevgreater[i] - i) * (i - nextgreater[i]) * nums[i]
    #
    #     return maxsum - minsum

    def subArrayRanges(self, nums) -> int:
        n = len(nums)
        stack = []
        next_greater = [n] * n
        for i in range(n):
            while stack and nums[i] > nums[stack[-1]]:
                popped = stack.pop()
                next_greater[popped] = i
            stack.append(i)

        stack = []
        next_smaller = [n] * n
        for i in range(n):
            while stack and nums[i] < nums[stack[-1]]:
                popped = stack.pop()
                next_smaller[popped] = i
            stack.append(i)

        stack = []
        prev_greater = [-1] * n
        for i in range(n - 1, -1, -1):
            while stack and nums[i] >= nums[stack[-1]]:
                popped = stack.pop()
                prev_greater[popped] = i
            stack.append(i)

        stack = []
        prev_smaller = [-1] * n
        for i in range(n - 1, -1, -1):
            while stack and nums[i] <= nums[stack[-1]]:
                popped = stack.pop()
                prev_smaller[popped] = i
            stack.append(i)

        min_sum = 0
        for i in range(n):
            min_sum += (i - prev_smaller[i]) * (next_smaller[i] - i) * nums[i]

        max_sum = 0
        for i in range(n):
            max_sum += (i - prev_greater[i]) * (next_greater[i] - i) * nums[i]

        return max_sum - min_sum


    # def subArrayRanges(self, nums) -> int:
    #     sa_range = 0
    #
    #     for i in range(len(nums)):
    #         range_min = nums[i]
    #         range_max = nums[i]
    #         for j in range(i, len(nums)):
    #             range_min = min(range_min, nums[j])
    #             range_max = max(range_max, nums[j])
    #             sa_range += (range_max - range_min)
    #
    #     return sa_range


    """
    There is an interesting part of this problem statement which I have not mentioned here.
    The solution is to find the sum of range of all the subarrays, which requires us to calculate the max and min of all the subarrays.
    We chose to do something else. We choose to take a number and see how many subarrays is that number the greatest or the smallest for.
    
    First thing which we need to consider is this: The sum of all the arrays thus found would be the sum of all the subarrays.
    This is because, each number has to be the greatest or the smallest of some subarrays, or to say it better, each subarray must have a greatest or the smallest.
    
    Second thing. The problem arises when we compare the equals. If we keep including the equals we find that we count more subarrays because of duplication.
    For example: [xx1x1x] for the array 1 is the lowest say, so 3x2 6 is counted twice.
    The easy fix is to allow equality only on one side. 
    """
    def subArrayRanges(self, nums) -> int:
        n = len(nums)

        next_smaller_equal, next_greater_equal = [n for _ in range(n)], [n for _ in range(n)]
        s, g = [], []
        for i in range(n):
            while g and nums[g[-1]] < nums[i]:
                next_greater_equal[g.pop()] = i
            g.append(i)

            while s and nums[s[-1]] > nums[i]:
                next_smaller_equal[s.pop()] = i
            s.append(i)

        prev_smaller, prev_greater = [-1 for _ in range(n)], [-1 for _ in range(n)]
        s, g = [], []
        for i in range(n - 1, -1, -1):
            while g and nums[g[-1]] <= nums[i]:
                prev_greater[g.pop()] = i
            g.append(i)

            while s and nums[s[-1]] >= nums[i]:
                prev_smaller[s.pop()] = i
            s.append(i)

        ans = 0
        for i in range(n):
            ans += nums[i] * (((next_greater_equal[i] - i) * (i - prev_greater[i])) - ((next_smaller_equal[i] - i) * (i - prev_smaller[i])))

        return ans

if __name__ == '__main__':
    print(Solution().subArrayRanges(nums = [4,-2,-3,4,1]))
    print(Solution().subArrayRanges(nums = [1, 2, 3]))
