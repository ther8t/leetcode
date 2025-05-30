class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        b_count, ans = 0, 0
        for i in range(n):
            if s[i] == "b":
                b_count += 1
            else:
                ans = min(ans + 1, b_count)

        return ans


    # def minimumDeletions(self, s: str) -> int:
    #     n = len(s)
    #     a, b = [0] * (n + 1), [0] * (n + 1)
    #
    #     for index, char in enumerate(s):
    #         if char == "a":
    #             a[index] = a[index - 1] + 1
    #             b[index] = b[index - 1]
    #         else:
    #             b[index] = b[index - 1] + 1
    #             a[index] = a[index - 1]
    #
    #     min_deletions = float('inf')
    #
    #     for i in range(n + 1):
    #         # i length for a
    #         # n - i length for b
    #         b_count = b[i - 1] - b[-1]
    #         a_count = a[n - 1] - a[i - 1]
    #         min_deletions = min(min_deletions, a_count + b_count)
    #
    #     return min_deletions


if __name__ == '__main__':
    print(Solution().minimumDeletions(s = "aababbab"))
    print(Solution().minimumDeletions(s = "bbaaaaabb"))
