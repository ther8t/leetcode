class Solution:
    def findMinArrowShots(self, points) -> int:
        points.sort()

        arrows = 0
        intersection = [float('-inf'), float('inf')]
        for s, e in points:
            intersection = [max(s, intersection[0]), min(e, intersection[1])]
            if intersection[1] < intersection[0]:
                arrows += 1
                intersection = [s, e]

        return arrows + 1


if __name__ == '__main__':
    print(Solution().findMinArrowShots(points = [[10,16],[2,8],[1,6],[7,12]]))
    print(Solution().findMinArrowShots(points = [[1,2],[3,4],[5,6],[7,8]]))
    print(Solution().findMinArrowShots(points = [[1,2],[2,3],[3,4],[4,5]]))
