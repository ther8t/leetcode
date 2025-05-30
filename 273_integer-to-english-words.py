class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        unit = {'0': '', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven',
                '8': 'Eight', '9': 'Nine', '10': 'Ten', '11': 'Eleven', '12': 'Twelve', '13': 'Thirteen',
                '14': 'Fourteen', '15': 'Fifteen', '16': 'Sixteen', '17': 'Seventeen', '18': 'Eighteen',
                '19': 'Nineteen'}

        tens = {'2': 'Twenty', '3': 'Thirty', '4': 'Forty', '5': 'Fifty', '6': 'Sixty', '7': 'Seventy',
                '8': 'Eighty', '9': 'Ninety'}

        def convert_nums(num):
            out = []
            if num // 100 != 0:
                out.append(unit[str(num // 100)])
                out.append("Hundred")
            num %= 100
            if num < 20:
                unit_digit = unit[str(num)]
                if unit_digit:
                    out.append(unit_digit)
            else:
                tens_digit = tens[str(num // 10)]
                if tens_digit:
                    out.append(tens_digit)
                unit_digit = unit[str(num % 10)]
                if unit_digit:
                    out.append(unit_digit)
            return out

        out = []
        for p, w in zip([9, 6, 3, 0], ["Billion", "Million", "Thousand", ""]):
            if num // pow(10, p) != 0:
                out += convert_nums(num // pow(10, p))
                out.append(w)
            num %= pow(10, p)

        return " ".join(out).strip()


if __name__ == '__main__':
    print(Solution().numberToWords(50868))



