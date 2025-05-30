class Solution:

    """
    Revision 2:
    The question was simple but a bit complicated to imagine. It's like working a stack.
    """
    def generateParenthesis(self, n):
        out = []

        def generate(current, open, close):
            nonlocal out
            if open == 0 and close == 0:
                return out.append(current)

            if open:
                generate(current + "(", open - 1, close)
            if close > open:
                generate(current + ")", open, close - 1)

        generate("", n, n)
        return out



    # def generateParenthesis(self, n):
    #     if n == 1:
    #         return ["()"]
    #
    #     output = set()
    #     subParanthesis = self.generateParenthesis(n - 1)
    #     for i in subParanthesis:
    #         output.add("()" + i)
    #         output.add("(" + i + ")")
    #         output.add(i + "()")
    #
    #     return output
    #
    # def isMirrorImage(self, string):
    #     if string is None:
    #         return False
    #     s = string.split("()")
    #     for i in s:
    #         if i:
    #             return False
    #     return True


    def generateParenthesis(self, n):
        paranthesis = set()

        def gen_para(current, left, right):
            if left == 0 and right == 0:
                paranthesis.add(current)
                return

            if left > 0:
                gen_para(current + "(", left - 1, right)
            if right > left:
                gen_para(current + ")", left, right - 1)

        gen_para("", n, n)
        return paranthesis

    def generateParenthesis(self, n):
        def genPara(n):
            if n <= 0:
                return [""]

            output = set()

            for p in genPara(n - 1):
                output.add("()" + p)
                output.add(p + "()")
                output.add("(" + p + ")")

            return output

        return genPara(n)




if __name__ == '__main__':
    a = Solution().generateParenthesis(3)
    s = "()(())"
    print(a)
