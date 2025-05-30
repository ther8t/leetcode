class Solution:
    """
    Revision 2:
    An amazing thing just happened. I remember that I need to solve this question because I remember the last time I solved this question a portion of the water container was repeated.
    I have to take care of that. For some reason I was not able to figure how it was that container was formed.
    So I coded the entire thing again. To my surprise I had already considered the condition to use, greater than on one monotonic stack and greater than equal to on the other.
    Which was the condition I could not figure out in the previous iteration. This came to me by default.
    I now declare this question REVISED!!
    """
    def trap(self, height):
        n = len(height)
        next_greater = [n] * n
        prev_greater_equal = [-1] * n

        stack = []
        for i in range(n):
            while stack and height[stack[-1]] < height[i]:
                next_greater[stack.pop()] = i
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and height[stack[-1]] <= height[i]:
                prev_greater_equal[stack.pop()] = i
            stack.append(i)


        trapped_water = 0
        ptr = 0
        while ptr < n:
            if next_greater[ptr] < n:
                top = height[ptr]
                for i in range(ptr, next_greater[ptr]):
                    trapped_water += (top - height[i])
            ptr = next_greater[ptr]

        ptr = n - 1
        while ptr >= 0:
            if prev_greater_equal[ptr] >= 0:
                top = height[ptr]
                for i in range(ptr, prev_greater_equal[ptr] - 1, -1):
                    trapped_water += (top - height[i]) if (top - height[i]) > 0 else 0
            ptr = prev_greater_equal[ptr]

        return trapped_water




    def trap(self, height):
        n = len(height)
        next_greater = [n] * n
        prev_greater = [-1] * n

        stack = []
        for i in range(n):
            while stack and height[stack[-1]] <= height[i]:
                next_greater[stack.pop()] = i
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and height[stack[-1]] < height[i]:
                prev_greater[stack.pop()] = i
            stack.append(i)

        trapped_water = 0
        ptr = 0
        while ptr < n:
            nge = next_greater[ptr]
            if nge != n:
                for i in range(ptr + 1, nge):
                    trapped_water += (height[ptr] - height[i])
            ptr = nge

        ptr = n - 1
        while ptr >= 0:
            pge = prev_greater[ptr]
            if pge != -1:
                for i in range(pge + 1, ptr):
                    trapped_water += (height[ptr] - height[i])
            ptr = pge

        return trapped_water



    # # TLE
    # def trap(self, height):
    #     if len(height) <= 2:
    #         return 0
    #     totalWater = 0
    #
    #     # find the tallest and the second tallest in the range
    #     tallestIndex = -1
    #     secondTallestIndex = -1
    #
    #     for i in range(len(height)):
    #         if height[i] >= height[tallestIndex] or tallestIndex == -1:
    #             tallestIndex = i
    #
    #     for i in range(len(height)):
    #         if (height[i] >= height[secondTallestIndex] or secondTallestIndex == -1) and i != tallestIndex:
    #             secondTallestIndex = i
    #
    #     for i in range(min(tallestIndex, secondTallestIndex), max(tallestIndex, secondTallestIndex) + 1):
    #         waterLevel = height[secondTallestIndex] - height[i]
    #         if waterLevel > 0:
    #             totalWater += waterLevel
    #
    #     totalWater += self.trap(height[0:min(tallestIndex, secondTallestIndex) + 1])
    #     totalWater += self.trap(height[max(tallestIndex, secondTallestIndex):])
    #
    #     return totalWater


    """
    Attempt #2
    """
    def trap(self, height):
        n = len(height)
        next_greater = [n] * n
        prev_greater_equal = [-1] * n
        s = []

        for index in range(n):
            while s and height[s[-1]] < height[index]:
                next_greater[s.pop()] = index
            s.append(index)

        s = []
        for index in range(n - 1, -1, -1):
            while s and height[s[-1]] <= height[index]:
                prev_greater_equal[s.pop()] = index
            s.append(index)

        trapped_water = 0
        ptr = 0
        while ptr < n and next_greater[ptr] < n:
            top = min(height[ptr], height[next_greater[ptr]])
            for i in range(ptr, next_greater[ptr]):
                trapped_water += top - height[i]
            ptr = next_greater[ptr]

        ptr = n - 1
        while ptr >= 0 and prev_greater_equal[ptr] >= 0:
            top = min(height[ptr], height[prev_greater_equal[ptr]])
            for i in range(ptr, prev_greater_equal[ptr], -1):
                trapped_water += top - height[i]
            ptr = prev_greater_equal[ptr]

        return trapped_water


if __name__ == '__main__':
    # print(Solution().trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))
    print(Solution().trap(height = [4,2,0,3,2,5]))
    # print(Solution().trap(height = [2, 0, 2]))
    # print(Solution().trap([4, 2, 3]))
