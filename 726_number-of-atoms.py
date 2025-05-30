import collections


class Solution:
    def countOfAtoms(self, formula: str) -> str:

        def countAtoms(formula, multiplication):
            ptr = 0
            elements = collections.defaultdict(int)
            while ptr < len(formula):
                if formula[ptr] == "(":
                    left_count = 1
                    right_count = 0
                    ptr_start = ptr
                    ptr_end = ptr + 1
                    name_start = ptr + 1
                    while left_count != right_count:
                        if formula[ptr_end] == "(":
                            left_count += 1
                        if formula[ptr_end] == ")":
                            right_count += 1
                        ptr_end += 1
                    name_end = ptr_end - 1

                    while ptr_end < len(formula) and ord('0') <= ord(formula[ptr_end]) <= ord('9'):
                        ptr_end += 1

                    sub_formula = formula[name_start:name_end]
                    sub_formula_multiplier = int(formula[name_end + 1:ptr_end]) if len(formula[name_end + 1:ptr_end])>0 else 1
                    sub_formula = countAtoms(sub_formula, sub_formula_multiplier)
                    formula = formula[0:ptr_start] + sub_formula + formula[ptr_end:]
                if ord('A') <= ord(formula[ptr]) <= ord('Z'):
                    # new element begun
                    name = formula[ptr]
                    ptr += 1
                    while ptr < len(formula) and ord('a') <= ord(formula[ptr]) <= ord('z'):
                        name += formula[ptr]
                        ptr += 1
                    times = 0
                    while ptr < len(formula) and ord('0') <= ord(formula[ptr]) <= ord('9'):
                        times *= 10
                        times += (ord(formula[ptr]) - ord('0'))
                        ptr += 1
                    elements[name] += max(times, 1)

            simplified_formula = ""
            for i in sorted(elements):
                simplified_formula += i
                simplified_formula += str(multiplication * elements[i]) if multiplication * elements[
                    i] != 1 else ""

            return simplified_formula
        return countAtoms(formula, 1)


if __name__ == '__main__':
    # print(Solution().countOfAtoms(
    #     "(N13O9Be)37(LiC50B35)38(Li33HHBe14He5ON50N)27(H3C)2He14C34Li33C33He15N14N5Li24Li17H28O13H42(HeHe6CO11Li)35(He3O27HO5N21H49O39CH37B3)8(O41He27He46He22He17)12"))
    print(Solution().countOfAtoms("(H)"))
