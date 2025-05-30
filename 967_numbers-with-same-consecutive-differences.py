class Solution:
    def numsSameConsecDiff(self, n: int, k: int):
        ans = []

        def build(number, digit_count):
            if digit_count == n:
                ans.append(number)
                return
            last_digit = number % 10
            new_last_digit = last_digit - k
            if new_last_digit >= 0:
                build(number * 10 + new_last_digit, digit_count + 1)

            if k != 0:
                new_last_digit = last_digit + k
                if new_last_digit < 10:
                    build(number * 10 + new_last_digit, digit_count + 1)

        for i in range(1, 10):
            build(i, 1)

        return ans


if __name__ == '__main__':
    print(Solution().numsSameConsecDiff(n = 3, k = 7))
    print(Solution().numsSameConsecDiff(n = 2, k = 1))
    print(Solution().numsSameConsecDiff(2, 0))
