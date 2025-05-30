class Solution:
    def isValid(self, s: str) -> bool:
        openingBrackets = {'(', '{', '['}
        closingBrackets = {')', '}', ']'}
        mapBrackets = {')': '(', '}': '{', ']': '['}

        stack = []
        for char in s:
            if char in openingBrackets:
                stack.append(char)
            elif char in closingBrackets:
                if len(stack) > 0 and mapBrackets.get(char) == stack[-1]:
                    stack.pop()
                else:
                    return False
        return not stack


if __name__ == '__main__':
    print(Solution().isValid('}'))
    # a = [1,2]
    # print(a[-2])
