import collections


class Solution:
    def minSwaps(self, nums) -> int:
        n = len(nums)
        zero_counter, one_counter = [0] * (n + 1), [0] * (n + 1)
        zero, one = 0, 0
        for i, v in enumerate(nums):
            if v == 0:
                zero += 1
            else:
                one += 1
            zero_counter[i] = zero
            one_counter[i] = one

        def check(index):
            zero_block = (one_counter[index + zero - 1] - one_counter[index - 1]) if index + zero < n else float('inf')
            one_block = (zero_counter[index + one - 1] - zero_counter[index - 1]) if index + one < n else float('inf')
            return min(zero_block, one_block)

        min_swaps = float('inf')
        for i in range(n):
            min_swaps = min(min_swaps, check(i))

        return min_swaps


    """
    Attempt: Fired
    Accepted: 5%
    """
    def minSwaps(self, nums) -> int:
        n = len(nums)
        counter = collections.Counter(nums)
        ones = counter[1]

        counter = collections.Counter(nums[:ones])
        min_swaps = counter[0]
        for i in range(ones, n + ones):
            counter[nums[(i - ones) % n]] -= 1
            counter[nums[i % n]] += 1
            min_swaps = min(min_swaps, counter[0])

        return min_swaps



if __name__ == '__main__':
    print(Solution().minSwaps(nums = [0,1,0,1,1,0,0]))
    print(Solution().minSwaps(nums = [0,1,1,1,0,0,1,1,0]))
    print(Solution().minSwaps(nums = [1,1,0,0,1]))
