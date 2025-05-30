class Solution:

    """
    Revision 2 : This is a brilliant peice of code where we convert an O(n2) to O(n). We need to find the maximum value which ccan be added.
    For that we can compare all the values for all the indexes in the next row. But we instead take a rolling maximum value from both directions, left to right and right to left.
    Let's take an array [0, 4, 2, 1]. The max value 0 index can have from the left is nothing. Between nothing and itself it chooses itself, so that's the base.
    [0, _, _, _]. For index 1, the max from left would be 0 - 1(because of the distance.) = -1. Between itself and -1, max = 4. [0, 4, _, _]
    For index 2, the max from left would be max@(index 1) - 1 = 3 and 2, so 3.
    This is a bit confusing to intuit. Either the max is left - 1 or itself. Itself part is pretty clear but how left - 1? For left of the index, either that is itself or some reduction of it's previous left.
    Whatever is the reason, we can take the same value the left did.
    For example : [4, 3, 1] Index 1 could have chosen itself 3 - 0, or it could have chosen 4 - 1 = 3. Either would have given the same result.
    But for [4, 2, 1]. For 4 - 1 > 2 - 0. That's pretty basic.
    For index 2 in both these cases, index 0 - 2 produces the required max so for first, Index 2 could have been Index 0 - 1 - 1, or Index 1 - 1, same thing.
    For second, Index 2 could only have been Index 0 - 1 - 1, which is nothing but Index 1 - 1
    The problem of O(n2) gets reduced to O(n).
    """
    def maxPoints(self, points) -> int:
        a = [[0 for _ in range(len(points[0]))] for _ in range(len(points))]

        rows, cols = len(points), len(points[0])

        a[-1] = points[-1]

        for row in range(rows - 1, 0, -1):
            left = [0 for _ in range(cols)]
            right = [0 for _ in range(cols)]
            left[0] = a[row][0]
            right[-1] = a[row][-1]

            for col in range(1, cols):
                left[col] = max(left[col - 1] - 1, a[row][col])
            for col in range(cols-2, -1, -1):
                right[col] = max(right[col + 1] - 1, a[row][col])

            for col in range(cols):
                a[row][col] = max(left[col], right[col])
                a[row-1][col] = points[row-1][col] + a[row][col]

        maxScore = 0
        for col in range(cols):
            maxScore = max(maxScore, a[0][col])

        return maxScore

    def maxPoints(self, points) -> int:
        rows, cols = len(points), len(points[0])

        current = points[0]
        prev = [0] * cols

        for row in range(rows):
            for i in range(1, cols):
                prev[i] = max(prev[i - 1] - 1, prev[i])
            for i in range(cols - 2, -1, -1):
                prev[i] = max(prev[i + 1] - 1, prev[i])
            for i in range(cols):
                current[i] = points[row][i] + prev[i]
            prev = current

        return max(current)

    # """
    # Revision 2 : This is the brute force approach. TLEs
    # """
    # def maxPoints(self, points) -> int:
    #     a = [[0 for _ in range(len(points[0]))] for _ in range(len(points))]
    #
    #     rows, cols = len(points), len(points[0])
    #
    #     a[-1] = points[-1]
    #
    #     for row in range(rows - 2, -1, -1):
    #         for i in range(cols):
    #             current_max = 0
    #             for j in range(cols):
    #                 current_max = max(current_max, a[row + 1][j] + points[row][i] - abs(j - i))
    #             a[row][i] = current_max
    #
    #     return max(a[0])

    # def maxPoints(self, points) -> int:
    #     a = [[0 for _ in range(len(points[0]))] for _ in range(len(points))]
    #
    #     a[-1] = points[-1]
    #
    #     beginIndex = 0
    #     endIndex = len(points[0]) - 1
    #     for i in range(len(points) - 1, 0, -1):
    #         # find the max in the row
    #         maxValue = 0
    #         maxValueIndex = 0
    #         for j in range(beginIndex, endIndex + 1):
    #             if a[i][j] > maxValue:
    #                 maxValue = a[i][j]
    #                 maxValueIndex = j
    #         beginIndex = max(maxValueIndex-points[i][maxValueIndex], 0)
    #         endIndex = min(maxValueIndex + points[i][maxValueIndex], len(points[0])-1)
    #         for j in range(beginIndex, endIndex+1):
    #             a[i-1][j] = points[i-1][j] + a[i][maxValueIndex] - abs(maxValueIndex - j)
    #
    #     print(a[0], beginIndex, endIndex)
    #     ultimateMaxPoints = 0
    #     for i in range(beginIndex, endIndex + 1):
    #         ultimateMaxPoints = max(ultimateMaxPoints, a[0][i])
    #
    #     return ultimateMaxPoints


# # TLE
# def maxPoints(self, points) -> int:
#     if len(points) == 1:
#         return sorted(points[0])[-1]
#
#     a = [[0 for _ in range(len(points[0]))] for _ in range(len(points))]
#
#     for i in range(len(points[0])):
#         a[-1][i] = points[-1][i]
#
#     rows = len(points)
#     cols = len(points[0])
#     overallMax = 0
#     for i in range(rows - 2, -1, -1):
#         overallMax = 0
#         for j in range(cols - 1, -1, -1):
#             maxPoints = 0
#             for k in range(max(0, j-points[i][j]), min(cols, j+points[i][j] + 1)):
#                 point = a[i + 1][k] - abs(k - j) + points[i][j]
#                 maxPoints = max(point, maxPoints)
#             a[i][j] = maxPoints
#             overallMax = max(overallMax, maxPoints)
#
#     # maxPoints = 0
#     # for i in range(cols):
#     #     maxPoints = max(a[0][i], maxPoints)
#
#     return overallMax

if __name__ == '__main__':
    print(Solution().maxPoints(points=[[1,5],[3,2],[4,2]]))
    print(Solution().maxPoints(points=[[1,2,3],[1,5,1],[3,1,1]]))
