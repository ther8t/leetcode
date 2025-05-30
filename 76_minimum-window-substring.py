import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        t_counter = collections.Counter(t)

        def compareCounter(c):
            for ch in t_counter:
                if c[ch] < t_counter[ch]:
                    return False

            return True

        def check():
            counter = collections.Counter(s[:mid])
            if compareCounter(counter): return s[:mid]

            for i in range(mid, len(s)):
                counter[s[i]] += 1
                counter[s[i - mid]] -= 1
                if compareCounter(counter):
                    return s[i - mid + 1: i + 1]

            return None

        lo, hi = 1, len(s) + 1
        smallest = ""
        while lo < hi:
            mid = (lo + hi) // 2
            a = check()
            if a:
                hi = mid
                smallest = a
            else:
                lo = mid + 1

        return smallest

    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s
        if len(t) > len(s):
            return ""
        t_counter = collections.Counter(t)

        def compareCounter(c):
            for ch in t_counter:
                if c[ch] < t_counter[ch]:
                    return False

            return True

        lo, hi = 0, 0
        counter = collections.defaultdict(int)
        ans = s
        for hi in range(len(s)):
            counter[s[hi]] += 1
            if compareCounter(counter):
                while compareCounter(counter):
                    if hi - lo + 1 < len(ans):
                        ans = s[lo:hi + 1]
                    counter[s[lo]] -= 1
                    lo += 1
        return ans if compareCounter(collections.Counter(s)) else ""





if __name__ == '__main__':
    print(Solution().minWindow(s = "ADOBECODEBANC", t = "ABC"))
    print(Solution().minWindow(s = "a", t = "a"))
    print(Solution().minWindow(s = "a", t = "aa"))
    print(Solution().minWindow("abc", "ac"))
