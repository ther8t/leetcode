import collections

Triee = lambda : collections.defaultdict(Triee)
WORD = "WORD"

class Trie:

    def __init__(self):
        self.trie = Triee()

    def insert(self, word: str) -> None:
        temp = self.trie
        for c in word:
            temp = temp[c]
        temp[WORD] = True

    def search(self, word: str) -> bool:
        temp = self.trie
        for c in word:
            if c not in temp:
                return False
            temp = temp[c]
        return WORD in temp

    def startsWith(self, prefix: str) -> bool:
        temp = self.trie
        for c in prefix:
            if c not in temp:
                return False
            temp = temp[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == '__main__':
    trie = Trie()
    print(trie.insert("hello"))
    print(trie.search("hell"))
    print(trie.search("helloa"))
    print(trie.search("hello"))
    print(trie.startsWith("hell"))
    print(trie.startsWith("helloa"))
    print(trie.startsWith("hello"))
