class Solution:
    def reverse(self, x: int) -> int:
        multiplier = 1
        reversedNumber = 0
        if x < 0:
            multiplier = -1
            x = x * -1
        while x > 0:
            reversedNumber = reversedNumber * 10 + x % 10
            x //= 10
        reversedNumber = multiplier * reversedNumber
        return reversedNumber if -1*pow(2, 31) < reversedNumber < pow(2,31) - 1 else 0


if __name__ == '__main__':
    print(Solution().reverse(-123))
