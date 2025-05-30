class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)

        def check(end):
            lo, hi = 0, end
            while lo < hi:
                if s[lo] != s[hi]:
                    return False
                lo += 1
                hi -= 1
            return True

        match_index = 0
        for i in range(n - 1, 0, -1):
            if check(i):
                match_index = i
                break

        return s[n - 1:match_index:-1] + s


if __name__ == '__main__':
    print(Solution().shortestPalindrome("aacecaaa"))
    print(Solution().shortestPalindrome("abcd"))
