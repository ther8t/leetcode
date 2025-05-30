class Solution:
    def findAndReplacePattern(self, words, pattern: str):
        ans = []
        for word in words:
            word_map, pattern_map = {}, {}
            is_match = True
            for w, p in zip(word, pattern):
                if w not in word_map: word_map[w] = p
                if p not in pattern_map: pattern_map[p] = w
                if (pattern_map[p], word_map[w]) != (w, p):
                    is_match = False
                    break

            if is_match: ans.append(word)

        return ans


if __name__ == '__main__':
    print(Solution().findAndReplacePattern(words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"))
    print(Solution().findAndReplacePattern(words = ["a","b","c"], pattern = "a"))
