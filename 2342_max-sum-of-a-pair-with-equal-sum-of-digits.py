import bisect
import collections


class Solution:
    def maximumSum(self, nums: list) -> int:
        a = collections.defaultdict(list)

        def get_digit_sum(num):
            digit_sum = 0
            while num != 0:
                digit_sum += (num % 10)
                num //= 10
            return digit_sum

        ans = -1
        for n in nums:
            digit_sum = get_digit_sum(n)
            a[digit_sum].append(n)
            a[digit_sum] = sorted(a[digit_sum])
            a[digit_sum] = a[digit_sum][-2:]
            if len(a[digit_sum]) == 2:
                ans = max(ans, sum(a[digit_sum]))

        return ans


if __name__ == '__main__':
    # print(Solution().maximumSum(nums = [18,43,36,13,7]))
    print(Solution().maximumSum([229,398,269,317,420,464,491,218,439,153,482,169,411,93,147,50,347,210,251,366,401]))
