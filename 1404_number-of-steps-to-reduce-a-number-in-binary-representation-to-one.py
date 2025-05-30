class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0
        carry = 0
        for i in range(len(s) - 1, 0, -1):
            if carry + int(s[i]) == 1:
                ans += 2
                carry = 1
            else:
                ans += 1
        return ans + carry


    # def numSteps(self, s: str) -> int:
    #     def add_one(s):
    #         nonlocal ones
    #         for i in range(len(s) - 1, -1, -1):
    #             if s[i] == "1":
    #                 ones -= 1
    #                 s[i] = "0"
    #             else:
    #                 s[i] = "1"
    #                 ones += 1
    #                 break
    #         return s
    #
    #     def divide_by_two(s):
    #         return ["0"] + s[:-1]
    #
    #     s = list(s)
    #     s = ["0"] + s
    #     ones = 0
    #     for char in s:
    #         if char == "1":
    #             ones += 1
    #
    #     steps = 0
    #     while ones > 1 or s[-1] != "1":
    #         steps += 1
    #         if s[-1] == "1":
    #             s = add_one(s)
    #         else:
    #             s = divide_by_two(s)
    #
    #     return steps

    def numSteps(self, s: str) -> int:
        s.lstrip("0")
        carry = 0
        ans = 0
        for i in range(len(s) - 1, 0, -1):
            if (carry + int(s[i])) % 2 == 0:
                ans += 1
                carry = (carry + int(s[i])) // 2
            else:
                ans += 2
                carry = 1
        return ans + (1 if carry == 1 else 0)




if __name__ == '__main__':
    print(Solution().numSteps(s = "1101"))
    print(Solution().numSteps(s = "1111"))
