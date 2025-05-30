class Solution:

    """
    Attempt: Fired
    TLE
    """
    def countSubarrays(self, nums, k: int) -> int:
        current_max = -1
        current_max_indexes = []
        for i, num in enumerate(nums):
            if num > current_max:
                current_max = num
                current_max_indexes = []
            if num == current_max:
                current_max_indexes.append(i)

        ans = 0
        current_max_indexes = [-1] + current_max_indexes + [len(nums)]
        for current_window_len in range(k, len(current_max_indexes) - 1):
            for l in range(1, len(current_max_indexes) - current_window_len):
                r = l + current_window_len - 1
                ans += (current_max_indexes[l] - current_max_indexes[l - 1]) * (current_max_indexes[r + 1] - current_max_indexes[r])

        return ans

    def countSubarrays(self, nums, k: int) -> int:
        count = 0
        max_num = max(nums)
        l = -1

        ans = 0
        for r in range(len(nums)):
            if nums[r] == max_num:
                count += 1
            while l < r and count >= k:
                l += 1
                if nums[l] == max_num:
                    count -= 1
            ans += (l + 1)

        return ans



if __name__ == '__main__':
    print(Solution().countSubarrays(nums = [1,3,2,3,3], k = 2))
    print(Solution().countSubarrays(nums = [1,4,2,1], k = 3))
    print(Solution().countSubarrays(nums = [1,2,3,1,2,3,1,2], k = 2))
