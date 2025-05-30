class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(pow(n, 0.5))


if __name__ == '__main__':
    print(Solution().bulbSwitch(99999999))
