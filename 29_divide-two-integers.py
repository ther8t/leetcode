class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negatives = 0
        if dividend < 0:
            negatives += 1
        if divisor < 0:
            negatives += 1

        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        while dividend >= divisor:
            divisorIterator = divisor
            quotientIterator = 1
            while dividend > (divisorIterator + divisorIterator):
                divisorIterator += divisorIterator
                quotientIterator += quotientIterator
            quotient += quotientIterator
            dividend -= divisorIterator
        return self.checkRange(quotient) if negatives != 1 else self.checkRange(-quotient)

    def checkRange(self, num):
        if num < -pow(2, 31):
            return -pow(2, 31)
        if num > pow(2, 31) - 1:
            return pow(2, 31) - 1
        return num


if __name__ == '__main__':
    print(Solution().divide(1, 1))
