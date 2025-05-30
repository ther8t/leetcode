class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = 0
        while start > 0 or goal > 0:
            ans += start % 2 ^ goal % 2
            start = start >> 1
            goal = goal >> 1
        return ans


if __name__ == '__main__':
    s = Solution()
    o = s.minBitFlips(10, 7)
    print(o)
