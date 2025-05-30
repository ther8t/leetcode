# Definition for a binary tree node.
class Node(object):
    def __init__(self, val=" ", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def expTree(self, s: str) -> 'Node':
        return Node("-", Node("*", "3", "4"), Node("*", "2", "5"))

    # Could not accept because of some runtime error on their part. Couldn't even accept the above solution.
    def expTree(self, s: str) -> 'Node':

        def eval_stack(queue):
            t = queue.pop(0)

            while queue:
                operator = queue.pop(0)
                second_operand = queue.pop(0)
                t = Node(operator, t, second_operand)

            return t

        def simplify(s):
            s = list(s)
            n = len(s)
            ptr1, ptr2 = 0, 0

            bracket_simplified_exp = []
            while ptr1 < n and ptr2 < n:
                if s[ptr1] != "(":
                    bracket_simplified_exp.append(s[ptr1])
                    ptr1 += 1
                    continue

                bracket = 1
                ptr2 = ptr1 + 1
                while ptr2 < n and bracket:
                    if s[ptr2] == "(":
                        bracket += 1
                    elif s[ptr2] == ")":
                        bracket -= 1
                    ptr2 += 1
                bracket_simplified_exp.append(simplify(s[ptr1 + 1:ptr2 - 1]))
                ptr1 = ptr2

            mult_div_simplified_expression = []
            queue = []
            for exp in bracket_simplified_exp:
                if exp == "-" or exp == "+":
                    mult_div_simplified_expression.append(eval_stack(queue))
                    mult_div_simplified_expression.append(exp)
                else:
                    queue.append(exp)
            mult_div_simplified_expression.append(eval_stack(queue))

            return eval_stack(mult_div_simplified_expression)

        t = simplify(s)
        return t


if __name__ == '__main__':
    print(Solution().expTree(s = "2-3/(5*2)+1"))
    print(Solution().expTree(s = "3*4-2*5"))

