class Solution:
    """
    Accepted :
    The solution goes something like this.

    """
    def longestSubsequence(self, s: str, k: int) -> int:
        number = 0
        base = 1
        max_len = 0
        for char in reversed(s):
            if char == '1':
                if number + base <= k:
                    number += base
                    max_len += 1
                    base *= 2
            else:
                max_len += 1
                base *= 2
        return max_len



    # """
    # The idea was similar to the longest increasing subsequence. It was to add a new character if it is possible otherwise just try and place the character in some other place where it would still create a number which is less than or equal to k.
    # Wrong Answer. Why? It was a really long string and I didn't want to spend as much time to figure out.
    # """
    # def longestSubsequence(self, s: str, k: int) -> int:
    #     number = 0
    #     max_len_seq_size = 0
    #     current_seq = collections.deque()
    #     for char in s:
    #         if number * 2 + int(char) <= k:
    #             current_seq.append(char)
    #             number = number * 2 + int(char)
    #             max_len_seq_size = max(max_len_seq_size, len(current_seq))
    #             continue
    #         else:
    #             if char == "0":
    #                 index = current_seq.index("1")
    #                 number -= pow(2, len(current_seq) - index - 1)
    #                 current_seq[index] = "0"
    #     return max_len_seq_size


if __name__ == '__main__':
    print(Solution().longestSubsequence(s = "1001010", k = 5))
    print(Solution().longestSubsequence(s = "00101001", k = 1))
    print(Solution().longestSubsequence("111100010000011101001110001111000000001011101111111110111000011111011000010101110100110110001111001001011001010011010000011111101001101000000101101001110110000111101011000101", 11713332))

