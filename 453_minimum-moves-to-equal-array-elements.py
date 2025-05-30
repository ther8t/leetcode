class Solution:
    def minMoves(self, nums) -> int:
        min_number = min(nums)
        score = 0

        for n in nums:
            score += n - min_number

        return score


    # def minMoves(self, nums) -> int:
    #     if len(nums) == 0:
    #         return 0
    #     if len(nums) == 1:
    #         return max(nums) - min(nums)
    #     nums.sort()
    #     score = 0
    #     while nums[0] != nums[-1]:
    #         diff = nums[-1] - nums[0]
    #         score += diff
    #         for i in range(len(nums) - 1):
    #             nums[i] += diff
    #         nums.sort()
    #
    #     return score

if __name__ == '__main__':
    # print(Solution().minMoves(nums = [1,2,3]))
    print(Solution().minMoves(nums = [0,2,3,6]))

