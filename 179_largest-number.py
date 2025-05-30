class Solution:
    def largestNumber(self, nums) -> str:
        return str(int("".join(sorted([str(nums[i]) for i in range(len(nums))], reverse=True, key=lambda x: "".join([x] * 10)))))


if __name__ == '__main__':
    # print(Solution().minimumOperationsToMakeEqual(26, 1))
    # print(Solution().minimumOperationsToMakeEqual(x = 54, y = 2))
    # print(Solution().minimumOperationsToMakeEqual(x = 25, y = 30))
    print(Solution().largestNumber(nums = [10,2]))
    print(Solution().largestNumber(nums = [3,30,34,5,9]))
    print(Solution().largestNumber(nums = [3,1,14]))
    print(Solution().largestNumber([999999991,9]))
