import collections


class Solution:
    def beautifulSubsets(self, nums, k: int) -> int:
        ans = 0

        def dfs(index, members):
            nonlocal ans
            if index == len(nums):
                if members:
                    ans += 1
                return
            dfs(index + 1, members)
            if nums[index] + k not in members and nums[index] - k not in members:
                members[nums[index]] += 1
                dfs(index + 1, members)
                members[nums[index]] -= 1
                if members[nums[index]] == 0:
                    del members[nums[index]]

        dfs(0, collections.defaultdict(int))
        return ans


if __name__ == '__main__':
    # print(Solution().beautifulSubsets(nums = [2,4,6], k = 2))
    print(Solution().beautifulSubsets(nums = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40], k = 2))
    # print(Solution().beautifulSubsets(nums = [1], k = 1))
