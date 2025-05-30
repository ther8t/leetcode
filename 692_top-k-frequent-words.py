import collections


class Solution:
    def topKFrequent(self, words, k: int):
        word_counter = collections.Counter(words)
        return list(reversed(sorted(word_counter, key=lambda x: (-word_counter[x], x), reverse=True)[-k:]))


if __name__ == '__main__':
    print(Solution().topKFrequent(words = ["i","love","leetcode","i","love","coding"], k = 2))
    print(Solution().topKFrequent(words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4))
