class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        divisors = []
        sqrt = int(pow(n, 0.5))
        for i in range(1, sqrt + 1):
            if n % i == 0:
                divisors.append(i)
                k -= 1
            if k == 0:
                return i
        if sqrt * sqrt == n:
            return -1 if k > len(divisors) - 1 else n // divisors[len(divisors) - 1 - k]

        return -1 if k > len(divisors) else n // divisors[len(divisors) - k]

    # # Accepted : 32 %
    # def kthFactor(self, n: int, k: int) -> int:
    #     for i in range(1, n // 2 + 1):
    #         if n % i == 0:
    #             k -= 1
    #         if k == 0:
    #             return i
    #     if k == 1:
    #         return n
    #     return -1


if __name__ == '__main__':
    # print(Solution().kthFactor(n = 12, k = 3))
    # print(Solution().kthFactor(n = 7, k = 2))
    # print(Solution().kthFactor(n = 4, k = 4))
    print(Solution().kthFactor(46, 4))
