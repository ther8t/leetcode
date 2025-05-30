class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        firstMatch = bool(s) and p[0] in {s[0], "."}
        if len(p) >= 2 and p[1] == "*":
            return (firstMatch and self.isMatch(s[1:], p)) or self.isMatch(s, p[2:])
        elif firstMatch:
            return self.isMatch(s[1:], p[1:])
        else:
            return False

    # def isMatch(self, s: str, p: str) -> bool:
    #     lengthTrue = -1
    #     patternLength = 0
    #     while patternLength < len(p):
    #         currentChar = p[patternLength:patternLength + 1]
    #         nextChar = p[patternLength + 1:patternLength + 2]
    #         if nextChar == "*":
    #             for j in range(lengthTrue + 1, len(s)):
    #                 if currentChar == ".":
    #                     lengthTrue += 1
    #                     continue
    #                 elif currentChar == s[lengthTrue + 1: lengthTrue + 2]:
    #                     lengthTrue += 1
    #                     continue
    #                 else:
    #                     break
    #             patternLength += 1
    #         elif currentChar == ".":
    #             lengthTrue += 1
    #         elif currentChar == s[lengthTrue + 1: lengthTrue + 2]:
    #             lengthTrue += 1
    #         else:
    #             return False
    #         patternLength += 1
    #     return True if lengthTrue == len(s) - 1 else False
    #
    #     # while patternLength < len(p):
    #     #     currentChar = p[patternLength:patternLength + 1]
    #     #     nextChar = p[patternLength + 1:patternLength + 2]
    #     #     if nextChar == "*":
    #     #         for j in range(lengthTrue + 1, len(s)):
    #     #             if currentChar == ".":
    #     #                 lengthTrue += 1
    #     #                 continue
    #     #             elif currentChar == s[lengthTrue + 1: lengthTrue + 2]:
    #     #                 lengthTrue += 1
    #     #                 continue
    #     #             else:
    #     #                 break
    #     #         patternLength += 1
    #     #     elif currentChar == ".":
    #     #         lengthTrue += 1
    #     #     elif currentChar == s[lengthTrue + 1: lengthTrue + 2]:
    #     #         lengthTrue += 1
    #     #     else:
    #     #         return False
    #     #     patternLength += 1
    #     # return True if lengthTrue == len(s) - 1 else False


if __name__ == '__main__':
    print(Solution().isMatch("aaa", "a*a"))
    print(bool("abc"))
# elif currentChar == "*":
#     if patternLength - 1 >= 0:
#         compareChar = p[patternLength - 1:patternLength]
#         for j in range(lengthTrue + 1, len(s)):
#             if compareChar == ".":
#                 lengthTrue += 1
#                 continue
#             elif compareChar == s[lengthTrue + 1: lengthTrue + 2]:
#                 lengthTrue += 1
#                 continue
#             else:
#                 break
#     else:
#         return False
