import collections


class Solution:

    # TLE
    def numSubarraysWithSum(self, nums, goal: int) -> int:
        if not nums:
            return 0
        n = len(nums)
        current_sum = 0
        ans = 0
        sums = [0] * (n + 1)
        for i in range(n):
            current_sum += nums[i]
            sums[i] = current_sum

        for lo in range(n):
            for hi in range(lo, n):
                current_sum = sums[hi] - sums[lo - 1]
                if current_sum == goal:
                    ans += 1
                if current_sum > goal:
                    break

        return ans

    def numSubarraysWithSum(self, nums, goal: int) -> int:
        if not nums:
            return 0
        running_sum = collections.defaultdict(list)
        current_sum = 0

        ans = 0
        for i in range(len(nums)):
            current_sum += nums[i]

            if current_sum - goal in running_sum:
                ans += len(running_sum[current_sum - goal])
            if current_sum == goal:
                ans += 1
            running_sum[current_sum].append(i)

        return ans

    """
    Attempt: Fired
    TLE
    """
    def numSubarraysWithSum(self, nums, goal: int) -> int:
        if not nums:
            return 0
        current_sum = 0
        l = 0

        ans = 0
        for r in range(len(nums)):
            current_sum += nums[r]
            while current_sum > goal and l < r:
                current_sum -= nums[l]
                l += 1
            temp = l
            prefix_counter = 0
            while temp < r and nums[temp] == 0:
                prefix_counter += 1
                temp += 1

            ans += temp - l + 1 if current_sum == goal else 0
        return ans



    def numSubarraysWithSum(self, nums, goal: int) -> int:
        if not nums:
            return 0

        def numSubarraysWithSumAtMost(goal):
            l = 0
            current_sum = 0

            ans = 0
            for r in range(len(nums)):
                current_sum += nums[r]
                while current_sum > goal and l < r:
                    current_sum -= nums[l]
                    l += 1
                ans += r - l + 1 if current_sum <= goal else 0

            return ans

        return numSubarraysWithSumAtMost(goal) - numSubarraysWithSumAtMost(goal - 1)


if __name__ == '__main__':
    print(Solution().numSubarraysWithSum(nums = [1,0,1,0,1], goal = 2))
    print(Solution().numSubarraysWithSum(nums = [0,0,0,0,0], goal = 0))
