import collections

Trie = lambda: collections.defaultdict(Trie)
WORD = "WORD"

class WordDictionary:

    def __init__(self):
        self.t = Trie()

    def addWord(self, word: str) -> None:
        temp = self.t
        for c in word:
            temp = temp[c]
        temp[WORD] = True

    def search(self, word: str) -> bool:
        def dfs(t, w):
            if not w:
                return WORD in t

            if w[0] == ".":
                for c in t:
                    if c != WORD:
                        if dfs(t[c], w[1:]):
                            return True
            else:
                return dfs(t[w[0]], w[1:])
        return dfs(self.t, word)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


if __name__ == '__main__':
    wordDictionary = WordDictionary()
    print(wordDictionary.addWord("bad"))
    print(wordDictionary.addWord("dad"))
    print(wordDictionary.addWord("mad"))
    print(wordDictionary.search("pad"))
    print(wordDictionary.search("bad"))
    print(wordDictionary.search(".ad"))
    print(wordDictionary.search("b.."))
