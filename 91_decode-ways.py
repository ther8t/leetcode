import functools


class Solution:
    """
    Attempt: Fired
    Accepted: 10%
    """
    def numDecodings(self, s: str) -> int:
        n = len(s)

        @functools.lru_cache(None)
        def dfs(index):
            if index == len(s):
                return 1
            if s[index] == "0":
                return 0
            if s[index] in {"1", "2"} and index + 1 < n and s[index + 1] == "0":
                return 1 * dfs(index + 2)
            if index + 1 < n and (s[index] == "1" or (s[index] == "2" and 1 <= int(s[index + 1]) <= 6)):
                return dfs(index + 2) + dfs(index + 1)
            return 1 * dfs(index + 1)

        return dfs(0)



if __name__ == '__main__':
    print(Solution().numDecodings("12"))
    print(Solution().numDecodings(s = "226"))
    print(Solution().numDecodings(s = "06"))
    print(Solution().numDecodings(s = "27"))

