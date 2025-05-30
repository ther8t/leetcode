import collections

Trie = lambda: collections.defaultdict(Trie)
IS_WORD = "@"


class StreamChecker:

    def __init__(self, words):
        self.trie = Trie()
        for word in words:
            temp = self.trie
            for char in word[::-1]:
                temp = temp[char]
            temp[IS_WORD] = True
        self.searched_nodes = []

    def query(self, letter: str) -> bool:
        self.searched_nodes.append(letter)
        temp = self.trie
        for char in reversed(self.searched_nodes):
            if char not in temp:
                return False
            temp = temp[char]
            if IS_WORD in temp:
                return True
        return False

    # def query(self, letter: str) -> bool:
    #     out = []
    #     is_word = False
    #     for node in self.searched_nodes + [self.trie]:
    #         if letter in node:
    #             out.append(node[letter])
    #             is_word = is_word or (IS_WORD in node[letter])
    #     self.searched_nodes = out
    #     return is_word



# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
if __name__ == '__main__':
    s = StreamChecker(["cd", "f", "kl"])
    print(s.query("a"))
    print(s.query("b"))
    print(s.query("c"))
    print(s.query("d"))
    print(s.query("e"))
    print(s.query("f"))
    print(s.query("g"))
    print(s.query("h"))
    print(s.query("i"))
    print(s.query("j"))
    print(s.query("k"))
    print(s.query("l"))
