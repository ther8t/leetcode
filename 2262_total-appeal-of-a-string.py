import collections


class Solution:
    # Same overall logic compressed/simplified using one pass.
    def appealSum(self, s: str) -> int:
        prev_char = {chr(i + ord('a')): -1 for i in range(26)}

        ans = 0
        for i in range(len(s)):
            ans += (len(s) - i) * (i - prev_char[s[i]])
            prev_char[s[i]] = i

        return ans

    # # Accepted : 5%
    # def appealSum(self, s: str) -> int:
    #     n = len(s)
    #     all_substrings_count = n * (n + 1) // 2
    #     char_map = collections.defaultdict(list)
    #     for index, char in enumerate(s):
    #         char_map[char].append(index)
    #
    #     ans = 0
    #     for char in char_map:
    #         summation = 0
    #         for i, char_index in enumerate(char_map[char]):
    #             if i == 0:
    #                 l = char_index
    #             else:
    #                 l = char_map[char][i] - char_map[char][i - 1] - 1
    #             summation += l * (l + 1) // 2
    #             if i == len(char_map[char]) - 1:
    #                 r = n - char_index - 1
    #                 summation += r * (r + 1) // 2
    #         ans += (all_substrings_count - summation)
    #
    #     return ans

    """
    Attempt: Fired
    Accepted: 59%
    
    The logic behind this is simple. We need to find out what contribution does each character have in the overall answer.
    Each character contributes 1 length to each string it is unique in. So consider abbc, the first 'b' contributes to 1 length in ab, b, bb, bbc, abb, abbc. This means that second b cant be considered in the strings where first b occurs.
    So second b's contribution is in b, bc (2 strings: 2 length contribution)
    We can either find out the next similar to limit our contributions and multiply that by position. OR
    Better yet find the previous similar to limit our contribution and multiply by the remaining.
    
    There is a little caveat to it. This may seem simple but there another fact to consider here. While counting the contribution one character has in the entire answer, find ourselves counting the number of string, which can cause us to ovelap with the string which have similar characters.
    What we have essentially done in this is to calculate the strings which on the left side do not have the same character. And on the right have have all the characters.
    This can also be done the other way round. For that we will need to find the next occurance of the character but with the previous we have to run just one loop.
    So this is like calculating strictly one 'b' on the left side and any number of b's on the right side.
    """
    def appealSum(self, s: str) -> int:
        prev_char = {chr(i + ord('a')): -1 for i in range(26)}

        ans = 0
        for i in range(len(s)):
            ans += (len(s) - i) * (i - prev_char[s[i]])
            prev_char[s[i]] = i

        return ans


if __name__ == '__main__':
    print(Solution().appealSum(s = "abbca"))
    print(Solution().appealSum(s = "code"))
