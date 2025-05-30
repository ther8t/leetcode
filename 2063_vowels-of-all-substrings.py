class Solution:
    def countVowels(self, word: str) -> int:
        return sum([(len(word) - i) * (i + 1) if word[i] in {'a', 'e', 'i', 'o', 'u'} else 0 for i in range(len(word))])


if __name__ == '__main__':
    print(Solution().countVowels(word = "aba"))
    print(Solution().countVowels(word = "abc"))
    print(Solution().countVowels(word = "ltcd"))
