import bisect


class Solution:
    def nextPalindrome(self, num: str) -> str:
        n = len(num)
        if n == 1:
            return num
        num = list(num)
        left_half = num[:n // 2]

        asc_digits = []
        prev_digit = left_half[-1]
        selected_digit_index = -1
        for i in range(len(left_half) - 1, -1, -1):
            if left_half[i] < prev_digit:
                selected_digit_index = i
                break
            asc_digits.append(left_half[i])
            prev_digit = left_half[i]

        if selected_digit_index == -1:
            return ""

        replacement_digit_index = bisect.bisect_right(asc_digits, left_half[selected_digit_index])
        replacement_digit = asc_digits[replacement_digit_index]
        asc_digits[replacement_digit_index] = left_half[selected_digit_index]
        asc_digits.sort()
        new_left_half = left_half[:selected_digit_index] + [replacement_digit] + asc_digits
        middle_digit = "" if n % 2 == 0 else num[n // 2]

        return "".join(new_left_half + [middle_digit] + list(reversed(new_left_half)))


if __name__ == '__main__':
    print(Solution().nextPalindrome("1"))
    # print(Solution().nextPalindrome("1221"))
    # print(Solution().nextPalindrome("213312"))
    # print(Solution().nextPalindrome("321123"))
    # print(Solution().nextPalindrome(num = "45544554"))
