class Solution:
    def removeElement(self, nums, val):
        if nums is None or len(nums) == 0:
            return 0
        ptrRemaining = -1

        for i in range(len(nums)):
            if nums[i] != val:
                ptrRemaining += 1
                nums[ptrRemaining] = nums[i]
        return ptrRemaining + 1


if __name__ == '__main__':
    print(Solution().removeElement([1, 1, 2], 1))
