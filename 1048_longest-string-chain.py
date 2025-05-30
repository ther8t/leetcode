import functools


class TreeNode:
     def __init__(self, val = ""):
         self.val = val
         self.children = []


class Solution:
    """
    Revision 2:
    I don't know what sort of sorcery I had conjured during my previous attempt to this question but I was able to solve this with a very easy DP and a sort of search I guess.
    This is simple, shorter, faster. The difference between 816 and 182ms faster.
    Accepted 88.3%
    """
    def longestStrChain(self, words):
        word_set = set(words)

        @functools.lru_cache(None)
        def longest_chain_length(word):
            if not word:
                return 0
            max_sub_word_chain_length = 0
            for i in range(len(word)):
                sub_word = word[:i] + word[i + 1:]
                if sub_word in word_set:
                    max_sub_word_chain_length = max(max_sub_word_chain_length, longest_chain_length(sub_word))
            return max_sub_word_chain_length + 1

        max_chain_length = 0
        for word in words:
            max_chain_length = max(max_chain_length, longest_chain_length(word))

        return max_chain_length



    # def longestStrChain(self, words):
    #     if len(words) == 0:
    #         return 0
    #
    #     def sortFunc(word):
    #         return len(word)
    #
    #     words.sort(key=sortFunc)
    #
    #
    #     root = None
    #     def insertNode(root, word):
    #         if root is None:
    #             return TreeNode(word)
    #         if self.isAPredecessorOfB(root.val, word):
    #             root.children.append(TreeNode(word))
    #         for child in root.children:
    #             insertNode(child, word)
    #         return root
    #
    #     for word in words:
    #         root = insertNode(root, word)
    #
    #     def findMaxDepth(root):
    #         if root is None:
    #             return 0
    #         maxDepth = 0
    #         for child in root.children:
    #             maxDepth = max(maxDepth, findMaxDepth(child))
    #         return maxDepth + 1
    #     return findMaxDepth(root)

    # def longestStrChain(self, words):
    #     if len(words) == 0:
    #         return 0
    #
    #     def sortFunc(word):
    #         return len(word)
    #
    #     words.sort(key=sortFunc)
    #
    #     counter = [1 for _ in range(len(words))]
    #
    #     for i in range(len(words)):
    #         currentMax = 1
    #         for j in range(i, -1, -1):
    #             if self.isAPredecessorOfB(words[j], words[i]):
    #                 currentMax = max(currentMax, counter[j] + 1)
    #         counter[i] = currentMax
    #
    #     maxChain = 0
    #     for i in counter:
    #         maxChain = max(maxChain, i)
    #     return maxChain



    # Accepted but could do better still - NO, I am happy to say that this solution is faster than 22% while the above solution is only 5% faster.
    # def longestStrChain(self, words):
    #     if len(words) == 0:
    #         return 0
    #
    #     def sortFunc(word):
    #         return len(word)
    #
    #     words.sort(key=sortFunc)
    #     sortedWordArray = []
    #     startingLength = len(words[0])
    #     subArray = []
    #     for i in range(len(words)):
    #         if len(words[i]) == startingLength:
    #             subArray.append([words[i], 1])
    #         else:
    #             sortedWordArray.append(subArray)
    #             startingLength = len(words[i])
    #             subArray = [[words[i], 1]]
    #     sortedWordArray.append(subArray)
    #
    #     for i in range(0, len(sortedWordArray) - 1):
    #         # compare (i) and (i+1)
    #         if len(sortedWordArray[i])>0 and len(sortedWordArray[i+1])>0 and len(sortedWordArray[i+1][0][0]) - len(sortedWordArray[i][0][0]) != 1:
    #             continue
    #         for j in range(len(sortedWordArray[i])):
    #             for k in range(len(sortedWordArray[i + 1])):
    #                 if self.isAPredecessorOfB(sortedWordArray[i][j][0], sortedWordArray[i+1][k][0]):
    #                     if sortedWordArray[i][j][1] + 1 > sortedWordArray[i+1][k][1]:
    #                         sortedWordArray[i+1][k][1] = sortedWordArray[i][j][1] + 1
    #
    #     maxChainLength = 0
    #     for i in range(len(sortedWordArray)):
    #         for j in range(len(sortedWordArray[i])):
    #             maxChainLength = max(maxChainLength, sortedWordArray[i][j][1])
    #
    #     return maxChainLength

    # Incorrect Solution
    # def longestStrChain(self, words):
    #     if len(words) == 0:
    #         return 0
    #
    #     def sortFunc(word):
    #         return len(word)
    #
    #     words.sort(key=sortFunc)
    #     print(words)
    #
    #     maxChainLength = 0
    #     for startingWordIndex in range(0, len(words)):
    #         startingWord = words[startingWordIndex]
    #         currentChainLength = 1
    #         for wordIndex in range(startingWordIndex, len(words)):
    #             if self.isAPredecessorOfB(startingWord, words[wordIndex]):
    #                 startingWord = words[wordIndex]
    #                 currentChainLength += 1
    #         maxChainLength = max(maxChainLength, currentChainLength)
    #     return maxChainLength

    def isAPredecessorOfB(self, a, b):
        if a == b:
            return False
        # a, b = (a, b) if len(a) <= len(b) else (b, a)
        index = 0
        while index < len(a) and index < len(b) and a[index] == b[index]:
            index += 1
        while index < len(a) and index + 1 < len(b) and a[index] == b[index + 1]:
            index += 1

        return True if index == len(a) and index + 1 == len(b) else False


if __name__ == '__main__':
    print(Solution().longestStrChain(["a", "ab", "ac", "bd", "abc", "abd", "abdd"]))
    print(Solution().longestStrChain(words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]))
    print(Solution().longestStrChain(words = ["abcd","dbqca"]))
