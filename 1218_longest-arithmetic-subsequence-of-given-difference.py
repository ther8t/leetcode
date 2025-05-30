import collections


class Solution:
    # # TLE 36/39
    # def longestSubsequence(self, arr, difference: int) -> int:
    #     map = collections.defaultdict(list)
    #     max_subsequence_length = 0
    #
    #     for index, value in enumerate(arr):
    #         map[value].append(index)
    #
    #     for i in range(len(arr)):
    #         current_subsequence_length = 1
    #         ptr_current = i
    #         next_number = difference + arr[ptr_current]
    #         while ptr_current < len(arr):
    #             if next_number not in map:
    #                 break
    #             position_arr = map[next_number]
    #             found = False
    #             for position in position_arr:
    #                 if position > ptr_current:
    #                     current_subsequence_length += 1
    #                     next_number = arr[position] + difference
    #                     ptr_current = position
    #                     found = True
    #                     break
    #             if not found:
    #                 break
    #         max_subsequence_length = max(max_subsequence_length, current_subsequence_length)
    #     return max_subsequence_length

    # TLE
    # def longestSubsequence(self, arr, difference: int) -> int:
    #     max_subsequence_length = 0
    #     for i in range(len(arr)):
    #         current_subsequence_length = 1
    #         ptr_current = i
    #         next_number = difference + arr[ptr_current]
    #         while ptr_current < len(arr):
    #             ptr_next = ptr_current + 1
    #             while ptr_next<len(arr):
    #                 if arr[ptr_next] == next_number:
    #                     current_subsequence_length+=1
    #                     next_number = arr[ptr_next] + difference
    #                     ptr_current = ptr_next
    #                     break
    #                 ptr_next+=1
    #             if ptr_next == len(arr):
    #                 break
    #         max_subsequence_length = max(max_subsequence_length, current_subsequence_length)
    #     return max_subsequence_length


    """
    Revision 2 :
    My first thought was to use monotonic stacks to figure out the previous smaller number. Then I remembered that there is a difference which we have to adhere to so we can directly find the previous number.
    With the previous number figured we can store a list of numbers which have occurred before the number and find out the max each time. Then I figure that we could simply do this by storing the max each time instead of storing a list.
    And this final approach came up.
    """
    def longestSubsequence(self, arr, difference: int) -> int:
        max_subsequence_length = 0
        dp = collections.defaultdict(int)

        for i in range(len(arr)):
            prev_number = arr[i] - difference
            if prev_number in dp:
                dp[arr[i]] = 1 + dp[prev_number]
            else:
                dp[arr[i]] = 1
            max_subsequence_length = max(max_subsequence_length, dp[arr[i]])
        return max_subsequence_length


if __name__ == '__main__':
    print(Solution().longestSubsequence(arr=[1, 5, 7, 8, 5, 3, 4, 2, 1], difference=-2))  # 4
    print(Solution().longestSubsequence(arr=[1, 2, 3, 4], difference=1))  # 4
    print(Solution().longestSubsequence(arr=[1, 3, 5, 7], difference=1))  # 1
    print(Solution().longestSubsequence(arr=[7, 5, 4, 3, 6, 5], difference=-1))  # 3
    print(Solution().longestSubsequence([-11, 8, 8, -13, -4, 6, 7, -3, 8, 4, -9, -7, 13, -15, 9], 9))  # 2
    print(Solution().longestSubsequence([16, -4, -6, -11, -8, -9, 4, -11, 15, 15, -9, 11, 7, -7, 10, -16, 4], 3))  # 3
