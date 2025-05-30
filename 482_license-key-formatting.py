class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "")
        n = len(s)
        return "-".join([s[0:k if n % k == 0 else n % k]] + [s[k if n % k == 0 else n % k:][i * k: (i + 1) * k] for i in range((n - (k if n % k == 0 else n % k)) // k)]).upper()


if __name__ == '__main__':
    print(Solution().licenseKeyFormatting(s = "5F3Z-2e-9-w", k = 4))
    print(Solution().licenseKeyFormatting(s = "2-5g-3-J", k = 2))

