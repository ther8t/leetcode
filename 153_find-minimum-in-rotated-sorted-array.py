class Solution:
    def findMin(self, nums) -> int:
        n = len(nums)
        if nums[0] <= nums[n - 1]:
            return nums[0]
        lo, hi = 0, n

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[0] < nums[mid] and nums[n - 1] < nums[mid]:
                lo = mid
            else:
                if nums[mid - 1] > nums[mid] and (mid + 1 == n or (nums[mid + 1] > nums[mid])):
                    return nums[mid]
                hi = mid

        return -1


if __name__ == '__main__':
    print(Solution().findMin(nums = [1]))
    print(Solution().findMin(nums = [0,1,2]))
    print(Solution().findMin(nums = [3,4,5,1,2]))
    print(Solution().findMin(nums = [4,5,6,7,0,1,2]))
    print(Solution().findMin(nums = [11,13,15,17]))
