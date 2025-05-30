class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            match = 0
            for j in range(len(needle)):
                if i+j<len(haystack) and haystack[i + j] == needle[j]:
                    match += 1
                else:
                    break
            if match == len(needle):
                return i
        return -1


if __name__ == '__main__':
    print(Solution().strStr("hello", "ll"))
