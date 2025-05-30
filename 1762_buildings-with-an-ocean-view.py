class Solution:
    def findBuildings(self, heights):
        n = len(heights)
        stack = []
        next_bigger = [n] * n

        for i, h in enumerate(heights):
            while stack and h >= heights[stack[-1]]:
                popped_index = stack.pop()
                next_bigger[popped_index] = i
            stack.append(i)

        return [index for index, i in enumerate(next_bigger) if i == n]


if __name__ == '__main__':
    print(Solution().findBuildings([2,2,2,2]))
