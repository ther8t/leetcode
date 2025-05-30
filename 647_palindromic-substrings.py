class Solution:
    """
    Interesting. Loll
    I haven't slept for long. There is some magic about me today. Yesterday Pakhi pushed me and I'm filled with some energy today. I have slept for barely 4 hours and I am ENERGETICCC!!
    """
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        ans = 0
        for i in range(n):
            lo, hi = i, i
            while lo >= 0 and hi < n and s[lo] == s[hi]:
                ans += 1
                lo -= 1
                hi += 1

            lo, hi = i, i + 1
            while lo >= 0 and hi < n and s[lo] == s[hi]:
                ans += 1
                lo -= 1
                hi += 1

        return ans


if __name__ == '__main__':
    print(Solution().countSubstrings(s = "abc"))
    print(Solution().countSubstrings(s = "aaa"))
