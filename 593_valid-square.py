import math


class Solution:
    def validSquare(self, p1, p2, p3, p4) -> bool:
        remaining = [p2, p3, p4]
        adjacent = []
        for i in range(len(remaining)):
            for j in range(i + 1, len(remaining)):
                if '%.5f' % abs(math.atan2(remaining[i][1] - p1[1], remaining[i][0] - p1[0]) - math.atan2(
                p1[1] - remaining[j][1],
                p1[0] - remaining[j][0])) in ['%.5f' % (math.pi / 2), '%.5f' % (2 * math.pi - math.pi / 2)]:
                    point1, point2 = remaining[i], remaining[j]
                    adjacent.append(point1)
                    adjacent.append(point2)
                    remaining.remove(point1)
                    remaining.remove(point2)
                    break

        if len(adjacent) == 0:
            return False

        def distance(p1, p2):
            return pow(pow(p1[1] - p2[1], 2) + pow(p1[0] - p2[0], 2), 0.5)

        if distance(p1, adjacent[0]) == distance(p1, adjacent[1]) == distance(remaining[0], adjacent[0]) == distance(
                remaining[0], adjacent[1]):
            return True

        return False


if __name__ == '__main__':
    print(Solution().validSquare([3127,253]
,[915,1225]
,[1535,-367]
,[2507,1845]))
