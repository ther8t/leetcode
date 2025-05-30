import functools


class Solution:
    def wordBreak(self, s: str, wordDict):
        wordDict = set(wordDict)
        words = []

        def word_break(start, prev):
            if start == len(s):
                words.append(" ".join(prev))
            current_string = ""
            for i in range(start, len(s)):
                current_string += s[i]
                if current_string in wordDict:
                    word_break(i + 1, prev + [current_string])

        word_break(0, [])
        return words


    """
    Accepted 29%:
    This is an alternate to the previous question.
    """
    def wordBreak(self, s: str, wordDict):
        wordDict = set(wordDict)

        @functools.lru_cache(None)
        def dfs(index):
            if index == len(s):
                return [[]]
            builder = ""
            sentences = []
            for i in range(index, len(s)):
                builder += s[i]
                if builder in wordDict:
                    sub_sentences = dfs(i + 1)
                    for j in sub_sentences:
                        sentences.append([builder] + j)

            return sentences

        sentences = dfs(0)
        out = []
        for i in sentences:
            out.append(" ".join(i))

        return out





if __name__ == '__main__':
    print(Solution().wordBreak(s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]))
    print(Solution().wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]))
