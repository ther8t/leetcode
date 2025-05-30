class Solution:
    def maxSubArray(self, nums) -> int:
        c_sum = [0 for _ in range(len(nums) + 1)]

        for i in range(len(nums)):
            c_sum[i] = c_sum[i - 1] + nums[i]

        min_i, max_i = -1, 0
        for i in range(len(nums)):
            if c_sum[i] > c_sum[max_i]:
                max_i = i

        for i in range(-1, max_i):
            if c_sum[i] < c_sum[min_i]:
                min_i = i

        return c_sum[max_i] - c_sum[min_i]


    def maxSubArray(self, nums) -> int:
        max_diff = -float('inf')
        running_min = 0
        running_sum = 0
        for i in range(len(nums)):
            running_sum = running_sum + nums[i]
            max_diff = max(max_diff, running_sum - running_min)
            running_min = min(running_min, running_sum)

        return max_diff







if __name__ == '__main__':
    print(Solution().maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))
    print(Solution().maxSubArray(nums = [-1]))
    print(Solution().maxSubArray(nums = [1]))
    print(Solution().maxSubArray(nums = [5,4,-1,7,8]))
    print(Solution().maxSubArray(nums = [-2,-1]))
