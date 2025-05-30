class Solution:

    """
    Revision 2 :
    I had to think a bit but the question was solved.
    """
    # Accepted 56%
    def lengthLongestPath(self, input: str) -> int:
        paths = input.split("\n")
        levels = []
        for index, path in enumerate(paths):
            levels.append(path.count('\t'))
            paths[index] = self.clean(paths[index])

        stack = []
        current_level = -1
        current_max_length = 0
        for i in range(len(paths)):
            if levels[i] <= current_level:
                for _ in range(current_level - levels[i] + 1):
                    stack.pop()
            stack.append(paths[i])
            current_level = levels[i]
            if paths[i].find(".") != -1:
                current_max_length = max(current_max_length, self.calculate_length(stack))

        return current_max_length

    def calculate_length(self, stack):
        """
        Revision 2:
        I even found another way to write this simply.
        """
        return len("/".join(stack))
        # length = 0
        # for i in stack:
        #     length += len(i)
        # return len(stack) - 1 + length

    def clean(self, input: str):
        return input.replace("\t", "").replace("\n", "")


if __name__ == '__main__':
    print(Solution().lengthLongestPath("a"))
