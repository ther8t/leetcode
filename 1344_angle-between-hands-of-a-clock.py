class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        ans = abs((30 * hour + minutes / 2) % 360 - 6 * minutes)
        return 360 - ans if ans > 180 else ans


if __name__ == '__main__':
    print(Solution().angleClock(hour = 12, minutes = 30))
    print(Solution().angleClock(hour = 3, minutes = 30))
    print(Solution().angleClock(hour = 3, minutes = 15))
    print(Solution().angleClock(1, 57))
