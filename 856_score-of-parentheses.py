class Solution:
    """
    Attempt #2
    Accepted : 93%
    """
    def scoreOfParentheses(self, s: str) -> int:
        n = len(s)
        score = [0] * (n + 1)
        stack = []

        for index, bracket in enumerate(s):
            if bracket == "(":
                stack.append(index)
                score[index] = 0
            else:
                popped = stack.pop()
                internal_score = 1 if s[index - 1] == "(" else 2 * score[index - 1]
                score[index] = score[popped - 1] + internal_score

        return score[n - 1]


if __name__ == '__main__':
    print(Solution().scoreOfParentheses("((())())"))
    print(Solution().scoreOfParentheses("()"))
    print(Solution().scoreOfParentheses("()()"))
    print(Solution().scoreOfParentheses("(())"))
    print(Solution().scoreOfParentheses("()((()))"))
