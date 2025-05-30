class Solution:
    def reverseParentheses(self, s: str) -> str:
        ss = [[]]
        for char in s:
            if char == "(":
                ss.append([])
            elif char == ")":
                top_stack = ss.pop()
                while top_stack:
                    ss[-1].append(top_stack.pop())
            else:
                ss[-1].append(char)

        return "".join(ss[-1])


if __name__ == '__main__':
    print(Solution().reverseParentheses(s = "(ed(et(oc))el)"))
    print(Solution().reverseParentheses(s = "(u(love)i)"))




