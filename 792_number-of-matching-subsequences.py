import collections


class Solution:
    # def numMatchingSubseq(self, s: str, words) -> int:
    #     word_ptr_map = {i: 0 for i in words}
    #     string_ptr = 0
    #     while string_ptr < len(s) and len(word_ptr_map) > 0:
    #         next_required_char = collections.defaultdict(list)
    #         for word in word_ptr_map:
    #             next_required_char[word[word_ptr_map[word]]].append(word)
    #         while string_ptr < len(s) and s[string_ptr] not in next_required_char:
    #             string_ptr += 1
    #         if string_ptr >= len(s):
    #             break
    #         check_char = s[string_ptr]
    #         for word in next_required_char[check_char]:
    #             word_ptr_map[word] += 1
    #             if word_ptr_map[word] == len(word):
    #                 del word_ptr_map[word]
    #         string_ptr += 1
    #
    #     not_match_count = 0
    #     for word in words:
    #         if word in word_ptr_map.keys():
    #             not_match_count += 1
    #
    #     return len(words) - not_match_count

    """
    Revision 2:
    I had come up with this algorithm but I could not think of using iterator which is a genius move. I was thinking more like (index, pointer) tuple.
    Although I had an idea of using a Trie Node as a possible alternative to the iterator but that would have meant putting all the words in Trie, which would have been time consuming, more than creating an iterator.
    """
    def numMatchingSubseq(self, S, words):
        ans = 0
        heads = [[] for _ in range(26)]
        for word in words:
            it = iter(word)
            heads[ord(next(it)) - ord('a')].append(it)

        for letter in S:
            letter_index = ord(letter) - ord('a')
            old_bucket = heads[letter_index]
            heads[letter_index] = []

            while old_bucket:
                it = old_bucket.pop()
                nxt = next(it, None)
                if nxt:
                    heads[ord(nxt) - ord('a')].append(it)
                else:
                    ans += 1

        return ans

    # TLE
    # def is_subsequence(self, string, possible_subsequence, string_starting_index):
    #     if len(string) < len(possible_subsequence):
    #         return False
    #     ptr_string = string_starting_index
    #     ptr_subsequence = 0
    #     while ptr_string < len(string) and ptr_subsequence < len(possible_subsequence):
    #         if string[ptr_string] == possible_subsequence[ptr_subsequence]:
    #             ptr_string += 1
    #             ptr_subsequence += 1
    #         else:
    #             ptr_string += 1
    #     return ptr_subsequence == len(possible_subsequence)
    #
    # def numMatchingSubseq(self, s: str, words) -> int:
    #     sorting_order = {chr(i + ord('a')): float('inf') for i in range(26)}
    #     for index, char in enumerate(s):
    #         if sorting_order[char] == float('inf'):
    #             sorting_order[char] = index
    #
    #     words.sort(key=lambda x: sorting_order[x[0]])
    #
    #     starting_index = 0
    #     matches = 0
    #     for index, word in enumerate(words):
    #         while starting_index<len(s) and s[starting_index] != word[0]:
    #             starting_index += 1
    #         if self.is_subsequence(s, word, starting_index):
    #             matches += 1
    #
    #     return matches


if __name__ == '__main__':
    print(Solution().numMatchingSubseq("vvvvvvvvvvvm", ["vm", "vm", "vm", "vm", "vn", "vn", "vn", "vn"]))
