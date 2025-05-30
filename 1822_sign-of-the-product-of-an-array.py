class Solution:
    def arraySign(self, nums) -> int:
        negatives = 0
        for num in nums:
            if num < 0:
                negatives += 1
            if num == 0:
                return 0
        return 1 if negatives % 2 == 0 else -1


if __name__ == '__main__':
    print(Solution().arraySign(nums = [-1,-2,-3,-4,3,2,1]))
    print(Solution().arraySign(nums = [1,5,0,2,-3]))
    print(Solution().arraySign(nums = [-1,1,-1,1,-1]))
