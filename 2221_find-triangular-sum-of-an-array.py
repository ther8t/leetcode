import math

class Solution:
    def triangularSum(self, nums) -> int:
        n = len(nums) - 1

        def nCr(n, r):
            f = math.factorial
            return f(n) // f(r) // f(n - r)

        res = 0
        for i in range(len(nums)):
            res += nCr(n, i) * nums[i]

        return res % 10

    # def triangularSum(self, nums) -> int:
    #     result = 0
    #     m = len(nums) - 1
    #     mCk = 1
    #     for k, num in enumerate(nums):
    #         result = (result + mCk * num) % 10
    #         mCk *= m - k
    #         mCk //= k + 1
    #     return result


if __name__ == '__main__':
    print(Solution().triangularSum(nums = [5]))
