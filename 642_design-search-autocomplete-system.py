import collections
import re


class Trie:
    def __init__(self):
        self.children = {}
        self.is_sentence = False
        self.hotness = 0

    def add_sentence(self, sentence, hotness):
        root = self
        for char in sentence:
            if char not in root.children:
                root.children[char] = Trie()
            root = root.children[char]
        root.hotness += hotness
        root.is_sentence = True

    def all_sentences(self, root, stack):
        sentences = {}
        if root.is_sentence:
            sentences["".join(stack)] = root.hotness
        for child in root.children:
            stack.append(child)
            sentences.update(self.all_sentences(root.children[child], stack))
            stack.pop()
        return sentences

    def search(self, partial_sentence):
        root = self
        for char in partial_sentence:
            if char in root.children:
                root = root.children[char]
            else:
                return []
        sentences = self.all_sentences(root, [partial_sentence])
        sorted_sentences = sorted(sentences, key=lambda x: (-1*sentences[x], x))
        return sorted_sentences



class AutocompleteSystem:

    def __init__(self, sentences, times):
        self.trie_root = Trie()
        self.partial_sentence = ""

        for i in range(len(sentences)):
            self.trie_root.add_sentence(sentences[i], times[i])


    def input(self, c: str):
        if c == "#":
            self.trie_root.add_sentence(self.partial_sentence, 1)
            self.partial_sentence = ""
            return []
        self.partial_sentence += c
        return self.trie_root.search(self.partial_sentence)[0:3]


# # Accepted : 18%
# class AutocompleteSystem:
#
#     def __init__(self, sentences, times):
#         self.sentence_hotness_map = collections.defaultdict(int)
#         for i in range(len(sentences)):
#             self.sentence_hotness_map[sentences[i]] = times[i]
#         self.cache = self.sentence_hotness_map.copy()
#         self.partial_string = ""
#
#     def input(self, c: str):
#         if c == "#":
#             self.sentence_hotness_map[self.partial_string] += 1
#             self.partial_string = ""
#             self.cache = self.sentence_hotness_map.copy()
#             return []
#         self.partial_string += c
#         for sentences in self.cache.copy():
#             if not re.match("^" + self.partial_string + ".*$", sentences):
#                 del self.cache[sentences]
#         sorted_cache = sorted(self.cache,
#                               key=lambda x: (-1*self.cache[x], x))
#         return list(sorted_cache)[0:3]


# Your AutocompleteSystem object will be instantiated and called as such:
obj = AutocompleteSystem(["abc","abbc","a"],[3,3,3])
print(obj.input("b"))
print(obj.input("c"))
print(obj.input("#"))
print(obj.input("b"))
print(obj.input("c"))
print(obj.input("#"))
print(obj.input("a"))
print(obj.input("b"))
print(obj.input("c"))
print(obj.input("#"))
print(obj.input("a"))
print(obj.input("b"))
print(obj.input("c"))
print(obj.input("#"))
