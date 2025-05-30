import collections

import collection as collection


class Solution:
    # def findSubstring(self, s, words):
    #     n = len(s)
    #     k = len(words)
    #     word_length = len(words[0])
    #     substring_size = word_length * k
    #     word_count = collections.Counter(words)
    #
    #     def sliding_window(left):
    #         words_found = collections.defaultdict(int)
    #         words_used = 0
    #         excess_word = False
    #
    #         # Do the same iteration pattern as the previous approach - iterate
    #         # word_length at a time, and at each iteration we focus on one word
    #         for right in range(left, n, word_length):
    #             if right + word_length > n:
    #                 break
    #
    #             sub = s[right: right + word_length]
    #             if sub not in word_count:
    #                 # Mismatched word - reset the window
    #                 words_found = collections.defaultdict(int)
    #                 words_used = 0
    #                 excess_word = False
    #                 left = right + word_length  # Retry at the next index
    #             else:
    #                 # If we reached max window size or have an excess word
    #                 while right - left == substring_size or excess_word:
    #                     # Move the left bound over continously
    #                     leftmost_word = s[left: left + word_length]
    #                     left += word_length
    #                     words_found[leftmost_word] -= 1
    #
    #                     if words_found[leftmost_word] == word_count[leftmost_word]:
    #                         # This word was the excess word
    #                         excess_word = False
    #                     else:
    #                         # Otherwise we actually needed it
    #                         words_used -= 1
    #
    #                 # Keep track of how many times this word occurs in the window
    #                 words_found[sub] += 1
    #                 if words_found[sub] <= word_count[sub]:
    #                     words_used += 1
    #                 else:
    #                     # Found too many instances already
    #                     excess_word = True
    #
    #                 if words_used == k and not excess_word:
    #                     # Found a valid substring
    #                     answer.append(left)
    #
    #     answer = []
    #     for i in range(word_length):
    #         sliding_window(i)
    #
    #     return answer

    def findSubstring(self, s, words):
        if not s or not words:
            return []
        wordCharLength = len(words[0])
        wordCount = len(words)
        iterationLength = wordCharLength * wordCount

        subStringsStartingIndexArray = []
        for subStringStartingIndex in range(0, len(s)):
            subString = s[subStringStartingIndex: subStringStartingIndex + iterationLength]

            if len(subString) < iterationLength:
                break

            if self.isMatch(subString, words.copy()):
                subStringsStartingIndexArray.append(subStringStartingIndex)

        return subStringsStartingIndexArray

    # This is an alternate solution to the same problem. This is done by skipping wordCharLength each time and to ensure every permutation is taken care of we differ the starting address.
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        wordCharLength = len(words[0])
        wordCount = len(words)
        iterationLength = wordCharLength * wordCount

        a = []
        for i in range(wordCharLength):
            subStringsStartingIndexArray = []
            for subStringStartingIndex in range(i, len(s), wordCharLength):
                subString = s[subStringStartingIndex: subStringStartingIndex + iterationLength]

                if len(subString) < iterationLength:
                    break

                if self.isMatch(subString, words.copy()):
                    subStringsStartingIndexArray.append(subStringStartingIndex)
            a += subStringsStartingIndexArray

        return a

    def isMatch(self, s, words):
        if not s or not words:
            return []
        wordCharLength = len(words[0])

        for subStringStartingIndex in range(0, len(s), wordCharLength):
            subString = s[subStringStartingIndex: subStringStartingIndex + wordCharLength]
            try:
                words.remove(subString)
            except:
                return False

        return True if len(words) == 0 else False


    def findSubstring(self, s, words):
        if not s or not words:
            return []

        wordCharLength = len(words[0])
        wordCount = len(words)
        iterationLength = wordCharLength * wordCount

        original_counter = collections.Counter(words)
        iteration_counter = collections.Counter()
        word_set = original_counter.copy()
        out = []

        for i in range(wordCount):
            current_word = s[i * wordCharLength: (i + 1) * wordCharLength]
            iteration_counter[current_word] += 1
            if current_word in original_counter:
                original_counter[current_word] -= 1
                if original_counter[current_word] == 0:
                    del original_counter[current_word]

        if not original_counter:
            out.append(0)

        for ptr in range(len(s)):
            if ptr + iterationLength >= len(s):
                break
            current_starting_word = s[ptr: ptr + wordCharLength]
            current_ending_word = s[ptr + iterationLength : ptr + iterationLength + wordCharLength]
            if current_starting_word in iteration_counter and iteration_counter[current_starting_word] > 0:
                iteration_counter[current_starting_word] -= 1
                if iteration_counter[current_starting_word] + original_counter[current_starting_word] < word_set[current_starting_word]:
                    original_counter[current_starting_word] += 1
            iteration_counter[current_ending_word] += 1
            if current_ending_word in original_counter:
                original_counter[current_ending_word] -= 1
                if original_counter[current_ending_word] == 0:
                    del original_counter[current_ending_word]
            if not original_counter:
                out.append((ptr + 1))

        return out






if __name__ == '__main__':
    print(Solution().findSubstring(s = "barfoothefoobarman", words = ["foo","bar"]))
    # print(Solution().findSubstring(s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]))
    # print(Solution().findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))
    # print(Solution().findSubstring("aaaaaaaaaaaaaa", ["aa","aa"]))
    # print(Solution().findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"]))
