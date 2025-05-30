import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        n, word_size = len(wordList), len(wordList[0])
        island_word_map = collections.defaultdict(set)

        for j in range(word_size):
            for i in range(n):
                word = list(wordList[i])
                word[j] = "*"
                island_name = "".join(word)
                island_word_map[island_name].add(wordList[i])

        visited = set()

        queue = [(beginWord, 1)]
        visited.add(beginWord)

        while queue:
            current_word, distance = queue.pop(0)

            for i in range(word_size):
                current_word_split = list(current_word)
                current_word_split[i] = "*"
                island_name = "".join(current_word_split)
                for e in island_word_map[island_name]:
                    if e == endWord:
                        return distance + 1
                    if e not in visited:
                        visited.add(e)
                        queue.append((e, distance + 1))

        return 0

    # # TLE
    # def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
    #     map = collections.defaultdict(set)
    #
    #     def diff(word1, word2):
    #         diff_count = 0
    #         for w1, w2 in zip(word1, word2):
    #             if w1 != w2:
    #                 diff_count += 1
    #             if diff_count > 1:
    #                 return False
    #         return True
    #
    #     for i in range(len(wordList)):
    #         if diff(beginWord, wordList[i]):
    #             map[beginWord].add(wordList[i])
    #         for j in range(i + 1, len(wordList)):
    #             word1, word2 = wordList[i], wordList[j]
    #             if diff(word1, word2):
    #                 map[word1].add(word2)
    #                 map[word2].add(word1)
    #
    #     visited = set()
    #
    #     queue = [(beginWord, 1, [beginWord])]
    #     visited.add(beginWord)
    #
    #     while queue:
    #         current_word, distance, stack = queue.pop(0)
    #
    #         for e in map[current_word]:
    #             if e == endWord:
    #                 return distance + 1
    #             if e not in visited:
    #                 visited.add(e)
    #                 queue.append((e, distance + 1, stack + [e]))
    #
    #     return 0


if __name__ == '__main__':
    print(Solution().ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))
