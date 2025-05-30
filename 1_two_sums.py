class Solution:
    def __init__(self):
        pass

    def twoSum(self, nums, target):
        m = {}
        for index, num in enumerate(nums):
            if target - num in m and m[target - num] != index:
                return [index, m[target - num]]
            m[num] = index


    # def twoSum(self, nums, target):
    #     nums.sort()
    #     for i in range(len(nums) - 1) :
    #         for j in range(i+1, len(nums)) :
    #             if (nums[j] + nums[i]) > target:
    #                 break
    #
    #             if (nums[i] + nums[j]) == target:
    #                 return [i, j]

    """
    Attempt #2
    Accepted : 75%
    """
    def twoSum(self, nums, target):
        temp = {}
        for index, num in enumerate(nums):
            if (target - num) in temp:
                return (index, temp[target - num])
            temp[num] = index


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([3,2,3], 6))