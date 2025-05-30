import collections


class Solution:
    # Accepted : 24%
    def uniqueLetterString(self, s: str) -> int:
        sum = 0
        last_score = 0
        prev_occurrence = {chr(i + ord('A')): [-1, -1] for i in range(26)}
        for i in range(len(s)):
            char = s[i]
            latest_occurrence_before = i - prev_occurrence[char][1] - 1
            previous_to_latest_occurrence_before = prev_occurrence[char][1] - prev_occurrence[char][0]
            current_score = last_score + latest_occurrence_before - previous_to_latest_occurrence_before + 1
            sum += current_score
            last_score = current_score
            prev_occurrence[char][0] = prev_occurrence[char][1]
            prev_occurrence[char][1] = i
        return sum

    # # Wrong Answer : Didn't even submit.
    # def uniqueLetterString(self, s: str) -> int:
    #     n = len(s)
    #     all_not = 0
    #
    #     for c in range(26):
    #         char = chr(c + ord('A'))
    #         a = s.replace(char, "*")
    #
    #         for i in range(len(a)):
    #             if a[i] != "*":
    #                 continue
    #             for j in range(i + 1, len(a)):
    #                 if a[j] != "*":
    #                     continue
    #                 L = j - i + 1
    #                 l, r = i, n - j - 1
    #                 all_not += (l * r + l + r + 1)
    #                 # all_not += (i + 1) * (len(a) - j)
    #
    #     return n * (n + 1) * (n + 2) // 6 - all_not


    def uniqueLetterString(self, s: str) -> int:
        last_occurance = {str(i + ord('A')): -1 for i in range(26)}
        for i in range(len(s)):




if __name__ == '__main__':
    print(Solution().uniqueLetterString("ABC"))
    print(Solution().uniqueLetterString("ABA"))
