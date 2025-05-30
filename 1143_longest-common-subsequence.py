import functools


class Solution:
    """
    Attempt: Fired
    TLE
    """
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1 = " " + text1
        text2 = " " + text2

        @functools.lru_cache(None)
        def lcs(index1, index2):
            if index1 == len(text1) or index2 == len(text2):
                return 0
            lcsl = 0
            for i in range(index1, len(text1)):
                for j in range(index2, len(text2)):
                    if text1[i] == text2[j]:
                        lcsl = max(lcsl, 1 + lcs(i + 1, j + 1))

            return lcsl

        return lcs(0, 0) - 1

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2) > len(text1):
            text1, text2 = text2, text1

        a = [[0 for _ in range(len(text1) + 1)] for _ in range(len(text2) + 1)]

        for i in range(len(text2) - 1, -1, -1):
            for j in range(len(text1) - 1, -1, -1):
                a[i][j] = max(a[i + 1][j], a[i][j + 1], 1 + a[i + 1][j + 1] if text1[j] == text2[i] else 0)

        return a[0][0]


if __name__ == '__main__':
    print(Solution().longestCommonSubsequence(text1 = "abcde", text2 = "ace"))
    print(Solution().longestCommonSubsequence(text1 = "abc", text2 = "abc"))
    print(Solution().longestCommonSubsequence(text1 = "abc", text2 = "def"))
