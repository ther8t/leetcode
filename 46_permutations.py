class Solution:
    def permute(self, nums):
        if len(nums) == 0:
            return [[]]

        if len(nums) == 1:
            return [nums]

        if len(nums) == 2:
            return [[nums[0], nums[1]], [nums[1], nums[0]]]
        ans = []
        for i in range(len(nums)):
            remainingPermutation = self.permute(nums[0:i] + nums[i + 1:])
            for j in remainingPermutation:
                ans.append([nums[i]] + j)
        return ans


if __name__ == '__main__':
    print(Solution().permute([1, 2, 3, 4]))
