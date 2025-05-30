import collections


class Solution:
    def palindromePairs(self, words):
        past_words = collections.defaultdict(list)
        def check_palindrome(w):
            for index, c in enumerate(w):
                if w[len(w) - 1 - index] != c:
                    return False
            return True

        ans = set()
        for index, w in enumerate(words):
            word_builder = ""
            for c in w:
                word_builder += c
                if word_builder in past_words:
                    for pw_index in past_words[word_builder]:
                        if check_palindrome(w + words[pw_index]):
                            ans.add((index, pw_index))
                            ans.add((pw_index, index))

            word_builder = ""
            for c in reversed(w):
                word_builder += c
                if word_builder in past_words:
                    for pw_index in past_words[word_builder]:
                        if check_palindrome(w + words[pw_index]):
                            ans.add((index, pw_index))
                            ans.add((pw_index, index))

            past_words[w].append(index)
            past_words[w[::-1]].append(index)

        return ans


if __name__ == '__main__':
    s = Solution()
    o = s.palindromePairs(["lls","s","sssll"])
    print(o)
