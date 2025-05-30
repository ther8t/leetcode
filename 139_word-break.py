class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        wordDict = set(wordDict)
        queue = [0]
        visited = set()

        while queue:
            start = queue.pop(0)
            if start in visited:
                continue

            visited.add(start)
            for end in range(start + 1, len(s) + 1):
                if s[start: end] in wordDict:
                    queue.append(end)
                    if end == len(s):
                        return True

        return False


    """
    Revision 2:
    The question is easy. The reason I am writing this is that my first instinct was to go for the recursive solution. It's not as effective because it repeats certain function calls.
    There are three ways to solve this:
    1. Recursive with @lru_cache(None). This prevents repeat function calls.
    2. Using dp as below. This is exactly the same as using @lru_cache(None).
    3. Using Queue : Something which I remember clearly I figured out much later and was like a sunshine on a cloudy day, an idea which I could not fathom why I could not figure out.
       It eliminates all the possibilities of a repeated function call. It's like BFS.
    """

    # Accepted Using DP
    def wordBreak(self, s: str, wordDict) -> bool:
        wordDict = set(wordDict)
        dp = [None] * len(s)

        def break_word(index):
            if index == len(s):
                return True
            if dp[index] != None:
                return dp[index]

            builder = ""
            for char_index in range(index, len(s)):
                builder += s[char_index]
                if builder in wordDict and break_word(char_index + 1):
                    dp[index] = True
                    return True
            dp[index] = False
            return False
        break_word(0)
        return dp[0]


if __name__ == '__main__':
    print(Solution().wordBreak(s = "leetcode", wordDict = ["leet","code"]))
    print(Solution().wordBreak(s = "applepenapple", wordDict = ["apple","pen"]))
    print(Solution().wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]))
    print(Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
