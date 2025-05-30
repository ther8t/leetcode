from bisect import bisect_left, bisect_right


class Solution:
    def searchRange(self, nums, target):
        r = [-1, -1]
        index = bisect_left(nums, target)
        if index >= len(nums) or nums[index] != target:
            return r
        r[0] = index
        index = bisect_right(nums, target)
        r[1] = index - 1
        return r

    # def searchRange(self, nums, target):
    #     if not nums:
    #         return [-1, -1]
    #     return self.searchRangeRecursive(nums, 0, len(nums) - 1, target)
    #
    # def searchRangeRecursive(self, nums, startIndex, endIndex, target):
    #     mid = (startIndex + endIndex) // 2
    #     if target != nums[mid] and (startIndex == endIndex or target<nums[startIndex] or target>nums[endIndex]):
    #         return [-1, -1]
    #     if nums[startIndex] == target and nums[endIndex] == target:
    #         return [startIndex, endIndex]
    #     if nums[mid] == target:
    #         # the range is around this point
    #         # search the left side to get a range
    #         # search the right side to get a range
    #         leftRange = self.searchRangeRecursive(nums, startIndex, mid, target)
    #         rightRange = self.searchRangeRecursive(nums, mid + 1, endIndex, target)
    #         if leftRange[0] == -1 and leftRange[1] == -1:
    #             return rightRange
    #         elif rightRange[0] == -1 and rightRange[1] == -1:
    #             return leftRange
    #         else:
    #             return [leftRange[0], rightRange[1]]
    #     elif target < nums[mid]:
    #         return self.searchRangeRecursive(nums, startIndex, mid - 1, target)
    #     else:
    #         return self.searchRangeRecursive(nums, mid + 1, endIndex, target)


if __name__ == '__main__':
    print(Solution().searchRange([5,8,8,9, 9,10], 8))
    print(Solution().searchRange(nums = [5,7,7,8,8,10], target = 8))
    print(Solution().searchRange(nums = [5,7,7,8,8,10], target = 6))
    print(Solution().searchRange(nums = [], target = 0))
    print(Solution().searchRange(nums = [1], target = 1))
