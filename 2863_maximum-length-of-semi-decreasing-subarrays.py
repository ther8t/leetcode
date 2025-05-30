from sortedcontainers import SortedList


class Solution:
    """
    Attempt: Fired
    TLE
    """
    def maxSubarrayLength(self, nums) -> int:
        a = SortedList()
        max_len = 0
        for i, val in enumerate(nums):
            index = a.bisect_right((val, i))
            least_index = min(a[index:], key=lambda x: x[1], default=(val, i))
            max_len = max(i - least_index[1] + 1, max_len)
            a.add((val, i))

        return max_len if max_len > 1 else 0

    """
    Attempt: Fired
    Accepted: 51%
    I had the intuition that this could be solved in O(N).
    Read: https://leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays/discuss/4322342/O(N)-Consice-easy-to-understand-solution-in-Python3
    I'm feeling lazy explaining.
    """
    def maxSubarrayLength(self, nums) -> int:
        n = len(nums)

        stack = []
        for i in range(n):
            if not stack or nums[stack[-1]] < nums[i]:
                stack.append(i)

        ans = 0
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] > nums[i]:
                ans = max(ans, i - stack[-1] + 1)
                stack.pop()

        return ans



if __name__ == '__main__':
    print(Solution().maxSubarrayLength(nums = [7,6,5,4,3,2,1,6,10,11]))
    print(Solution().maxSubarrayLength(nums = [57,55,50,60,61,58,63,59,64,60,63]))
    print(Solution().maxSubarrayLength(nums = [1,2,3,4]))
