import functools
import time

import numpy


class Solution:
    """
    Revision 2:
    The question is fairly simple to logic. I on the other hand had made a very stupid mistake. Instead of doing (num1 % MOD) * (num2 % MOD), I did (num1 * num2) % MOD.
    This for numbers so huge that it breaks the internet can be a bit treacherous.

    The logic goes something like this.
    For n = 1 : P, L
    For n = 2 : PP, PL, LP, LL
    For n = 3 : This gets a bit tricky. Out of all the above we can't have LL with L. So we can have (f(n-1) + 'P') and (f(n - 1) - 1 + 'L')
    .
    .
    For n = 5 : _ _ _ _ _. We have 5 places. We can place P in the last, no problem, f(4) ways. We can't place L as simply.
    What can we not include? _ _ L L 'L'. Then how many number of ways this can happen? f(2) ways.
    BUT out of f(2) ways, those ending with L can't be included because they would not have progressed because LLL is not allowed, imagine _ L L L 'L'. This option won't even be available.
    So we can only have f(1).
    Similarly for f(6) we can have f(2), and f(n) -> f(n - 4)

    So f(n) = 2 * f(n - 1) - f(n - 4)
    """
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [float('inf')] * (max(4, n + 1))
        dp[0], dp[1], dp[2], dp[3] = 1, 2, 4, 7

        for i in range(4, n + 1):
            dp[i] = (2 * dp[i - 1] - dp[i - 4]) % MOD

        count = 0
        for i in range(n):
            count += dp[i] * dp[n - 1 - i]
            count %= MOD

        return (dp[n] + count) % MOD



    # def checkRecord(self, n: int) -> int:
    #     dp = [1, 2, 4]
    #     mod = 1000000007
    #
    #     # This code takes milliseconds
    #     for i in range(3, n + 2):
    #         dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])
    #
    #     nValue = dp[n]
    #
    #     # This code takes forever.
    #     s = 0
    #     t = time.time()
    #     # dp = numpy.array(dp)
    #     # n = len(dp)
    #     # nValue + numpy.mod(numpy.multiply(dp[:n//2], dp[n//2 + 1:]), mod)
    #     first = dp[len(dp) // 2]
    #
    #     for i in range(n):
    #         a = (dp[i] % mod) * (dp[n - 1 - i] % mod)
    #         s = (s + a % mod) % mod
    #
    #
    #     return (s + nValue) % mod

        # mod = pow(10, 9) + 7
        # dp = [1, 2, 4]
        # for i in range(3, n + 2):
        #     dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])
        #
        # nValue = dp[n]
        #
        # sum = 0
        # if n % 2 == 0:
        #     for i in range((n // 2)):
        #         sum += dp[i] % mod * dp[n - 1 - i] % mod
        #     sum *= 2
        # else:
        #     for i in range(n // 2):
        #         sum += dp[i] % mod * dp[n - 1 - i] % mod
        #     sum *= 2
        #     sum += dp[n // 2] % mod * dp[n // 2] % mod
        #
        # return (sum + nValue) % mod


if __name__ == '__main__':
    # print(Solution().checkRecord(1))
    print(Solution().checkRecord(10101))
    print(Solution().checkRecord(99997))
