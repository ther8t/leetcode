import collections


class Solution:
    def wordSubsets(self, words1, words2):
        combined_word2 = collections.defaultdict(int)

        for word in words2:
            counter = collections.Counter(word)
            for char in counter:
                if combined_word2[char] < counter[char]:
                    combined_word2[char] = counter[char]

        out = []
        for word in words1:
            counter = collections.Counter(word)
            is_universal = True
            for char in combined_word2:
                if char not in counter or counter[char] < combined_word2[char]:
                    is_universal = False
                    break

            if is_universal:
                out.append(word)

        return out


if __name__ == '__main__':
    print(Solution().wordSubsets(words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]))


