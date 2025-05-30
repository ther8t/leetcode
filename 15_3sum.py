import collections


class Solution:
    LEVEL = 3

    def threeSum(self, nums):
        nums.sort()

        a = []

        def twoSum(nums, target):
            a = []
            ptr1 = 0
            ptr2 = len(nums) - 1
            while ptr1 < ptr2:
                if (nums[ptr1] + nums[ptr2]) == target:
                    while nums[ptr1] == nums[ptr1 + 1] and ptr1 + 1 <= len(nums) - 1:
                        ptr1 += 1
                    while nums[ptr2] == nums[ptr2 - 1] and ptr2 - 1 >= 0:
                        ptr2 -= 1

                    a.append([nums[ptr1], nums[ptr2]])
                    ptr1 += 1
                    ptr2 -= 1
                elif (nums[ptr1] + nums[ptr2]) < target:
                    ptr1 += 1
                elif (nums[ptr1] + nums[ptr2]) > target:
                    ptr2 -= 1
            return a

        for i in range(len(nums)):
            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                continue
            twoSums = twoSum(nums[i + 1:], -1 * nums[i])
            for j in range(len(twoSums)):
                a.append([nums[i]] + twoSums[j])
        return a

    def threeSumRecursive(self, nums, target, level):
        if level == 1:
            a = []
            for i in range(len(nums)):
                if nums[i] == target:
                    a.append([nums[i]])
            return a
        else:
            a = []
            for i in range(len(nums)):
                sums = self.threeSumTarget(nums[i + 1:], target - nums[i], level - 1)
                for j in range(len(sums)):
                    a.append([nums[i]] + sums[j])

            return a


if __name__ == '__main__':
    print(Solution().threeSum([-1, -1, -1, 0, 1, 2, -1, -4]))
