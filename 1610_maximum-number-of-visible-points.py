import math


class Solution:
    def visiblePoints(self, points, angle: int, location) -> int:
        angles = []
        samePoint = 0
        for point in points:
            if point == location:
                samePoint += 1
                continue
            angles.append(self.findAngle(location, point))

        angles.sort()
        n = len(angles)
        angles += [a + 360 for a in angles]

        print(angles)
        maxVisibility = 0
        left = 0
        right = 0
        while left < n:
            while right < 2 * n and angles[right] - angles[left] <= angle:
                right += 1
            maxVisibility = max(maxVisibility, right - left)
            while left < n and angles[right] - angles[left] > angle:
                left += 1
        return maxVisibility + samePoint

    # def visiblePoints(self, points, angle: int, location) -> int:
    #     maxVisiblePoints = 0
    #
    #     for pointer in points:
    #         # print(f"{pointer}")
    #         currentVisiblePointSide1 = 0
    #         currentVisiblePointSide2 = 0
    #         # if pointer == location:
    #         #     continue
    #         for point in points:
    #             delta = self.findAngle(pointer, location, point)
    #             # print(f"{delta} for {point}")
    #             if point == location or (0 <= delta <= angle):
    #                 currentVisiblePointSide1 += 1
    #             if point == location or (0 >= delta >= (-1 * angle)):
    #                 currentVisiblePointSide2 += 1
    #         # print(f"{currentVisiblePointSide1}, {currentVisiblePointSide2}")
    #         maxVisiblePoints = max(maxVisiblePoints, max(currentVisiblePointSide1, currentVisiblePointSide2))
    #         # print("")
    #     return maxVisiblePoints
    #
    # def findAngle(self, pointer, pivot, point):
    #     angleLinePointer = self.simplifyAngle(math.atan2(
    #         (pointer[1] - pivot[1]), (pointer[0] - pivot[0])) * 180 / math.pi)
    #     angleLinePoint = self.simplifyAngle(math.atan2(
    #         (point[1] - pivot[1]), (point[0] - pivot[0])) * 180 / math.pi)
    #     delta = angleLinePoint - angleLinePointer
    #
    #     return self.simplifyAngle(delta)

    def findAngle(self, pivot, point):
        return self.simplifyAngle(math.atan2(
            (point[1] - pivot[1]), (point[0] - pivot[0])) * 180 / math.pi)

    def simplifyAngle(self, angle):
        return angle
        # return angle if angle >= 0 else angle + 360

    # def visiblePoints(self, points, angle: int, location) -> int:
    #     maxVisiblePoints = 0
    #     for lineHelperPoint in points:
    #         lowerLineInclination = tanLower = 0
    #         try:
    #             lowerLineInclination = tanLower = (lineHelperPoint[1] - location[1]) / (
    #                     lineHelperPoint[0] - location[0])
    #         except:
    #             pass
    #         upperLineInclination = tanUpper = (math.tan(math.pi * angle / 180) + tanLower) / (
    #                 1 - math.tan(math.pi * angle / 180) * tanLower)
    #         sideEnsuringLineInclination = math.pi + (lowerLineInclination + math.pi * angle / 180 / 2)
    #
    #         currentMaxVisible = 0
    #         sideValue = (lineHelperPoint[1] - location[1]) - sideEnsuringLineInclination * (
    #                     lineHelperPoint[0] - location[0])
    #         sideValue = (sideValue // abs(sideValue))
    #         for detectablePoint in points:
    #             x = detectablePoint[0]
    #             y = detectablePoint[1]
    #             lowerLineEqSolution = (y - location[1]) - lowerLineInclination * (x - location[0])
    #             upperLineEqSolution = (y - location[1]) - upperLineInclination * (x - location[0])
    #             sideEnsuringLineEqSolution = (y - location[1]) - sideEnsuringLineInclination * (x - location[0])
    #             currentSideValue = (sideEnsuringLineEqSolution // abs(sideEnsuringLineEqSolution))
    #             diffAngle = self.findAngle(lineHelperPoint, location, detectablePoint)
    #             print(diffAngle)
    #             if lowerLineEqSolution * upperLineEqSolution <= 0 and sideValue == currentSideValue:
    #                 currentMaxVisible += 1
    #         maxVisiblePoints = max(currentMaxVisible, maxVisiblePoints)
    #         print(f'{maxVisiblePoints} at {lineHelperPoint}')
    #         print("")
    #     return maxVisiblePoints


if __name__ == '__main__':
    # print(Solution().visiblePoints(
    #     points=[[2, 1], [2, 2], [3, 3]], angle=90, location=[1, 1]))  # ans 3
    # print(Solution().visiblePoints(
    #     points=[[2, 1], [2, 2], [3, 4], [1, 1]], angle=90, location=[1, 1]))  # ans 4
    # print(Solution().visiblePoints(
    #     points=[[1, 0], [2, 1]], angle=13, location=[1, 1]))  # ans 1
    # print(Solution().visiblePoints(
    #     [[0, 0], [0, 2]]
    #     , 90
    #     , [1, 1]))  # ans 2
    # print(Solution().visiblePoints(
    #     [[34, 26], [35, 95], [31, 56], [84, 75], [26, 76], [22, 15], [26, 78], [90, 41], [94, 18], [12, 88], [42, 82],
    #      [27, 0], [85, 49], [69, 71], [13, 36], [59, 58], [58, 18], [21, 62]]
    #     , 15
    #     , [67, 91]))  # ans 4
    print(Solution().visiblePoints(
        [[1, 1], [2, 2], [3, 3], [4, 4], [1, 2], [2, 1]]
        , 0
        , [1, 1]))  # ans 4
    # print(Solution().visiblePoints(
    #     [[55, 14], [60, 61], [58, 47], [17, 26], [87, 97], [63, 63], [26, 50], [70, 21], [3, 89], [51, 24], [6, 51],
    #      [64, 21], [66, 33], [54, 35], [87, 38], [30, 0], [37, 92], [92, 12], [60, 73], [75, 98], [1, 11], [88, 24],
    #      [82, 92]]
    #     , 44
    #     , [15, 50]))  # ans 11
    # print(Solution().visiblePoints([[1, 1], [1, 1], [1, 1]]
    #                                , 1
    #                                , [1, 1]))  # ans 3
    # print(Solution().findAngle([0, 2], [1, 1], [0, 0]))
    # print(Solution().findAngle([2, 0], [0, 0], [-1, 1]))
    # print(Solution().findAngle([2, 0], [0, 0], [-1, 1]))

    print(math.atan2(0, 1))
