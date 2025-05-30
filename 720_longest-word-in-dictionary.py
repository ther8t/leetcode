import collections

Trie = lambda: collections.defaultdict(Trie)
IS_WORD = "@"


class Solution:
    def longestWord(self, words) -> str:
        trie = Trie()
        words.sort(key=len)

        def add_word(word):
            temp = trie
            for i, char in enumerate(word):
                if char in temp:
                    temp = temp[char]
                else:
                    if i == len(word) - 1:
                        temp[char][IS_WORD] = True
                        return True
                    else:
                        return False
            return True

        ans = ""
        for word in words:
            can_build = add_word(word)
            if can_build:
                if len(word) > len(ans) or word < ans:
                    ans = word

        return ans


if __name__ == '__main__':
    print(Solution().longestWord(words = ["w","wo","wor","worl","world"]))
