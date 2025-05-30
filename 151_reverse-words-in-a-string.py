import re


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(re.split("\s+", s.strip())))


if __name__ == '__main__':
    print(Solution().reverseWords("a good   example"))
    print(Solution().reverseWords("the sky is blue"))
    print(Solution().reverseWords("  hello world  "))
