class Solution:

    def intToRoman(self, num: int) -> str:
        symbols = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
        if num in symbols:
            return symbols[num]
        else:
            # just smaller
            just_smaller = 0
            for i in symbols.keys():
                if num > i:
                    just_smaller = i
                else:
                    break

            return symbols[just_smaller] + self.intToRoman(num - just_smaller)


if __name__ == '__main__':
    print(Solution().intToRoman(1994))