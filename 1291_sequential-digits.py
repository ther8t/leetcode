class Solution:
    def sequentialDigits(self, low: int, high: int):
        low_digits, high_digits = -1, -1
        for i in range(1, 11):
            if low_digits == -1 and low // pow(10, i) == 0:
                low_digits = i
            if high_digits == -1 and high // pow(10, i) == 0:
                high_digits = i

        s = "123456789"
        out = []
        for i in range(low_digits, high_digits + 1):
            for j in range(9 - i + 1):
                num = int(s[j:j + i])
                if num > high:
                    return out
                if num >= low:
                    out.append(num)

        return out


if __name__ == '__main__':
    print(Solution().sequentialDigits(10, 1000000000))
