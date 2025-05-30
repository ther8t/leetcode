class Solution:
    def sumZero(self, n: int):
        ans = []
        if n % 2 == 1:
            ans.append(0)
            n -= 1
        for i in range(1, n // 2 + 1):
            ans.append(i)
            ans.append(-i)

        return ans


if __name__ == '__main__':
    print(Solution().sumZero(2))
