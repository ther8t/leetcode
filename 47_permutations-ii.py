class Solution:
    def permuteUnique(self, nums):
        nums.sort()

        def permuteRec(nums):
            if len(nums) == 0:
                return [[]]
            if len(nums) == 1:
                return [[nums[0]]]

            out = []
            for i in range(len(nums)):
                if i + 1 < len(nums) and nums[i] == nums[i + 1]:
                    continue
                subarrays = permuteRec(nums[:i] + nums[i + 1:])
                for j in range(len(subarrays)):
                    out.append([nums[i]] + subarrays[j])

            return out

        return permuteRec(nums)


    # def permuteUnique(self, nums):
    #     nums.sort()
    #     return self.permuteUniqueRec(nums)
    #
    # def permuteUniqueRec(self, nums):
    #     if len(nums) == 0:
    #         return [[]]
    #
    #     if len(nums) == 1:
    #         return [nums]
    #
    #     if len(nums) == 2:
    #         if nums[0] == nums[1]:
    #             return [nums]
    #         return [[nums[0], nums[1]], [nums[1], nums[0]]]
    #     ans = []
    #
    #     i = 0
    #     while i < len(nums):
    #         while i + 1 < len(nums) and nums[i + 1] == nums[i]:
    #             i += 1
    #
    #         remainingPermutation = self.permuteUnique(nums[0:i] + nums[i + 1:])
    #         for j in remainingPermutation:
    #             ans.append([nums[i]] + j)
    #         i+=1
    #     return ans


if __name__ == '__main__':
    print(Solution().permuteUnique([1, 1, 1, 2, 2]))
    print(Solution().permuteUnique([3,3,0,3]))
