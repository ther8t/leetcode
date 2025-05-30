class Solution:
    def removeDuplicates(self, nums):
        if nums is None or len(nums) == 0:
            return []
        ptrUnique = 0

        for i in range(len(nums)):
            if nums[i]!=nums[ptrUnique]:
                ptrUnique+=1
                nums[ptrUnique] = nums[i]
        return ptrUnique+1

if __name__ == '__main__':
    print(Solution().removeDuplicates([1,1,2]))
