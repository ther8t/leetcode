import functools


class Solution:
    # This is a genius solution to the problem statement.
    def encode(self, s: str) -> str:
        dp = {}

        def dfs(s):
            if s not in dp:
                # Absolutely love this line of code. ↓
                min_pattern_length_which_covers_the_whole_string = length = (s + s).find(s, 1)
                encoded = str(len(s) // length) + "[" + s[0:length] + "]" if len(
                    str(len(s) // length) + "[" + s[0:length] + "]") < len(s) else s
                further_encoding = [dfs(encoded[0:i]) + dfs(encoded[i:]) for i in range(1, len(encoded))]
                dp[s] = min(further_encoding + [encoded], key=len)
            return dp[s]

        return dfs(s)

    # # TLE : There is nothing much to complain about. It was an elegant solution.
    # def encode(self, s: str) -> str:
    #     string_map = {}
    #     for rank in range(1, len(s) // 2 + 1):
    #         for starting_pos in range(0, len(s) - rank + 1):
    #             new_string = s[starting_pos: starting_pos + rank]
    #             new_string_freq = 0
    #             ptr = starting_pos
    #             while ptr + rank <= len(s):
    #                 if s[ptr: ptr + rank] == new_string:
    #                     new_string_freq += 1
    #                     ptr = ptr + rank
    #                 else:
    #                     break
    #             encoded_string = str(new_string_freq) + "[" + new_string + "]"
    #             space_saved = new_string_freq * len(new_string) - len(encoded_string)
    #             if (new_string not in string_map and space_saved > 0):
    #                 string_map[new_string] = (new_string, starting_pos, new_string_freq, space_saved)
    #
    #     string_map = list(string_map.values())
    #     string_map.sort(key=lambda x: x[3], reverse=True)
    #
    #     min_encoded_string = s
    #     for string, starting_pos, freq, saved in string_map:
    #         replaced_s = s[0:starting_pos] + (str(freq) + "[" + string + "]") + s[starting_pos + freq * len(string):]
    #         ultimate_encoded_s = self.encode(replaced_s)
    #         if len(ultimate_encoded_s) < len(min_encoded_string):
    #             min_encoded_string = ultimate_encoded_s
    #     return min_encoded_string

    # # Wrong Answer: i had a confusion if the question was asking about a string or a single character. I had guessed correctly that it was a string but I had to check
    # def encode(self, s: str) -> str:
    #     ptrl = 0
    #     ptrr = 0
    #     output_str = ""
    #     while ptrl < len(s):
    #         while ptrr < len(s) and s[ptrr] == s[ptrl]:
    #             ptrr += 1
    #
    #         encoded = str(ptrr - ptrl) + "[" + s[ptrl] + "]"
    #         if len(encoded) < (ptrr - ptrl):
    #             output_str += encoded
    #         else:
    #             output_str += s[ptrl:ptrr]
    #         ptrl = ptrr
    #
    #     return output_str

    @functools.lru_cache(None)
    def encode(self, s: str) -> str:
        length = (s + s).find(s, 1)
        encoded = str(len(s) // length) + "[" + s[0:length] + "]" if len(str(len(s) // length) + "[" + s[0:length] + "]") < len(s) else s
        return min([self.encode(encoded[0: i]) + self.encode(encoded[i:]) for i in range(1, len(encoded))] + [encoded], key=len)


if __name__ == '__main__':
    print(Solution().encode("abaabcabcabc"))
    # s = "abcabcabc"
    # print((s+s).find(s, 1))
