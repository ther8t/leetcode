class Solution:
    """
    Revision 2 : I had a hard time to figure out that all the index ranges with pivot within it's bound will have nums[startIndex] > nums[endIndex] which is opposite to what actually is in a sorted array.
    With that knowledge we can run a recursive B-Search.
    """
    def search(self, nums, target):
        return self.bPivotSearch(nums, 0, len(nums) - 1, target)

    def bPivotSearch(self, nums, startIndex, endIndex, target):
        if startIndex == endIndex:
            if nums[startIndex] == target:
                return startIndex
            else:
                return -1
        if nums[startIndex] < nums[endIndex]:
            if target >= nums[startIndex] and target <= nums[endIndex]:
                return self.bSearch(nums, startIndex, endIndex, target)
            else:
                return -1
        else:
            mid = (startIndex + endIndex) // 2
            result = self.bPivotSearch(nums, startIndex, mid, target)
            if result != -1:
                return result
            result = self.bPivotSearch(nums, mid + 1, endIndex, target)
            if result != -1:
                return result
        return -1

    def bSearch(self, nums, startIndex, endIndex, target):
        if startIndex == endIndex:
            if nums[startIndex] == target:
                return startIndex
            else:
                return -1
        else:
            mid = (startIndex + endIndex) // 2
            result = self.bSearch(nums, startIndex, mid, target)
            if result != -1:
                return result
            result = self.bSearch(nums, mid + 1, endIndex, target)
            if result != -1:
                return result
        return -1


if __name__ == '__main__':
    print(Solution().search([1,2,3,4], 4))
