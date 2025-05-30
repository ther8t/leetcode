import collections


class Dictionary:

    def __init__(self, val):
        self.val = val
        self.isWord = False
        self.sub_dict = {chr(_ + ord('a')): None for _ in range(26)}

    def addWord(self, root, word):
        if not word:
            return root
        if not root:
            root = Dictionary("")

        iterator = root
        for char in word:
            if iterator.sub_dict[char] is None:
                newNode = Dictionary(char)
                iterator.sub_dict[char] = newNode
            iterator = iterator.sub_dict[char]
        iterator.isWord = True
        return root

    def searchWord(self, root, word):
        iterator = root
        for char in word:
            if iterator.sub_dict[char] is None:
                return False
            iterator = iterator.sub_dict[char]

        return iterator.isWord


class Solution:
    # def createHash(self, word, skipChar="#"):
    #     hash = 0
    #     for char in word:
    #         if char == skipChar:
    #             continue
    #         hash |= (1 << (ord(char) - 97))
    #     return hash
    #
    # def wordCount(self, startWords, targetWords) -> int:
    #     searchKeeper = set()
    #     for startWord in startWords:
    #         searchKeeper.add(self.createHash(startWord))
    #
    #     possibleTargetWordsCount = 0
    #     for targetWord in targetWords:
    #         for char in targetWord:
    #             hash = self.createHash(targetWord, char)
    #             if hash in searchKeeper:
    #                 possibleTargetWordsCount += 1
    #                 break
    #     return possibleTargetWordsCount


    # """
    # Revision 2 :
    # TLE
    # I thought comparing simple maps would do the trick. My logic was right but the time complexity is more.
    # My interpretation of the question was also wrong. The texts can differ only by one character.
    # """
    # def wordCount(self, startWords, targetWords) -> int:
    #     start_word_map = {}
    #     for word in startWords:
    #         start_word_map[word] = collections.Counter(word)
    #
    #     count = 0
    #     for target_word in targetWords:
    #         target_word_map = collections.Counter(target_word)
    #         for word in start_word_map:
    #             if len(target_word) - len(word) != 1:
    #                 continue
    #             is_match = True
    #             for char in start_word_map[word]:
    #                 if char not in target_word or target_word_map[char] < start_word_map[word][char]:
    #                     is_match = False
    #                     break
    #             if is_match:
    #                 count += 1
    #                 break
    #     return count

    # Accepted 15%
    def wordCount(self, startWords, targetWords) -> int:
        possibilities = set()

        def get_hash(word):
            hash = 0
            for char in word:
                power = ord(char) - ord('a')
                hash += pow(26, power)

            return hash

        for word in startWords:
            word_hash = get_hash(word)
            for char in range(26):
                possibilities.add(word_hash + pow(26, char))

        count = 0
        for word in targetWords:
            word = get_hash(word)
            if word in possibilities: count += 1

        return count


    def wordCount(self, startWords, targetWords) -> int:
        word_hash = set()
        for word in startWords:
            word_hash.add("".join(sorted(word)))

        count = 0
        for word in targetWords:
            for i in range(len(word)):
                if "".join(sorted(word[:i] + word[i + 1:])) in word_hash:
                    count += 1
                    break

        return count





    # # Simple Solution not mine
    # def wordCount(self, startWords, targetWords) -> int:
    #     se=set()
    #     for i in startWords:
    #         s=set(i)
    #         for j in range(26):
    #             j=chr(j+97)
    #             if j not in s:
    #                 s.add(j)
    #                 se.add("".join(sorted(s)))
    #                 s.remove(j)
    #     return sum("".join(sorted(i)) in se for i in targetWords)

    # def wordCount(self, startWords, targetWords) -> int:
    #     root = Dictionary("")
    #     for startWord in startWords:
    #         sortedStartWord = sorted(startWord)
    #         root.addWord(root, sortedStartWord)
    #
    #     possibleTargetWordsCount = 0
    #     for targetWord in targetWords:
    #         sortedTargetWord = sorted(targetWord)
    #         isFound = False
    #         iterator = root
    #         for missingCharIndex in range(len(sortedTargetWord)):
    #             wordToSearch = sortedTargetWord[0:missingCharIndex] + sortedTargetWord[missingCharIndex + 1:]
    #             if iterator.searchWord(iterator, wordToSearch):
    #                 isFound = True
    #                 break
    #         if isFound:
    #             possibleTargetWordsCount += 1
    #     return possibleTargetWordsCount

    # def wordCount(self, startWords, targetWords) -> int:
    #     root = Dictionary("")
    #     for startWord in startWords:
    #         sortedStartWord = sorted(startWord)
    #         root.addWord(root, sortedStartWord)
    #
    #     possibleTargetWordsCount = 0
    #     for targetWord in targetWords:
    #         isSkipped = False
    #         sortedTargetWord = sorted(targetWord)
    #         canBeFormed = False
    #         iterator = root
    #         stringMatchedSoFar = ""
    #         for index, char in enumerate(sortedTargetWord):
    #             if iterator is None:
    #                 break
    #             if iterator.sub_dict[char] is not None:
    #                 iterator = iterator.sub_dict[char]
    #                 stringMatchedSoFar += iterator.val
    #                 if index == len(sortedTargetWord) - 1 and iterator.isWord:
    #                     canBeFormed = True
    #                 continue
    #             else:
    #                 if not isSkipped:
    #                     if stringMatchedSoFar.find(char) == -1:
    #                         isSkipped = True
    #                         if index == len(sortedTargetWord) - 1 and iterator.isWord:
    #                             canBeFormed = True
    #                         continue
    #                     else:
    #                         canBeFormed = False
    #                         break
    #                 # reached the end of match
    #                 if isSkipped:
    #                     canBeFormed = False
    #                     break
    #         if canBeFormed and isSkipped:
    #             possibleTargetWordsCount += 1
    #     return possibleTargetWordsCount

    # # TLE
    # def wordCount(self, startWords, targetWords) -> int:
    #     # prep
    #     lenCountMap = collections.defaultdict(list)
    #     charMap = collections.defaultdict(dict)
    #
    #     for startWord in startWords:
    #         lenCountMap[len(startWord)].append(startWord)
    #         startWordCharMap = collections.defaultdict(int)
    #         for i in startWord:
    #             startWordCharMap[i] += 1
    #         charMap[startWord] = startWordCharMap
    #
    #     possibleTargetWordsCount = 0
    #     for targetWord in targetWords:
    #         targetWordLen = len(targetWord)
    #         startWordPossibleMatch = lenCountMap[targetWordLen - 1]
    #         for possibleMatch in startWordPossibleMatch:
    #             possibleMatchCharMap = charMap[possibleMatch]
    #             additionalChar = ""
    #             isMatch = True
    #             for targetWordChar in targetWord:
    #                 if possibleMatchCharMap[targetWordChar] == 1:
    #                     continue
    #                 else:
    #                     if not additionalChar:
    #                         additionalChar = targetWordChar
    #                     else:
    #                         isMatch = False
    #                         break
    #             if isMatch:
    #                 possibleTargetWordsCount += 1
    #                 break
    #     return possibleTargetWordsCount


if __name__ == '__main__':
    print(Solution().wordCount(startWords=["ant", "act", "tack"], targetWords=["tack", "act", "acti"]))
    print(Solution().wordCount(startWords=["ab", "a"], targetWords=["abc", "abcd"]))
    # a = {chr(_ + ord('a')): None for _ in range(26)}
    # a = "tack"
    # b = sorted(a)
    # print(str(b))
    # a = (0b100 & (~0b100))
    # print(a)
