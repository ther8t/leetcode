import math


class Solution:
    # Wrong Answer: Average doesn't mean that the sum will always be less.
    def getMinDistSum(self, positions) -> float:
        n = len(positions)
        xavg, yavg = sum([x[0] for x in positions]) / n, sum([y[1] for y in positions]) / n
        min_sum = float('inf')

        for rx, ry in [(0, 0)]:
            nx, ny = xavg + rx, yavg + ry
            current_sum = 0
            for x, y in positions:
                current_sum += math.sqrt((nx - x)**2 + (ny - y)**2)
            min_sum = min(min_sum, current_sum)

        return round(min_sum, 5)


    # def getMinDistSum(self, positions) -> float:
    #     n = len(positions)
    #     minx, miny, maxx, maxy = min([x[0] for x in positions]), min([y[1] for y in positions]), max([x[0] for x in positions]), max([y[1] for y in positions])
    #     min_sum = float('inf')
    #
    #     for cx in range(minx, maxx + 1):
    #         for cy in range(miny, maxy + 1):
    #             current_sum = 0
    #             for x, y in positions:
    #                 current_sum += math.sqrt((cx - x) ** 2 + (cy - y) ** 2)
    #             min_sum = min(min_sum, current_sum)
    #
    #     return round(min_sum, 5)


if __name__ == '__main__':
    # print(Solution().getMinDistSum(positions = [[0,1],[1,0],[1,2],[2,1]]))
    # print(Solution().getMinDistSum(positions = [[1,1],[3,3]]))
    print(Solution().getMinDistSum([[1,1],[0,0],[2,0]]))
