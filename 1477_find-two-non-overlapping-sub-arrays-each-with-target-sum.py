import bisect
import collections
import functools


class Solution:
    # Accepted as well.
    def minSumOfLengths(self, arr, target: int) -> int:
        start, end, sum = 0, 0, 0
        subarray_keeper = {i: float('inf') for i in range(len(arr))}
        subarray_keeper[-1] = float('inf')
        global_min = float('inf')
        for i in range(len(arr)):
            end = i
            sum += arr[i]
            while sum > target:
                sum -= arr[start]
                start += 1
            if sum == target:
                subarray_keeper[end] = min(subarray_keeper[end], subarray_keeper[end - 1], end - start + 1)
                global_min = min(global_min, subarray_keeper[start - 1] + end - start + 1)
            else:
                subarray_keeper[end] = min(subarray_keeper[end], subarray_keeper[end - 1])

        return global_min if global_min != float('inf') else -1

    # # Accepted : This was a tough question despite it's rating as Medium it's acceptance rate is 37%.
    # # Concept to be learnt : Sliding Window.
    # def minSumOfLengths(self, arr, target: int) -> int:
    #     subarray_keeper = {i:float('inf') for i in range(len(arr))}
    #     subarray_keeper[-1] = float('inf')
    #     ptr_l, ptr_r = 0, 0
    #     sum = 0
    #     global_min = float('inf')
    #     while ptr_l < len(arr) and ptr_r < len(arr):
    #         if ptr_l > ptr_r:
    #             ptr_r = ptr_l
    #             sum = 0
    #         elif sum + arr[ptr_r] == target:
    #             sum+=arr[ptr_r]
    #             min_length_before_this_match = subarray_keeper[ptr_l - 1]
    #             length_this_match = (ptr_r - ptr_l + 1)
    #             subarray_keeper[ptr_r] = min(length_this_match, min_length_before_this_match)
    #             global_min = min(global_min, length_this_match + min_length_before_this_match)
    #             ptr_r+=1
    #         elif sum + arr[ptr_r] < target:
    #             sum += arr[ptr_r]
    #             subarray_keeper[ptr_r] = min(subarray_keeper[ptr_r - 1], subarray_keeper[ptr_r])
    #             ptr_r += 1
    #         elif sum + arr[ptr_r] > target:
    #             sum -= arr[ptr_l]
    #             subarray_keeper[ptr_l] = min(subarray_keeper[ptr_l - 1], subarray_keeper[ptr_l])
    #             ptr_l += 1
    #
    #     return global_min if global_min != float('inf') else -1

    # # TLE
    # def minSumOfLengths(self, arr, target: int) -> int:
    #     subarray_keeper = []
    #     for starting_pos in range(len(arr)):
    #         sum = 0
    #         ptr = starting_pos
    #         while ptr < len(arr) and arr[ptr] + sum <= target:
    #             sum += arr[ptr]
    #             ptr += 1
    #         if sum == target:
    #             subarray_keeper.append((starting_pos, ptr))
    #
    #     subarray_keeper.sort(key=lambda x: x[1] - x[0])
    #
    #     min_len_sum = float('inf')
    #     for i in range(len(subarray_keeper) - 1):
    #         for j in range(i, len(subarray_keeper)):
    #             # is overlap?
    #             if subarray_keeper[i][0] < subarray_keeper[i][1] <= subarray_keeper[j][0] < subarray_keeper[j][1] or \
    #                     subarray_keeper[j][0] < subarray_keeper[j][1] <= subarray_keeper[i][0] < subarray_keeper[i][1]:
    #                 min_len_sum = min((subarray_keeper[i][1] - subarray_keeper[i][0]) + (
    #                             subarray_keeper[j][1] - subarray_keeper[j][0]), min_len_sum)
    #
    #     return min_len_sum if min_len_sum != float('inf') else -1

    # def minSumOfLengths(self, arr, target: int) -> int:
    #     subarray_keeper = {i:float('inf') for i in range(len(arr))}
    #     subarray_keeper[-1] = float('inf')
    #     min_len_sum = float('inf')
    #     for starting_pos in range(len(arr)):
    #         sum = 0
    #         ptr = starting_pos
    #         while ptr < len(arr) and arr[ptr] + sum <= target:
    #             sum += arr[ptr]
    #             ptr += 1
    #         if sum == target:
    #             subarray_keeper[ptr - 1] = min(subarray_keeper[starting_pos - 1], ptr-starting_pos)
    #             min_len_sum = min(min_len_sum, subarray_keeper[starting_pos - 1] + ptr-starting_pos)
    #         else:
    #             subarray_keeper[starting_pos] = min(subarray_keeper[starting_pos - 1], subarray_keeper[starting_pos])
    #
    #     return min_len_sum if min_len_sum != float('inf') else -1


    def minSumOfLengths(self, arr, target: int) -> int:
        n = len(arr)
        match_length = [0] * (n + 1)
        match_length[-1] = float('inf')
        start = 0
        s = 0
        ans = float('inf')
        for i in range(len(arr)):
            s += arr[i]

            while s > target:
                s -= arr[start]
                start += 1
            if s == target:
                match_length[i] = min(match_length[i - 1], i - start + 1)
                ans = min(ans, i - start + 1 + match_length[start - 1])
            else:
                match_length[i] = match_length[i - 1]

        return ans if ans != float('inf') else -1

    """
    Attempt: Fired
    Accepted 5.23%
    """
    def minSumOfLengths(self, arr, target: int) -> int:
        n = len(arr)
        c_sum = [0] * (n + 1)

        for i in range(n):
            c_sum[i] = c_sum[i - 1] + arr[i]

        @functools.lru_cache(None)
        def searchMinLen(index):
            if index > n:
                return float('inf')

            min_len = float('inf')
            hi = bisect.bisect_left(c_sum, c_sum[index - 1] + target, hi=n)
            if hi < n and c_sum[hi] == c_sum[index - 1] + target:
                min_len = hi - index + 1
            return min(min_len, searchMinLen(index + 1))

        min_len = float('inf')
        for i in range(n):
            hi = bisect.bisect_left(c_sum, c_sum[i - 1] + target, hi=n)
            if hi < n and c_sum[hi] == c_sum[i - 1] + target:
                min_len = min(min_len, (hi - i + 1) + searchMinLen(hi + 1))

        return min_len if min_len != float('inf') else -1


    """
    Attempt: Fired
    We need to find the minimum length which the sum of a subarray can have really. Let that index be i and our current index be c.
    This can easily be solved by running sum. Just search for (current_running_sum - target)
    Additional problem is that we need to find a similar such subarray. The constraint here is that, this subarray should be before index i, inclusive.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    def minSumOfLengths(self, arr, target: int) -> int:
        min_len_keeper = collections.defaultdict(lambda: float("inf"))
        run_sum = 0
        c_sum_index_map = collections.defaultdict(int)
        c_sum_index_map[0] = -1

        ans = float('inf')
        for i in range(len(arr)):
            run_sum += arr[i]
            c_sum_index_map[run_sum] = i
            if run_sum - target in c_sum_index_map:
                prev_index = c_sum_index_map[run_sum - target]
                ans = min(ans, min_len_keeper[prev_index] + (i - prev_index))
                min_len_keeper[i] = min(min_len_keeper[i - 1], (i - prev_index))
            else:
                min_len_keeper[i] = min_len_keeper[i - 1]

        return ans if ans != float('inf') else -1


if __name__ == '__main__':
    print(Solution().minSumOfLengths(arr = [3,2,2,4,3], target = 3))
    print(Solution().minSumOfLengths(arr = [7,3,4,7], target = 7))
    print(Solution().minSumOfLengths(arr = [4,3,2,6,2,3,4], target = 6))
    print(Solution().minSumOfLengths([2, 2, 4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                     20))
