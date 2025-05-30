import collections
import functools


class Solution:

    # TLE
    def maxNonOverlapping(self, nums, target: int) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        all_sum = [0] * (n + 1)
        for i in range(n):
            all_sum[i] = all_sum[i - 1] + nums[i]

        max_subarray_count = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if all_sum[j] - all_sum[i - 1] == target:
                    dp[i] = max(dp[i], dp[j + 1] + 1)
                    break
            dp[i] = max(dp[i], dp[i + 1])
            max_subarray_count = max(max_subarray_count, dp[i])

        return max_subarray_count


    """
    Intuition:
    Move from right to left. Start counting from current index i in the right direction.
    If you discover sum equal to the target till target index j, the total count would be the max count after j index + 1.
    This is an O(n2) algo. 
    
    But there is a faster method to solve this.
    The intuition here is that this can be solved by greedy method.
    Sidenote : There's a method to find longest increasing subsequence of a array in O(n) time.
    In that we simply check if the number is greater than the last added number. The idea behind being that when a number is appended to an array at the end it creates a space, thus increasing the length. So if we discover a number which lies behind that number in order to form another subsequence, then we simply keep replacing that index with the incoming numbers.
    The idea is to create as many spaces not to maintain the correct order at all times.
    This greedy approach is sort of similar to the LIS.
    So even if there is an overlap with any of the previously recorded subarrays. Those indices can simply be updated except when they are being appended. 
    
    For example : Take [-2,6,6,0,5,1,5,-2,8], for sum 6.
    Presums : [-2,4,10,10,15,16,21,19,27]
    Index    options    presum - target    found at 
    1        -2         4 - 6 = -2         0       
    2        4          10 - 6 = 4         1       
    3        10         10 - 6 = 4         -       
    5        10,10,15   16 - 6 = 10        2,3       
    6        16         21 - 5 = 15        -
    8        16,21,19   27 - 6 = 21        6
    ..
    
    It's a bit hard to intuit, but this ordering and replacing the the prev subarrays can be done by simply deleting everything once we find a new subarray.
    We don't discover all the subarrays of sum. We miss out those which overlap with the previously found subarray.
    In my opinion, this should be a hard problem.
    """
    def maxNonOverlapping(self, nums, target: int) -> int:
        options = set()
        # We need to add 0 in order to find the first subarray. Consider this presum[-1], when there is nothing to add.
        options.add(0)

        current_sum = 0
        out = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            prev_pre_sums_needed_from_the_index_after_the_last_match_index = current_sum - target
            if prev_pre_sums_needed_from_the_index_after_the_last_match_index in options:
                out += 1
                # This is a cruitial step because we need to make sure that there is no overlap.
                options = set()
            # This includes the current index so we could minus this from the current sum to get the subarray starting from the index AFTER i.
            options.add(current_sum)

        return out

    # def maxNonOverlapping(self, nums, target: int) -> int:
    #     n = len(nums)
    #     dp = [-1] * n
    #     dp.append(0)
    #     last_found_at = n
    #
    #     def search(starting_index):
    #         nonlocal last_found_at
    #         continuous_sum = 0
    #         max_finds = -1
    #         for i in range(starting_index, last_found_at):
    #             if dp[i] >= 0:
    #                 break
    #             continuous_sum += nums[i]
    #             if continuous_sum == target:
    #                 max_finds = max(max_finds, 1 + dp[last_found_at])
    #                 break
    #         dp[starting_index] = max_finds
    #         if max_finds != -1:
    #             last_found_at = starting_index
    #         return dp[starting_index]
    #
    #     max_finds = 0
    #     for i in range(len(nums) - 1, -1, -1):
    #         max_finds = max(max_finds, search(i))
    #
    #     return max_finds


    """
    Attempt: Fired
    Accepted: 24%
    
    This is a much simpler solution than the above. It's easier to understand.
    The idea is to search for the index which carried the last diff. Diff is the current running sum - target. If that 'diff' current sum exists in the array. Then we can say that an array exists which has the sum equal to the target.
    Now we search for the maximum number of arrays which satisfied the condition of the question before that.
    """
    def maxNonOverlapping(self, nums, target: int) -> int:
        options = collections.defaultdict(int)
        options[0] = -1
        dp = [0 for _ in range(len(nums) + 1)]

        running_sum = 0
        for i in range(len(nums)):
            running_sum += nums[i]
            dp[i] = dp[i - 1]
            if running_sum - target in options:
                dp[i] = max(dp[i - 1], dp[options[running_sum - target]] + 1)
            options[running_sum] = i

        return dp[len(nums) - 1]






if __name__ == '__main__':
    print(Solution().maxNonOverlapping(nums = [0,0,-1,0,-2,0,1,0,1], target = 0))
    print(Solution().maxNonOverlapping(nums = [1,1,1,1,1], target = 2))
    print(Solution().maxNonOverlapping(nums = [-1,3,5,1,4,2,-9], target = 6))
    print(Solution().maxNonOverlapping([-2,6,6,3,5,4,1,2,8], 10))
