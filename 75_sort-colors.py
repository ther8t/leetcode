class Solution:
    def sortColors(self, nums) -> None:
        lo, hi = 0, len(nums) - 1
        i = 0
        while i < len(nums):
            if nums[i] == 0 and i >= lo:
                nums[i], nums[lo] = nums[lo], nums[i]
                lo += 1
                i += 1
            elif nums[i] == 2 and i <= hi:
                nums[i], nums[hi] = nums[hi], nums[i]
                hi -= 1
            else:
                i += 1


if __name__ == '__main__':
    print(Solution().sortColors([2,0,2,1,1,0]))
    print(Solution().sortColors([1,2,0]))
