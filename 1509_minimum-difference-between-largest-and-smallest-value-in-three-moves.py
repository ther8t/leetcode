class Solution:
    """
    Revision 2:
    It took about 5 minutes but I was able to crack it in the first go.

    Approach:
    The numbers to be considered are only the smallest and the largest ones.
    So sort the array and look at the first and last numbers.
    We need to choose only 3 numbers from either or both sides.
    If we look closely we observe that the min diff you can achieve is actually the difference of the largest and smallest number thus remain after making the choice of the three numbers.
    """
    def minDifference(self, nums):
        if len(nums) <= 4:
            return 0
        nums.sort()
        minDiff = float('inf')
        for i in range(4):
            minDiff = min(minDiff, nums[len(nums) - 3 + i - 1] - nums[i])
        return minDiff


if __name__ == '__main__':
    print(Solution().minDifference([6,6,0,1,1,4,6]))
