import functools
import heapq


class Solution:

    """
    Attempt: Fired
    Accepted: 27%
    This is an interesting take on a dp problem. It is exactly the same as 198_house-robber. There's just one change at the bottom.
    This was particularly difficult to find out.
    The issue is that we don't know if the last one will connect back to the first one or not. Let's say the first one connects to someone who connected with the last(which was adjacent to the first)
    Easy fix. REMOVE IT!! Break the garland.
    """
    def rob(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]

        def robBlind(nums):
            n = len(nums)
            a = [(0, n), (0, n + 1)]

            for i in range(n - 1, -1, -1):
                if a[0][1] - i == 1:
                    a.append((nums[i] + a[1][0], i))
                else:
                    a.append((nums[i] + a[0][0], i))
                a = sorted(a, reverse=True)[:2]

            return a[0][0]

        return max(robBlind(nums[:-1]), robBlind(nums[1:]))


if __name__ == '__main__':
    print(Solution().rob(nums = [2,3,2]))
    print(Solution().rob(nums = [2,7,9,3,1]))
    print(Solution().rob(nums = [1,2,3,1]))
    print(Solution().rob(nums = [1,2,3]))
    print(Solution().rob(nums = [1]))
    print(Solution().rob(nums = [1,2]))

