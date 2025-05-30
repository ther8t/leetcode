import collections
import itertools


class Solution:

    # def kadane(self, nums):
    #     # [5, -1, 2, -10, 1, 4, -4, 6, 7]
    #     max_sum = -float('inf')
    #
    #     current_sum = 0
    #     for n in nums:
    #         current_sum = max(current_sum + n, n)
    #         max_sum = max(max_sum, current_sum)
    #
    #     return max_sum


    def largestVariance(self, s: str) -> int:
        counter = collections.Counter(s)

        def get_largest_variance(a, b):
            largest_variance = 0
            freq_a, freq_b = 0, 0
            remaining_a, remaining_b = counter[a], counter[b]
            for i, char in enumerate(s):
                if char != a and char != b:
                    continue
                if freq_a - freq_b < 0 and remaining_a and remaining_b:
                    freq_a = 0
                    freq_b = 0
                if char == a:
                    freq_a += 1
                    remaining_a -= 1
                if char == b:
                    freq_b += 1
                    remaining_b -= 1
                if freq_a > 0 and freq_b > 0:
                    largest_variance = max(largest_variance, freq_a - freq_b)
            return largest_variance

        largest_variance = 0
        for char_a, char_b in itertools.permutations(counter,2):
            if char_a == char_b:
                continue
            largest_variance = max(largest_variance, get_largest_variance(char_a, char_b))

        return largest_variance

    # def largestVariance(self, s: str) -> int:
    #     freq1 = 0
    #     freq2 = 0
    #     variance = 0
    #
    #     # create distinct list of character pairs
    #     pairs = [(l1, l2) for l1 in set(s) for l2 in set(s) if l1 != l2]
    #
    #     # run once for original string order, then again for reverse string order
    #     for runs in range(2):
    #         for pair in pairs:
    #
    #             for letter in s:
    #                 # no reason to process letters that aren't part of the current pair
    #                 if letter not in pair:
    #                     continue
    #                 if letter == pair[0]:
    #                     freq1 += 1
    #                 elif letter == pair[1]:
    #                     freq2 += 1
    #                 if freq1 < freq2:
    #                     freq1 = freq2 = 0
    #                 elif freq1 > 0 and freq2 > 0:
    #                     variance = max(variance, freq1 - freq2)
    #             freq1 = freq2 = 0
    #
    #         # reverse the string for the second time around
    #         s = s[::-1]
    #
    #     return variance

    # def largestVariance(self, s: str) -> int:
    #     alphabets = set(s)
    #     largest_variance = 0
    #
    #     def get_variance_for(a, b):
    #         max_variance = 0
    #         freq_a, freq_b = 0, 0
    #         for char in s:
    #             if char not in [a, b]:
    #                 continue
    #             freq_a += char == a
    #             freq_b += char == b
    #             if freq_a - freq_b < 0:
    #                 freq_a, freq_b = 0, 1
    #             if freq_a > 0 and freq_b > 0:
    #                 max_variance = max(max_variance, freq_a - freq_b)
    #
    #         return max_variance
    #
    #     get_variance_for("b", "a")
    #     # for i in range(len(alphabets) - 1):
    #     #     largest_variance = max(largest_variance, get_variance_for(s[i], s[i + 1]), get_variance_for(s[i + 1], s[i]))
    #
    #     return largest_variance


if __name__ == '__main__':
    print(Solution().largestVariance("aababbb"))
    # print(Solution().kadane([5, -1, 2, -10, 1, 4, -4, 6, 7]))


