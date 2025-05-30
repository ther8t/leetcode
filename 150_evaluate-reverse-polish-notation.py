class Solution:
    def evalRPN(self, tokens):
        signSet = {"+", "-", "*", "/"}
        stack = []

        def evaluate(number1, number2, sign):
            number1 = int(number1)
            number2 = int(number2)
            if sign == "+":
                return number1 + number2
            if sign == "-":
                return number1 - number2
            if sign == "*":
                return number1 * number2
            if sign == "/":
                return int(number1 / number2)

        for token in tokens:
            if token in signSet:
                number1 = stack.pop()
                number2 = stack.pop()
                answer = str(evaluate(number2, number1, token))
                stack.append(answer)
            else:
                stack.append(token)

        return int(stack.pop())


if __name__ == '__main__':
    print(Solution().evalRPN(["2", "1", "+", "3", "*"]))
