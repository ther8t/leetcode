class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) <= 0:
            return 0
        multiplier = 1
        if s[0:1] == '-' or s[0:1] == '+':
            if s[0:1] == '-':
                multiplier = -1
            s = s[1:]

        number = 0
        for i in range(0, len(s)):
            if ord(s[i:i+1]) < 48 or ord(s[i:i+1]) > 57:
                continue
            char = s[i: i + 1]
            num = ord(char) - 48
            number = number * 10 + num

        number *= multiplier
        if number < -1 * pow(2, 31):
            return max(number, -1 * pow(2, 31))
        if number > pow(2, 31) - 1:
            return min(number, pow(2, 31) - 1)
        return number


if __name__ == '__main__':
    print(Solution().myAtoi("words and 987 and 89"))
