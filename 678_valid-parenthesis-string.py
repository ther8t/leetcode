class Solution:
    def checkValidString(self, s: str) -> bool:
        b_stack, star_stack = [], []

        for i, c in enumerate(s):
            if c == '(':
                b_stack.append(i)
            elif c == "*":
                star_stack.append(i)
            else:
                if b_stack:
                    b_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False

        while star_stack:
            popped = star_stack.pop()
            if not b_stack:
                return True
            if popped > b_stack[-1]:
                b_stack.pop()
            else:
                return False

        return not b_stack


if __name__ == '__main__':
    print(Solution().checkValidString(s = "()"))
    print(Solution().checkValidString(s = "(*)"))
    print(Solution().checkValidString(s = "(*))"))
    print(Solution().checkValidString(s = "())*"))
    print(Solution().checkValidString(s = "("))
    print(Solution().checkValidString(s = "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"))
    print(Solution().checkValidString(s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))
