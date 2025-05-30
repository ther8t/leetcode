import collections


class Solution:
    def maxSubarrayLength(self, nums, k: int) -> int:
        n = len(nums)
        last_pos = collections.defaultdict(list)
        left, right = 0, 0
        max_len = 0

        while right < n:
            # right is currently in consideration
            if len(last_pos[nums[right]]) >= k:
                popped = last_pos[nums[right]][0]
                for i in range(left, popped + 1):
                    last_pos[nums[i]].pop(0)
                last_pos[nums[right]].append(right)
                left = popped + 1
            else:
                last_pos[nums[right]].append(right)
            right += 1
            max_len = max(max_len, right - left)

        return max_len


if __name__ == '__main__':
    print(Solution().maxSubarrayLength(nums = [1,2,3,1,2,3,1,2], k = 2))
    print(Solution().maxSubarrayLength(nums = [1,2,3,3,2,3,1,2], k = 2))
    print(Solution().maxSubarrayLength(nums = [1,2,1,2,1,2,1,2], k = 1))
    print(Solution().maxSubarrayLength(nums = [5,5,5,5,5,5,5], k = 4))
