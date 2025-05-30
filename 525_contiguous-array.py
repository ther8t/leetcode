class Solution:
    def findMaxLength(self, nums) -> int:
        n = len(nums)

        # Remeber the counter holds the counter AFTER the count has been updated so counter[0] already has the updated count for nums[0]
        # counter = [0] * (n + 1)
        current_count = 0
        first_count = {0: -1}
        ans = 0
        for i in range(n):
            current_count += 1 if nums[i] == 1 else -1
            if current_count in first_count:
                ans = max(ans, (i - first_count[current_count]))
            else:
                first_count[current_count] = i

        return ans


if __name__ == '__main__':
    print(Solution().findMaxLength(nums = [0,1]))
    print(Solution().findMaxLength(nums = [0,1,0]))
    print(Solution().findMaxLength(nums = [0, 1, 1, 0, 0, 0, 1, 0, 1]))
