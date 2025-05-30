class Solution:
    """
    Revision 2 : I remember this solution. I came up with this after waking up and having figured it out in my sleep.
    I woke up to realise that it is done by swap.
    All the elements, if they exist, after the swap come to the position of index that their value suggests and the first which doesn't at the end is the one which is the answer.
    """
    def firstMissingPositive(self, nums):
        nums = [0] + nums

        for i in range(1, len(nums)):
            if nums[i] >= len(nums) or nums[i] < 1:
                nums[i] = -1
            else:
                if nums[i] == i:
                    continue
                ptr = nums[i]
                while len(nums) > ptr > 0:
                    temp = nums[ptr]
                    nums[ptr] = ptr
                    ptr = temp
                    if nums[ptr] == ptr:
                        break

        for i in range(1, len(nums)):
            if nums[i] != i:
                return i
        return len(nums)


    # # Wrong Answer
    # def firstMissingPositive(self, nums):
    #     mini = float('inf')
    #     maxi = -float('inf')
    #     numbersCount = 0
    #     numbersSum = 0
    #     for i in range(len(nums)):
    #         if nums[i] <= 0:
    #             continue
    #         mini = min(nums[i], mini)
    #         maxi = max(nums[i], maxi)
    #         numbersCount += 1
    #         numbersSum += nums[i]
    #     if mini != 1:
    #         return 1
    #     if (maxi - mini + 1) == numbersCount:
    #         return maxi + 1
    #
    #     APofNumbersIfTheyWereSeries = (maxi + mini)*(maxi - mini + 1)//2
    #     sumOfMissingNumbers = APofNumbersIfTheyWereSeries - numbersSum
    #     missingNumberCount = maxi - mini + 1 - numbersCount
    #
    #     if missingNumberCount == 1:
    #         return sumOfMissingNumbers
    #
    #     averageMissingNumber = sumOfMissingNumbers//missingNumberCount
    #     for i in range(2, averageMissingNumber + 2):
    #         if i not in nums:
    #             return i


if __name__ == '__main__':
    print(Solution().firstMissingPositive(
        [-4, 24, 32, 25, 16, -8, 3, -5, -6, 30, 3, 3, 29, -5, 6, -3, 1, 29, -2, 4, 4, 7, 14, 20, 5, 0, 25, 2, 13, 26,
         -9, 7, 6, 33]))
