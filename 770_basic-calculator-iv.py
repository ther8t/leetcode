import collections
import re


class Solution:
    def basicCalculatorIV(self, expression: str, evalvars, evalints):
        expression = expression.replace("(", "( ")
        expression = expression.replace(")", " )")
        split_expression = expression.split(" ")
        evaluated_expression = []
        for token in split_expression:
            if token in evalvars:
                value = evalints[evalvars.index(token)]
                evaluated_expression.append(str(value))
            else:
                evaluated_expression.append(token)

        def multiplication(expression1, expression2):
            if not expression1 or not expression2:
                return []
            if expression1[0] == "(":
                expression1 = expression1[1:len(expression1) - 1]
            if expression2[0] == "(":
                expression2 = expression2[1:len(expression1) - 1]
            output = []
            for exp1 in expression1:
                for exp2 in expression2:
                    split_exp1 = exp1.split(" ")
                    split_exp2 = exp2.split(" ")
                    output.append(multiply_tokens(split_exp1, split_exp2))
            return output

        def is_number(exp):
            return re.match(r"(-?\d+)", exp) is not None

        def is_variable(exp):
            return re.match(r"([a-z]+)", exp) is not None

        def multiply_tokens(exp1, exp2):
            numbers = []
            variables = []

            for ex in exp1:
                if is_number(ex):
                    numbers.append(ex)
                if is_variable(ex):
                    variables.append(ex)

            for ex in exp2:
                if is_number(ex):
                    numbers.append(ex)
                if is_variable(ex):
                    variables.append(ex)

            cooficient = 1
            for number in numbers:
                cooficient *= int(number)

            return " * ".join([str(cooficient)] + sorted(variables))

        def add(map, exp):
            split_exp = exp.split(" ")
            variable = " ".join(split_exp[1:])
            order = len(split_exp[1:]) // 2
            prev_value = 0
            if variable in map:
                prev_value = map[variable][1]
            map[variable] = [order, prev_value + int(split_exp[0])]

        def simplify_expression(expression):
            ptr = 0
            while ptr < len(expression):
                if expression[ptr] == "-" or expression[ptr] == "+":
                    ptr_start = ptr + 1
                    ptr_end = ptr_start + 1
                    bracket_count = 0
                    if expression[ptr_start] == "(":
                        bracket_count = 1
                        while ptr_end < len(expression) and bracket_count > 0:
                            if expression[ptr_end] == "(":
                                bracket_count += 1
                            elif expression[ptr_end] == ")":
                                bracket_count -= 1
                            ptr_end += 1
                        # [ptr_start, ptr_end) either expression or expression WITH and including brackets
                        brackets_simplified = multiplication([expression[ptr] + "1"], simplify_expression(expression[ptr_start + 1:ptr_end - 1]))
                        expression = expression[0:ptr] + expression[ptr+1:ptr_start + 1] + brackets_simplified + expression[ptr_end - 1:]
                        ptr = ptr_start + 1 + len(brackets_simplified)

                    else:
                        exp_multiplication = multiplication([expression[ptr]+"1"], expression[ptr_start:ptr_end])
                        expression = expression[0:ptr_start - 1] + exp_multiplication + expression[ptr_end:]
                        ptr = ptr - 1 + len(exp_multiplication) + 1
                elif expression[ptr] == "(":
                    ptr_start = ptr
                    ptr_end = ptr + 1
                    bracket_count = 1
                    while ptr_end < len(expression) and bracket_count > 0:
                        if expression[ptr_end] == "(":
                            bracket_count += 1
                        elif expression[ptr_end] == ")":
                            bracket_count -= 1
                        ptr_end += 1
                    brackets_simplified = simplify_expression(expression[ptr_start + 1:ptr_end - 1])
                    expression = expression[0:ptr_start + 1] + brackets_simplified + expression[ptr_end - 1:]
                    ptr = ptr_start + 1 + len(brackets_simplified) + 1
                elif expression[ptr] == "*":
                    # trace back to find out where the brackets balance
                    ptr_exp1_end = ptr
                    ptr_exp1_start = ptr - 1
                    bracket_count = 0
                    first_expression_bracket = False
                    if expression[ptr_exp1_start] == ")":
                        bracket_count += 1
                        first_expression_bracket = True
                    while ptr_exp1_start - 1 >= 0 and bracket_count > 0:
                        if expression[ptr_exp1_start - 1] == "(":
                            bracket_count -= 1
                        elif expression[ptr_exp1_start - 1] == ")":
                            bracket_count += 1
                        ptr_exp1_start -= 1
                    multiplication_expression1 = expression[ptr_exp1_start:ptr_exp1_end]  # with brackets

                    ptr_exp2_start = ptr + 1
                    ptr_exp2_end = ptr + 2
                    bracket_count = 0
                    second_expression_bracket = False
                    if expression[ptr_exp2_start] == "(":
                        second_expression_bracket = True
                        bracket_count += 1
                        while ptr_exp2_end < len(expression) and bracket_count > 0:
                            if expression[ptr_exp2_end] == "(":
                                bracket_count += 1
                            elif expression[ptr_exp2_end] == ")":
                                bracket_count -= 1
                            ptr_exp2_end += 1
                    multiplication_expression2 = simplify_expression(
                        expression[ptr_exp2_start:ptr_exp2_end])  # with brackets

                    multiplication_simplified = multiplication(multiplication_expression1, multiplication_expression2)
                    if len(multiplication_simplified) <= 1:
                        # no brackets
                        expression = expression[0:ptr_exp1_start] + multiplication_simplified + expression[
                                                                                                ptr_exp2_end:]
                        ptr = ptr_exp1_start + len(multiplication_simplified)
                    else:
                        # brackets
                        expression = expression[0:ptr_exp1_start] + ["("] + multiplication_simplified + [")"] + expression[
                                                                                                ptr_exp2_end:]
                        ptr = ptr_exp1_start + 1 + len(multiplication_simplified) + 1

                elif is_variable(expression[ptr]):
                    expression = expression[0:ptr] + multiplication(["1"], [expression[ptr]]) + expression[
                                                                                                ptr + 1:]
                    ptr+=1
                else:
                    ptr += 1

            map = collections.defaultdict(int)
            for exp in expression:
                if exp in ["(", ")"]:
                    continue
                add(map, exp)

            map_order = sorted(map, key=lambda x: (-1*map[x][0], x, map[x][1]))
            output = []
            for key in map_order:
                if map[key][1] == 0:
                    continue
                exp = str(map[key][1]) + " " + str(key)
                output.append(exp.strip())

            return output

        simplified = simplify_expression(evaluated_expression)
        for index, simple in enumerate(simplified):
            simplified[index] = simple.strip().replace(" ", "")

        return simplified


if __name__ == '__main__':
    print(Solution().basicCalculatorIV("(av * 9) - (ar + 0) - ((bq - cv) + v * (b + bq - bk)) * (a - 12 + 2 - (6 * cc - 8 - bv + ag))", ["d", "g", "h", "j", "l", "o", "s", "u", "v", "w", "af", "ag", "ah", "ak", "at", "au", "av", "aw", "az", "bc", "be", "bg", "bj", "bm", "bn", "bq", "br", "bs", "bt", "bu", "bv", "bw", "bx", "by", "bz", "ca", "cd", "ce", "cf", "ch", "ci", "ck", "cq", "cr", "cs", "cu", "cv"], [3, 6, 7, 9, 11, 1, 5, 7, 8, 9, 10, 11, 12, 2, 11, 12, 0, 1, 4, 12, 1, 3, 6, 9, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 5, 6, 7, 9, 10, 12, 5, 6, 7, 9, 10]))
    # print(Solution().basicCalculatorIV("((a - b) * (b - c) + (c - a))", [], []))
    # print(Solution().basicCalculatorIV("a + (a - b)", [], []))
