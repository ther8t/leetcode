import collections
from functools import lru_cache


class Solution:
    # # TLE
    def addOperators(self, num: str, target: int):

        @lru_cache(None)
        def populate_expressions(index):
            if index == len(num) - 1:
                return [num[index]]

            expressions = []
            sub_expressions = populate_expressions(index + 1)
            for operator in ["-", "+", "*", ""]:
                for ex in sub_expressions:
                    expressions.append(num[index] + operator + ex)

            return expressions

        expressions = populate_expressions(0)
        out = []
        for i in expressions:
            try:
                if eval(i) == target:
                    out.append(i)
            except:
                pass
        return out

    # """
    # The idea behind this is to append each number with all the operators and reach a final expression.
    # Since evaluating expression at the very end is a time expensive process, we evaluate them before hand.
    # The evaluation of expression, which was the problem with other algo, works well because we evaluate the expression moving left to right which is the correct order of precedence.
    # But it's a huge amount of iterations because of the repeating expression, the kind of thing which can be reduced by backtrack + memorization, which has a problem with precedence and thus evaluating expression.
    #
    # It's a To Be or Not To Be question now. And the answer is something in the middle.
    # """
    # def addOperators(self, num: str, target: int):
    #     expressions = []
    #
    #     def dfs(index, expression, stack):
    #         if index == len(num):
    #             if sum(stack) == target:
    #                 expressions.append(expression)
    #             return
    #         for i in range(1, len(num)):
    #             if index + i > len(num):
    #                 break
    #             current_number = num[index: index + i]
    #             stack_last = stack[-1]
    #             dfs(index + 1, expression + "+" + current_number, stack + [int(current_number)])
    #             dfs(index + 1, expression + "-" + current_number, stack + [-int(current_number)])
    #             # stack[-1] = stack_last * 10 + int(current_number)
    #             # dfs(index + 1, expression + current_number, stack)
    #             stack[-1] = stack_last * int(current_number)
    #             dfs(index + 1, expression + "*" + current_number, stack)
    #             # if int(current_number) != 0:
    #             #     stack[-1] = stack_last / int(current_number)
    #             #     dfs(index + 1, expression + "/" + current_number, stack)
    #
    #     dfs(1, num[0], [int(num[0])])
    #     return expressions

    """
    The algo unfortunately gives the wrong answer because of a very simple Computer Science property. Precedence.
    Evaluating 7/8*9. Since we are considering backtracking + memorization in this we travel bottom up. Thus evaluation happens right to left, which means.
    7/8*9 = 7/72 = 0.09722
    It should however be 7/8*9 = 0.875*9 = 7.875
    The advantage of backtracking + memorization is that unlike the usual dfs to reach the leaf nodes, it's faster.

    THE STUPIDEST MISTAKE I HAVE EVER MADE. I READ THE QUESTION INCORRECTLY. THERE WAS NO '/'.
    This was for good reason infact. The reasons are why I could not solve the question in the first place.
    """
    def addOperators(self, num: str, target: int):
        @lru_cache(None)
        def populate_expressions(index):
            expressions = []
            for i in range(1, len(num) + 1):
                current_number = num[index: index + i]
                if index + i == len(num):
                    expressions.append((current_number, [int(current_number)]))
                    break
                if index + i > len(num):
                    break
                sub_expressions = populate_expressions(index + i)
                for (exp, stack) in sub_expressions:
                    expressions.append((current_number + "+" + exp, stack + [int(current_number)]))

                for (exp, stack) in sub_expressions:
                    new_stack = stack.copy()
                    new_stack[-1] = -new_stack[-1]
                    new_stack.append(int(current_number))
                    expressions.append((current_number + "-" + exp, new_stack))

                for (exp, stack) in sub_expressions:
                    new_stack = stack.copy()
                    new_stack[-1] = int(current_number) * new_stack[-1]
                    expressions.append((current_number + "*" + exp, new_stack))

                # for (exp, stack) in sub_expressions:
                #     if stack[-1] == 0:
                #         continue
                #     new_stack = stack.copy()
                #
                #     new_stack[-1] = int(current_number) / new_stack[-1]
                #     expressions.append((current_number + "/" + exp, new_stack))

                if current_number == "0":
                    break

            return expressions

        expressions = populate_expressions(0)
        out = []
        for exp, stack in expressions:
            if sum(stack) == target:
                out.append(exp)
        return out


    def addOperators(self, num: str, target: int):
        @lru_cache(None)
        def populate_expressions(index):
            expressions = []
            for i in range(index + 1, len(num) + 1):
                current_number = num[index: i]
                if i == len(num):
                    expressions.append((current_number, [int(current_number)]))
                    break
                subexpressions = populate_expressions(i)
                """
                Why have I used 3 separate loops when 1 singular loop would have sufficed.
                This is because popping the stack alters it. There were cases where expression and stack did not match ('3', []) because it would have been popped at some point of time.
                """
                # for (exp, stack) in subexpressions:
                #     left_most = stack.pop()
                #     expressions.append((current_number + "+" + exp, stack + [left_most, int(current_number)]))
                #     expressions.append((current_number + "*" + exp, stack + [left_most * int(current_number)]))
                #     expressions.append((current_number + "-" + exp, stack + [-left_most, int(current_number)]))

                for (exp, stack) in subexpressions:
                    expressions.append((current_number + "+" + exp, stack + [int(current_number)]))

                for (exp, stack) in subexpressions:
                    new_stack = stack.copy()
                    new_stack[-1] = -new_stack[-1]
                    new_stack.append(int(current_number))
                    expressions.append((current_number + "-" + exp, new_stack))

                for (exp, stack) in subexpressions:
                    new_stack = stack.copy()
                    new_stack[-1] = int(current_number) * new_stack[-1]
                    expressions.append((current_number + "*" + exp, new_stack))
                if int(current_number) == 0:
                    """
                    This is interesting piece of code. 1*05 = 5, but this is not acceptable solution.
                    """
                    break
            return expressions

        expressions = populate_expressions(0)
        out = []
        for exp, stack in expressions:
            if sum(stack) == target:
                out.append(exp)

        return out


    def addOperators(self, num: str, target: int):


if __name__ == '__main__':
    print(Solution().addOperators(num = "123", target = 6))
    print(Solution().addOperators(num = "232", target = 8))
    print(Solution().addOperators(num = "3456237490", target = 9191))
    print(Solution().addOperators("123456789", 45))
    print(Solution().addOperators("105", 5))
    print(Solution().addOperators("2147483647", 2147483647))
