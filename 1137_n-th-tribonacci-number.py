import functools


class Solution:
    @functools.lru_cache(None)
    def tribonacci(self, n: int) -> int:
        if n in {0, 1, 2}:
            return [0, 1, 1][n]
        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)


if __name__ == '__main__':
    print(Solution().tribonacci(n = 4))
    print(Solution().tribonacci(n = 25))
