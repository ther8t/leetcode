class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        del_position = None
        for i in range(len(number) - 1, -1, -1):
            if number[i] == digit and (not del_position or (del_position and number[i + 1] > digit)):
                del_position = i
        return number[:del_position] + number[del_position + 1:]


if __name__ == '__main__':
    print(Solution().removeDigit(number = "123", digit = "3"))
    print(Solution().removeDigit(number = "1231", digit = "1"))
    print(Solution().removeDigit(number = "551", digit = "5"))
