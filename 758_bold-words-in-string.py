import re


class Solution:
    # Accepted : 24%
    def boldWords(self, words, s: str) -> str:
        dp = [False] * len(s)
        word_dict = set()
        min_length, max_length = float('inf'), -float('inf')
        for word in words:
            word_dict.add(word)
            min_length = min(min_length, len(word))
            max_length = max(max_length, len(word))

        for l in range(min_length, max_length + 1):
            for i in range(0, len(s) - l + 1):
                word = "".join(s[i:i+l])
                if word in word_dict:
                    for j in range(i, i + l):
                        dp[j] = True

        out = ""
        ptr1, ptr2 = 0, 0
        while ptr1 < len(s) and ptr2 < len(s):
            if not dp[ptr1]:
                out += s[ptr1]
                ptr1 += 1
            else:
                ptr2 = ptr1
                out += "<b>"
                while ptr2 < len(s) and dp[ptr2]:
                    out += s[ptr2]
                    ptr2+=1
                out += '</b>'
                ptr1 = ptr2

        return out

    # # Accepted : 66%
    # def boldWords(self, words, s: str) -> str:
    #     dp = [False] * len(s)
    #     for word in words:
    #         start_index = 0
    #         while True:
    #             result = s.find(word, start_index)
    #             if result != -1:
    #                 for i in range(result, result + len(word)):
    #                     dp[i] = True
    #                 start_index = result + 1
    #             else:
    #                 break
    #
    #     out = ""
    #     ptr1, ptr2 = 0, 0
    #     while ptr1 < len(s) and ptr2 < len(s):
    #         if not dp[ptr1]:
    #             out += s[ptr1]
    #             ptr1 += 1
    #         else:
    #             ptr2 = ptr1
    #             out += "<b>"
    #             while ptr2 < len(s) and dp[ptr2]:
    #                 out += s[ptr2]
    #                 ptr2+=1
    #             out += '</b>'
    #             ptr1 = ptr2
    #
    #     return out


if __name__ == '__main__':
    print(Solution().boldWords(words = ["ab","bc"], s = "aabcd"))
    print(Solution().boldWords(words = ["ab","cb"], s = "aabcd"))
