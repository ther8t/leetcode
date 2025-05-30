class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        n = str(n)
        l = len(n)
        count = 0

        def get_numbers_less_than_equal_to(index):
            count = 0
            s = set()
            for i in range(index):
                if n[i] in s:
                    return int(n[index])
                s.add(n[i])
                if n[i] < n[index]:
                    count += 1
            return count

        for i in range(1, l):
            current_contribution = 1
            for j in range(1, i):
                current_contribution *= (9 - j + 1)
            count += 9 * current_contribution

        digits = set()
        for i in range(len(n)):
            current_digit = n[i]
            # first calculate all number less than the digit in consideration.
            numbers_on_left, numbers_on_right = i, l - i - 1

            current_contribution = 1
            for j in range(l - i - 1):
                current_contribution *= (9 - j - numbers_on_left)
            count += (int(current_digit) + (-1 if i == 0 else 0) - get_numbers_less_than_equal_to(i)) * current_contribution
            if current_digit in digits:
                return count
            digits.add(current_digit)

        return count + 1


if __name__ == '__main__':
    print(Solution().countSpecialNumbers(20))
    print(Solution().countSpecialNumbers(135))
    print(Solution().countSpecialNumbers(5))
    print(Solution().countSpecialNumbers(233)) #180
    print(Solution().countSpecialNumbers(225)) #178
