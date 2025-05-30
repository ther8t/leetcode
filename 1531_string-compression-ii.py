from functools import lru_cache


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def dp(index, last_char, last_char_count, k):
            if k < 0:
                return float('inf')
            if index == len(s):
                return 0
            delete_score = dp(index + 1, last_char, last_char_count, k - 1)
            if s[index] == last_char:
                keep_score = dp(index + 1, last_char, last_char_count + 1, k) + (last_char_count in [1, 9, 99])
            else:
                keep_score = dp(index + 1, s[index], 1, k) + 1

            return min(delete_score, keep_score)

        return dp(0, "", 0, k)


    """
    Revision 2:
    Simply understood the code. Revisit this again. I am marking this as revise.
    """
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def dp(index, last_char, last_char_count, k):
            if k < 0:
                return float('inf')
            if index == len(s):
                return 0
            if s[index] == last_char:
                keep = dp(index + 1, last_char, last_char_count + 1, k) + (last_char_count in {1, 9, 99})
            else:
                keep = dp(index + 1, s[index], 1, k) + 1
            delete = dp(index + 1, last_char, last_char_count, k - 1)

            return min(keep, delete)

        return dp(0, "", 0, k)



    # # Wrong Answer
    # def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
    #     def compress(s):
    #         n = len(s)
    #         ptr1, ptr2 = 0, 0
    #         builder = ""
    #         while ptr1 < n and ptr2 < n:
    #             ptr2 = ptr1
    #             while ptr2 < n and s[ptr2] == s[ptr1]:
    #                 ptr2 += 1
    #             builder += (s[ptr1] + (str(ptr2 - ptr1) if ptr2 - ptr1 > 1 else ""))
    #             ptr1 = ptr2
    #         return len(builder)
    #
    #     while k > 0:
    #         n = len(s)
    #         current_string_score = compress(s)
    #         current_max_diff = 0
    #         del_range_beg, del_range_end = -1, -1
    #
    #         for i, char in enumerate(s):
    #             if i + 1 < n and s[i + 1] != s[i]:
    #                 # search for the same character forwards
    #                 ptr1, ptr2 = i + 1, i + 1
    #                 max_diff = 0
    #                 max_ptr = i + 1
    #                 while ptr1 < n and ptr2 < n:
    #                     while ptr1 < n and s[ptr1] != s[i]:
    #                         ptr1 += 1
    #                     if ptr1 - i - 1 <= k:
    #                         score = compress(s[:i + 1] + s[ptr1:])
    #                         if current_string_score - score > max_diff:
    #                             max_diff = current_string_score - score
    #                             max_ptr = ptr1
    #                     ptr2 = ptr1
    #                     while ptr2 < n and s[ptr2] == s[ptr1]:
    #                         ptr2 += 1
    #                     ptr1 = ptr2
    #                 if current_max_diff < max_diff:
    #                     current_max_diff = max_diff
    #                     del_range_beg, del_range_end = i + 1, max_ptr
    #
    #         if current_max_diff > 0:
    #             s = s[:del_range_beg] + s[del_range_end:]
    #             k -= (del_range_end - del_range_beg)
    #         else:
    #             break
    #
    #         # # try removing those that can make a difference because of their length a10 -> a9, a5 -> nothing,
    #         # while k:
    #
    #     ptr1, ptr2 = 0, 0
    #     while k:
    #         while ptr1 < len(s) and ptr2 < len(s):
    #             ptr2 = ptr1
    #             while ptr2 < len(s) and s[ptr2] == s[ptr1]:
    #                 ptr2 += 1
    #             match_length = ptr2 - ptr1
    #             length_after_removal = match_length - min(match_length, k)
    #             if (match_length and length_after_removal == 0) or (match_length >= 2 and length_after_removal <= 1) or (match_length >=10 and length_after_removal < 10) or (match_length >= 100 and length_after_removal < 100):
    #                 s = s[:ptr1 - 1] + s[ptr1 + min(match_length, k):]
    #                 k -= min(match_length, k)
    #             ptr1 = ptr2
    #
    #     return compress(s)

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        @lru_cache(None)
        def compress(index, stack, remaining_k):
            if remaining_k == 0 or index == len(s):
                temp_s = stack
                i = index
                while i < len(s):
                    if not temp_s or temp_s[-1][0] != s[i]:
                        temp_s.append((s[i], 0))
                    temp_s[-1] = (temp_s[-1][0], temp_s[-1][1] + 1)
                    i += 1

                return len("".join([c + (str(count) if count > 1 else "") for c, count in temp_s]))

            i = index
            while i < len(s) and s[i] == s[index]:
                i += 1

            count = i - index
            if stack and stack[-1][0] == s[index]:
                count += stack[-1][1]

            min_len = float('inf')
            for r in range(min(remaining_k, count), -1, -1):
                if remaining_k - r >= 0:
                    min_len = min(min_len, compress(i, stack + ([(s[index], count - r)] if count - r > 0 else []), remaining_k - r))

            return min_len

        return compress(0, [], k)





if __name__ == '__main__':
    print(Solution().getLengthOfOptimalCompression("abc", 2))
    print(Solution().getLengthOfOptimalCompression("aabbaa", 2))