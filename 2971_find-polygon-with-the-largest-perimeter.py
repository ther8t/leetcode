class Solution:
    def largestPerimeter(self, nums) -> int:
        if len(nums) < 3:
            return -1
        nums.sort()
        r_sum = sum(nums[:2])
        max_sum = -1
        for i in range(2, len(nums)):
            if r_sum > nums[i]:
                max_sum = max(max_sum, r_sum + nums[i])
            r_sum += nums[i]
        return max_sum


if __name__ == '__main__':
    print(Solution().largestPerimeter(nums = [5,5,5]))
    print(Solution().largestPerimeter(nums = [1,12,1,2,5,50,3]))
    print(Solution().largestPerimeter([5,5,50]))
