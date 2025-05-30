class Solution:
    """
    Attempt: Fired
    Accepted: 29%
    """
    def productExceptSelf(self, nums):
        a = [1 for _ in range(len(nums))]
        p = 1
        for i in range(len(nums)):
            a[i] = p
            p *= nums[i]

        p = 1
        for i in range(len(nums) - 1, -1, -1):
            a[i] *= p
            p *= nums[i]

        return a


if __name__ == '__main__':
    print(Solution().productExceptSelf([1,2,3,4]))
    print(Solution().productExceptSelf([-1,1,0,-3,3]))
