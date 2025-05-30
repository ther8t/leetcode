import collections


class Solution:
    def minimumOperations(self, nums) -> int:
        counter = collections.Counter(nums)
        del counter[0]
        return len(counter)


if __name__ == '__main__':
    print(Solution().minimumOperations(nums = [1,5,0,3,5]))
    print(Solution().minimumOperations(nums = [0]))
