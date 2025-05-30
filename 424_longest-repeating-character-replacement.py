import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lo, hi = 0, 0
        c = collections.defaultdict(int)

        def check():
            sortedc = sorted(c, key=lambda x: c[x])
            return hi - lo + 1 - c[sortedc[-1]] <= k

        ans = 0
        while hi < len(s):
            c[s[hi]] += 1
            if check():
                ans = max(ans, hi - lo + 1)
            else:
                while not check():
                    c[s[lo]] -= 1
                    lo += 1
            hi += 1

        return ans


if __name__ == '__main__':
    print(Solution().characterReplacement(s = "ABAB", k = 2))
    print(Solution().characterReplacement(s = "AABABBA", k = 1))
