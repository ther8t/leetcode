class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        dp = {512: 9, 256: 8, 128: 7, 64: 6, 32: 5, 16: 4, 8: 3, 4: 2, 2: 1, 1: 0}

        def get_steps(num, steps=0):
            if num in dp:
                return steps + dp[num]
            if num % 2 == 0:
                return get_steps(num//2, steps + 1)
            else:
                return get_steps(3 * num + 1, steps + 1)

        a = []
        for num in range(lo, hi + 1):
            a.append((get_steps(num), num))

        a.sort()
        return a[k - 1][1]


if __name__ == '__main__':
    print(Solution().getKth(lo = 1, hi = 1000, k = 4))
