class Solution:
    def findDuplicates(self, nums):
        nums = [0] + nums

        index = 0
        duplicate = []
        for i in range(len(nums)):
            if index != nums[i]:
                next_index = nums[index]
                nums[index] = -1
                while next_index != nums[next_index] and next_index != -1:
                    temp = next_index
                    next_index = nums[next_index]
                    nums[temp] = temp

                if next_index != index and next_index != -1:
                    duplicate.append(next_index)
            index += 1

        return duplicate


if __name__ == '__main__':
    print(Solution().findDuplicates(nums = [4,3,2,7,8,2,3,1]))
    print(Solution().findDuplicates(nums = [1,1,2]))
    print(Solution().findDuplicates(nums = [1]))
    print(Solution().findDuplicates(nums = [2,3,4,1]))
