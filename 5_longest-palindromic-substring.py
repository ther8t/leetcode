class Solution:

    def isPalindrom(self, s):
        for i in range(len(s) // 2 + 1):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True

    def maxPalindrom(self, s, index):
        if index < 0 or index >= len(s):
            return ""
        max_radius = -1
        for radius in range(0, min(index, len(s) - index - 1) + 1):
            if s[index - radius] == s[index + radius]:
                max_radius += 1
            else:
                break

        return s[index - max_radius:index + max_radius + 1]

    def maxPalindrom(self, s, index1, index2):
        if index1 < 0 or index2 >= len(s):
            return ""
        max_radius = -1
        for radius in range(0, min(index1, len(s) - index2 - 1) + 1):
            if s[index1 - radius] == s[index2 + radius]:
                max_radius += 1
            else:
                break

        return s[index1 - max_radius:index2 + max_radius + 1]

    def longestPalindrome(self, s: str) -> str:
        max_Palindrom = ""
        for i in range(len(s)):
            s1 = self.maxPalindrom(s, i, i)
            s2 = self.maxPalindrom(s, i, i + 1)
            if len(s1) > len(max_Palindrom):
                max_Palindrom = s1
            if len(s2) > len(max_Palindrom):
                max_Palindrom = s2
        return max_Palindrom


    def longestPalindrome(self, s: str) -> str:
        def isPalindrom(l):
            for start in range(len(s) - l + 1):
                end = start + l - 1
                isPalindrom = True
                for i in range(0, l // 2 + 1):
                    if s[start + i] != s[end - i]:
                        isPalindrom = False
                        break
                if isPalindrom:
                    return s[start: end + 1]
            return ""

        lo, hi = 0, len(s)
        longest = ""
        while lo <= hi:
            mid = (lo + hi) // 2 + 1
            p = isPalindrom(mid - 1)
            p2 = isPalindrom(mid)
            if p or p2:
                longest = p2 if p2 else p
                if lo == mid:
                    break
                lo = mid
            else:
                if hi == mid:
                    break
                hi = mid

        return longest



if __name__ == '__main__':
    print(Solution().longestPalindrome(
        "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"))
    print(Solution().longestPalindrome("abbcccbbbcaaccbababcbcabca"))
    print(Solution().longestPalindrome("abba"))
    print(Solution().longestPalindrome("a"))
    print(Solution().longestPalindrome("abcda"))
