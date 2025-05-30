class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        lo, hi = 0, 0
        window_cost = 0
        max_size = 0
        while hi < len(s):
            window_cost += abs(ord(s[hi]) - ord(t[hi]))
            while window_cost > maxCost:
                window_cost -= abs(ord(s[lo]) - ord(t[lo]))
                lo += 1
            max_size = max(max_size, hi - lo + 1)
            hi += 1

        return max_size


if __name__ == '__main__':
    print(Solution().equalSubstring(s = "abcd", t = "bcdf", maxCost = 3))
    print(Solution().equalSubstring(s = "abcd", t = "cdef", maxCost = 3))
    print(Solution().equalSubstring(s = "abcd", t = "acde", maxCost = 0))
