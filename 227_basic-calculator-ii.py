class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        ans = 0
        ptr = 0
        builder = ""
        while ptr < n and s[ptr] != "*" and s[ptr] != "/" and s[ptr] != "+" and s[ptr] != "-":
            builder += s[ptr]
            ptr += 1
        num1 = int(builder.strip())
        last_number = num1
        ans += num1

        while ptr < n:
            ptr2 = ptr
            num1 = last_number
            operator = s[ptr2]
            ptr2 += 1
            builder = ""
            while ptr2 < n and s[ptr2] != "*" and s[ptr2] != "/" and s[ptr2] != "+" and s[ptr2] != "-":
                builder += s[ptr2]
                ptr2 += 1
            num2 = int(builder.strip())
            if operator == "/":
                ans -= last_number
                ans += ((num1 // abs(num1)) * (abs(num1) // num2) if num1 != 0 and num2 != 0 else 0)
                last_number = ((num1 // abs(num1)) * (abs(num1) // num2) if num1 != 0 and num2 != 0 else 0)
            elif operator == "*":
                ans -= last_number
                ans += (num1 * num2)
                last_number = (num1 * num2)
            elif operator == "-":
                ans += (-num2)
                last_number = -num2
            elif operator == "+":
                ans += (num2)
                last_number = num2
            ptr = ptr2

        return ans


if __name__ == '__main__':
    print(Solution().calculate(s = "3+2*2"))
    print(Solution().calculate(s = " 3/2 "))
    print(Solution().calculate(s = " 3+5 / 2 "))
    print(Solution().calculate(s = "14-3/2"))

