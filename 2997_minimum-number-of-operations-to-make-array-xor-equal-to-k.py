import collections


class Solution:
    """
    Attempt: Fired
    Accepted 5%
    """
    def minOperations(self, nums, k: int) -> int:
        max_num = max(nums + [k])
        i = 0
        ans = 0

        while max_num >= (1 << i):
            counter = collections.defaultdict(int)
            for j in range(len(nums)):
                counter[(nums[j] >> i) % 2] += 1
            if ((k >> i) % 2 == 0 and counter[1] % 2 == 1) or ((k >> i) % 2 == 1 and counter[1] % 2 == 0):
                ans += 1
            i += 1
        return ans

    """
    Attempt: Fired
    Accepted: 68%
    
    This is a neat trick.
    """
    def minOperations(self, nums, k: int) -> int:
        """
        The idea is that we need to calculate the XOR of all the numbers and then check how many bits need to change with respect to k (diff).
        The diff operation is XOR operation in itself. So we initialise the variable as k only.
        """
        xor = k
        for n in nums:
            xor ^= n

        ans = 0
        while xor > 0:
            ans += xor % 2
            xor >>= 1
        return ans






if __name__ == '__main__':
    print(Solution().minOperations(nums = [2,1,3,4], k = 1))
    print(Solution().minOperations(nums = [2,0,2,0], k = 0))
    print(Solution().minOperations([4], 7))
