class Solution:
    def myPow(self, x: float, n: int) -> float:
        power = abs(n)
        answer = 1

        powerIterator = 1
        outputIterator = x
        dp = {0: 1, 1: x}
        while powerIterator < power:
            outputIterator *= outputIterator
            powerIterator += powerIterator
            dp[powerIterator] = outputIterator

        while power >= 1:
            justLesserPower = 0
            subAnswer = 1
            for i in dp.keys():
                if i <= power:
                    justLesserPower = i
                    subAnswer = dp[i]
                else:
                    break
            power -= justLesserPower
            answer *= subAnswer
        return answer if n > 0 else 1 / answer


if __name__ == '__main__':
    print(Solution().myPow(x = 2.10000, n = 3))
