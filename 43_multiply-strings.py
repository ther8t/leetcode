class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = "0" + num1
        ans = 0
        for i in range(len(num2) - 1, -1, -1):
            carry = 0
            subMultiplication = 0
            for j in range(len(num1) - 1, -1, -1):
                number1 = num1[j]
                number2 = num2[i]
                multiplication = int(number1) * int(number2)
                multiplication += carry
                unit = (multiplication % 10) * pow(10, len(num1) -1 - j)
                subMultiplication += unit
                carry = multiplication // 10
            ans += subMultiplication * pow(10, len(num2) - i - 1)
        return str(ans)


if __name__ == '__main__':
    print(Solution().multiply("999", "456"))
