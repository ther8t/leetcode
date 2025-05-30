import collections
import math
from sortedcontainers import SortedList


class Solution:
    """
    Revision 2:
    I have to admit that this is not the most optimised solution but it is clever none the less.
    The brute force approach requires us to iterate over every point and permute making it O(n4).
    But what we can do is to make combinations of pairs of points and consider them diagonally opposite. We can derive the remaining two points very easily, the rectangle being x-y aligned.
    This gets accepted by 43%.
    """
    def minAreaRect(self, points) -> int:
        points_set = set()
        for x, y in points:
            points_set.add((x, y))

        min_area = float('inf')
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                (x1, y1), (x2, y2) = points[i], points[j]
                if x1 == x2 or y1 == y2:
                    continue
                if (x1, y2) in points_set and (x2, y1) in points_set:
                    min_area = min(min_area, abs(x2 - x1) * abs(y2 - y1))
        return min_area if min_area != float('inf') else 0


    """
    Revision 2:
    This is a great algo but a bit tough to imagine. The logic is simple though.
    A rectangle can only be formed enclosed by a pair of points having same y coordinates separated by some distance x. OR
    A pair of x coordinates separated by some distance y.
    We choose the first assumption.
    
    we make all possible combinations of y. such that (y1, y2) y2 > y1 and have same x. Thus they form a sort of column which stands perpendicular to x axis.
    All we need is another pair of same (y1, y2) separated by some distance x, but the distances should also be sorted in ascending order so we can be sure that the last pair of (y1, y2) we have is the closest, thus forming the rectangle with least possible area for x, y1 and y2.
    We thus update the x where we found the latest (y1, y2), so that future xs might be able to form a rectangle.
    """
    def minAreaRect(self, points) -> int:
        ys_for_xs = collections.defaultdict(list)

        for x, y in points:
            ys_for_xs[x].append(y)

        lastx = {}
        area = float('inf')
        for x in sorted(ys_for_xs):
            ys = ys_for_xs[x]
            ys.sort()
            """ This sort is very much necessary. It is used to keep the ys in order so that the key formed in lastx is in order and easy to find.
            Failing to do this we have to search for both permutations (i, j) and (j, i). This is computationally more expensive than running a sort.
            This sort serves no purpose in calculation of min area unlike the sort used in sorting x in sorted(ys_for_xs), which is to get the min area only."""
            for j in range(len(ys)):
                for i in range(j):
                    if (ys[j], ys[i]) in lastx:
                        area = min(area, abs((ys[j] - ys[i])*(x - lastx[(ys[j], ys[i])])))
                    lastx[(ys[j], ys[i])] = x
        return area if area != float('inf') else 0

    # # TLE : But this is important!!. TLE was because of SortedList and after removing the sorted list and adding ys.sort() we get the accepted by 80%
    # def minAreaRect(self, points) -> int:
    #     ys_for_xs = collections.defaultdict(SortedList)
    #
    #     for x, y in points:
    #         ys_for_xs[x].add(y)
    #
    #     lastx = {}
    #     area = float('inf')
    #     for x in sorted(ys_for_xs):
    #         ys = ys_for_xs[x]
    #         for j in range(len(ys)):
    #             for i in range(j):
    #                 if (ys[j], ys[i]) in lastx:
    #                     area = min(area, abs((ys[j] - ys[i])*(x - lastx[(ys[j], ys[i])])))
    #                 lastx[(ys[j], ys[i])] = x
    #     return area if area != float('inf') else 0

    # # TLE
    # def minAreaRect(self, points) -> int:
    #     xs_for_ys = collections.defaultdict(list)
    #
    #     for i in range(len(points)):
    #         for j in range(i + 1, len(points)):
    #             if points[j][0] == points[i][0]:
    #                 if points[j][1] > points[i][1]:
    #                     xs_for_ys[points[j][1], points[i][1]].append(points[j][0])
    #                 else:
    #                     xs_for_ys[points[i][1], points[j][1]].append(points[j][0])
    #
    #     area = float('inf')
    #     for i in xs_for_ys:
    #         xs = xs_for_ys[i]
    #         for j in range(len(xs)):
    #             for k in range(j):
    #                 area = min(area, abs((i[0] - i[1])*(xs[k] - xs[j])))
    #
    #     return area if area != float('inf') else 0

    # # TLE
    # def minAreaRect(self, points) -> int:
    #     vertical = collections.defaultdict(SortedList)
    #     horizontal = collections.defaultdict(SortedList)
    #
    #     points = [tuple(points[i]) for i in range(len(points))]
    #
    #     for i in range(len(points)):
    #         for j in range(i + 1, len(points)):
    #             if points[j][1] == points[i][1]:
    #                 horizontal[points[i]].add((abs(points[j][0] - points[i][0]), points[j]))
    #             elif points[j][0] == points[i][0]:
    #                 vertical[points[i]].add((abs(points[j][1] - points[i][1]), points[j]))
    #
    #     min_area = float('inf')
    #     for i in points:
    #         vertical_points = vertical[i]
    #         horizontal_points = horizontal[i]
    #
    #         for v in vertical_points:
    #             for h in horizontal_points:
    #                 last_point = (v[1][0] + (h[1][0] - i[0]), v[1][1])
    #                 if last_point in points:
    #                     area = abs(h[0] * v[0])
    #                     min_area = min(min_area, area)
    #
    #     return int(min_area) if min_area != float('inf') else 0

    # # TLE
    # def minAreaRect(self, points) -> int:
    #     vertical_distance_map = collections.defaultdict(list)
    #
    #     points = [tuple(points[i]) for i in range(len(points))]
    #
    #     for i in range(len(points)):
    #         for j in range(i + 1, len(points)):
    #             if points[j][0] == points[i][0]:
    #                 vertical_distance_map[abs(points[j][1] - points[i][1])].append((points[i], points[j]))
    #
    #     minarea = float('inf')
    #
    #     for distance in vertical_distance_map:
    #         vertical_points = vertical_distance_map[distance]
    #         for i in range(len(vertical_points)):
    #             for j in range(i + 1, len(vertical_points)):
    #                 p1 = vertical_points[i][0]
    #                 p2 = vertical_points[i][1]
    #                 p3 = vertical_points[j][0]
    #                 p4 = vertical_points[j][1]
    #
    #                 if p1[1] == p3[1] and p2[1] == p4[1]:
    #                     area = abs((p2[1] - p1[1])*(p3[0] - p1[0]))
    #                     minarea = min(area, minarea)
    #                 elif p1[1] == p4[1] and p2[1] == p3[1]:
    #                     area = abs((p2[1] - p1[1]) * (p4[0] - p1[0]))
    #                     minarea = min(area, minarea)
    #
    #     return 0 if minarea == float('inf') else int(minarea)

    # # TLE
    # def minAreaRect(self, points) -> int:
    #     vertical_distance_map = {}
    #     horizontal_distance_map = {}
    #
    #     points = [tuple(points[i]) for i in range(len(points))]
    #
    #     for i in range(len(points)):
    #         for j in range(i + 1, len(points)):
    #             slope = float('%.5f' % abs(math.atan2(points[j][1] - points[i][1], points[j][0] - points[i][0])))
    #             distance = pow(pow(points[j][1] - points[i][1], 2) + pow(points[j][0] - points[i][0], 2), 0.5)
    #             if slope == 0 or slope == float('%.5f' % math.pi):
    #                 horizontal_distance_map[(points[i], points[j])] = (points[i], points[j], distance)
    #             elif slope == float('%.5f' % (math.pi / 2)) or slope == float('%.5f' % (3 * math.pi / 2)):
    #                 vertical_distance_map[(points[i], points[j])] = (points[i], points[j], distance)
    #
    #     vertical_points_sorted = sorted(vertical_distance_map.values(), key=lambda x: x[2])
    #
    #     ptr1 = 0
    #     ptr2 = 0
    #     minarea = float('inf')
    #     if not vertical_distance_map or not horizontal_distance_map:
    #         return 0
    #
    #     while ptr1 < len(vertical_points_sorted) and ptr2 < len(vertical_points_sorted):
    #         while ptr2 < len(vertical_points_sorted) and vertical_points_sorted[ptr2][2] == \
    #                 vertical_points_sorted[ptr1][2]:
    #             ptr2 += 1
    #
    #         for i in range(ptr1, ptr2):
    #             for j in range(i + 1, ptr2):
    #                 p1 = vertical_points_sorted[i][0]
    #                 p2 = vertical_points_sorted[i][1]
    #                 p3 = vertical_points_sorted[j][0]
    #                 p4 = vertical_points_sorted[j][1]
    #
    #                 if (p1, p3) in horizontal_distance_map and (p2, p4) in horizontal_distance_map:
    #                     area = vertical_points_sorted[i][2] * horizontal_distance_map[(p1, p3)][2]
    #                     minarea = min(area, minarea)
    #                     continue
    #
    #                 if (p1, p3) in horizontal_distance_map and (p4, p2) in horizontal_distance_map:
    #                     area = vertical_points_sorted[i][2] * horizontal_distance_map[(p1, p3)][2]
    #                     minarea = min(area, minarea)
    #                     continue
    #
    #                 if (p3, p1) in horizontal_distance_map and (p2, p4) in horizontal_distance_map:
    #                     area = vertical_points_sorted[i][2] * horizontal_distance_map[(p1, p3)][2]
    #                     minarea = min(area, minarea)
    #                     continue
    #
    #                 if (p3, p1) in horizontal_distance_map and (p4, p2) in horizontal_distance_map:
    #                     area = vertical_points_sorted[i][2] * horizontal_distance_map[(p1, p3)][2]
    #                     minarea = min(area, minarea)
    #                     continue
    #
    #                 if (p1, p4) in horizontal_distance_map and (p2, p3) in horizontal_distance_map:
    #                     area = vertical_points_sorted[i][2] * horizontal_distance_map[(p1, p4)][2]
    #                     minarea = min(area, minarea)
    #                     continue
    #
    #                 if (p4, p1) in horizontal_distance_map and (p2, p3) in horizontal_distance_map:
    #                     area = vertical_points_sorted[i][2] * horizontal_distance_map[(p1, p4)][2]
    #                     minarea = min(area, minarea)
    #                     continue
    #
    #                 if (p1, p4) in horizontal_distance_map and (p3, p2) in horizontal_distance_map:
    #                     area = vertical_points_sorted[i][2] * horizontal_distance_map[(p1, p4)][2]
    #                     minarea = min(area, minarea)
    #                     continue
    #
    #                 if (p4, p1) in horizontal_distance_map and (p3, p2) in horizontal_distance_map:
    #                     area = vertical_points_sorted[i][2] * horizontal_distance_map[(p1, p4)][2]
    #                     minarea = min(area, minarea)
    #                     continue
    #
    #         ptr1 = ptr2
    #     return 0 if minarea == float('inf') else int(minarea)
    #


if __name__ == '__main__':
    print(Solution().minAreaRect(
        [[39465, 25332], [19034, 25498], [39465, 26069], [19034, 36989], [39465, 13961], [39465, 33772], [19034, 39015],
         [19034, 20403], [39465, 39481], [19034, 21081], [19034, 942], [39465, 21332], [39465, 14922], [39465, 2000],
         [19034, 23149], [39465, 28804], [19034, 8813], [19034, 23827], [19034, 36684], [19034, 30990], [19034, 296],
         [39465, 2224], [39465, 15737], [39465, 30990], [39465, 32404], [39465, 20752], [19034, 37694], [19034, 14922],
         [39465, 8198], [19034, 7165], [39465, 4873], [19034, 24552], [19034, 15440], [19034, 11794], [39465, 25498],
         [19034, 918], [39465, 1513], [19034, 2153], [19034, 10732], [39465, 15440], [19034, 14846], [19034, 10795],
         [39465, 28593], [19034, 8216], [19034, 20752], [39465, 14488], [19034, 14773], [19034, 32404], [39465, 21960],
         [19034, 1276], [19034, 12808], [39465, 37694], [19034, 39958], [39465, 18088], [19034, 27228], [19034, 28804],
         [19034, 2000], [19034, 34829], [39465, 31438], [19034, 21332], [39465, 14773], [39465, 24636], [19034, 13868],
         [39465, 5450], [39465, 2399], [19034, 34489], [19034, 23448], [19034, 26069], [39465, 942], [39465, 22435],
         [19034, 15070], [39465, 24798], [19034, 28593], [19034, 27564], [19034, 11267], [39465, 1629], [39465, 3088],
         [39465, 39506], [39465, 14328], [19034, 14424], [39465, 30491], [19034, 27735], [39465, 9111], [39465, 14424],
         [39465, 21089], [19034, 1629], [39465, 39882], [19034, 3735], [19034, 23505], [39465, 9618], [19034, 2224],
         [19034, 20537], [39465, 20346], [19034, 18830], [19034, 2449], [39465, 32360], [39465, 16087], [39465, 11025],
         [19034, 9639], [39465, 23448], [39465, 10022], [39465, 32833], [19034, 16503], [39465, 8368], [19034, 37189],
         [19034, 984], [19034, 20046], [19034, 25332], [19034, 32154], [39465, 27228], [19034, 32360], [19034, 3460],
         [39465, 4530], [19034, 2978], [19034, 33772], [39465, 27975], [19034, 8172], [39465, 12808], [19034, 39202],
         [19034, 21960], [39465, 33707], [39465, 13407], [39465, 25798], [19034, 14488], [19034, 2830], [19034, 38836],
         [19034, 16986], [39465, 2449], [19034, 8368], [39465, 29253], [39465, 8216], [39465, 10007], [39465, 20615],
         [19034, 14328], [39465, 27067], [19034, 34068], [19034, 1857], [19034, 8406], [19034, 24671], [39465, 32748],
         [39465, 10419], [39465, 28166], [39465, 27564], [19034, 35460], [19034, 2619], [39465, 30625], [39465, 34829],
         [39465, 32227], [19034, 4873], [39465, 1687], [39465, 19845], [39465, 34489], [19034, 22261], [19034, 22318],
         [39465, 29108], [39465, 39958], [19034, 24636], [39465, 26667], [39465, 35518], [19034, 36754], [19034, 659],
         [39465, 38235], [39465, 34319], [39465, 25493], [19034, 18088], [19034, 21159], [39465, 36684], [39465, 30337],
         [19034, 36215], [39465, 38742], [39465, 1276], [39465, 7568], [39465, 5074], [39465, 21081], [39465, 15121],
         [19034, 22127], [19034, 12276], [19034, 6177], [39465, 1749], [19034, 27619], [19034, 13961], [39465, 6481],
         [19034, 20327], [19034, 31184], [39465, 22424], [39465, 22599], [19034, 11727], [19034, 30036], [19034, 25082],
         [39465, 2153], [19034, 1513], [19034, 19144], [39465, 22643], [39465, 16326], [19034, 19453], [19034, 34319],
         [39465, 25600], [39465, 38753], [19034, 25536], [39465, 24552], [39465, 156], [39465, 7165], [39465, 16816],
         [39465, 34879], [39465, 30021], [19034, 37069], [39465, 36300], [19034, 12763], [19034, 16916], [19034, 32744],
         [19034, 17164], [39465, 14135], [39465, 16010], [39465, 2978], [19034, 22599], [39465, 9636], [19034, 32541],
         [19034, 15737], [19034, 22450], [39465, 33814], [39465, 296], [19034, 32732], [19034, 15307], [39465, 38308],
         [19034, 16326], [39465, 18188], [39465, 8813], [39465, 769], [19034, 39005], [19034, 30021], [19034, 33311],
         [39465, 19243], [19034, 18503], [39465, 32744], [19034, 39481], [19034, 28440], [19034, 3636], [19034, 37366],
         [39465, 37366], [39465, 34941], [39465, 11824], [19034, 5074], [39465, 30125], [39465, 20033], [39465, 19453],
         [19034, 38742], [19034, 24798], [19034, 15832], [19034, 30229], [39465, 22894], [39465, 5199], [39465, 25225],
         [39465, 36330], [39465, 7493], [39465, 22450], [39465, 659], [39465, 1420], [19034, 14135], [19034, 33814],
         [39465, 10795], [39465, 8062], [39465, 14846], [19034, 29909], [19034, 29108], [19034, 1687], [39465, 25320],
         [39465, 35740], [19034, 25054], [39465, 25054], [19034, 28166], [19034, 22643], [19034, 31513], [39465, 12399],
         [19034, 14493], [39465, 8406], [39465, 3344], [39465, 37566], [19034, 2980], [39465, 4036], [19034, 20615],
         [39465, 20327], [19034, 30447], [39465, 17268], [39465, 27619], [19034, 17628], [39465, 39633], [39465, 26788],
         [19034, 25798], [19034, 5199], [19034, 23903], [39465, 23328], [19034, 28116], [39465, 28116], [39465, 36215],
         [39465, 39857], [19034, 39633], [19034, 27975], [39465, 34028], [39465, 21159], [19034, 15121], [19034, 4036],
         [19034, 3344], [39465, 36857], [19034, 30337], [39465, 30447], [19034, 18188], [39465, 28125], [19034, 35518],
         [39465, 33311], [19034, 28153], [19034, 12399], [19034, 16087], [39465, 29909], [19034, 32227], [19034, 7772],
         [39465, 15307], [39465, 32453], [19034, 10419], [19034, 9618], [19034, 36920], [39465, 38685], [19034, 8062],
         [19034, 16010], [39465, 10732], [19034, 22424], [39465, 12763], [19034, 6481], [19034, 9111], [39465, 30229],
         [39465, 27735], [39465, 27133], [19034, 39857], [19034, 36330], [19034, 24601], [19034, 39506], [19034, 3832],
         [19034, 22894], [19034, 20033], [39465, 39202], [19034, 23328], [39465, 11267], [19034, 26788], [39465, 24281],
         [19034, 4530], [19034, 17268], [39465, 11727], [39465, 32552], [39465, 2980], [39465, 34745], [19034, 24281],
         [39465, 32877], [19034, 769], [39465, 35516], [39465, 16503], [19034, 37566], [19034, 19243], [19034, 36057],
         [19034, 10022], [39465, 24601], [39465, 8172], [39465, 9639], [19034, 21089], [39465, 23149], [39465, 3709],
         [39465, 12184], [39465, 15834], [39465, 29613], [19034, 38235], [39465, 16916], [19034, 32552], [19034, 38685],
         [19034, 7493], [39465, 13868], [19034, 29613], [19034, 21060], [39465, 25536], [19034, 25600], [19034, 3709],
         [39465, 11583], [39465, 7772], [19034, 34879], [19034, 32748], [39465, 30036], [19034, 28125], [39465, 918],
         [19034, 35516], [19034, 15834], [39465, 31184], [39465, 35460], [39465, 24671], [39465, 11794], [19034, 11824],
         [19034, 32877], [19034, 34745], [39465, 25082], [19034, 1749], [39465, 3636], [39465, 20537], [19034, 22435],
         [39465, 36754], [19034, 7568], [19034, 8198], [39465, 16986], [39465, 33523], [39465, 2830], [39465, 22127],
         [19034, 13407], [19034, 9636], [39465, 3832], [19034, 25493], [19034, 27133], [39465, 17628], [39465, 23827],
         [39465, 984], [39465, 32154], [39465, 20046], [39465, 14493], [19034, 19845], [19034, 26667], [19034, 16816],
         [39465, 36920], [39465, 31513], [19034, 38308], [39465, 22318], [19034, 38753], [19034, 35740], [39465, 20563],
         [39465, 28153], [39465, 2619], [39465, 18830], [39465, 1857], [39465, 34068], [39465, 36989], [19034, 30851],
         [19034, 29253], [39465, 21060], [19034, 39882], [19034, 1420], [19034, 36857], [19034, 27067], [39465, 6177],
         [39465, 12276], [19034, 25225], [39465, 12055], [19034, 11583], [39465, 15832], [19034, 34028], [39465, 33863],
         [19034, 30491], [39465, 32541], [19034, 27379], [19034, 33707], [39465, 3460], [19034, 10259], [39465, 23903],
         [19034, 22750], [39465, 15070], [39465, 37189], [39465, 28440], [39465, 3735], [19034, 32833], [39465, 22261],
         [19034, 2399], [39465, 39005], [19034, 11025], [19034, 5450], [39465, 20403], [39465, 36057], [39465, 39015],
         [39465, 18503], [19034, 31438], [19034, 32453], [19034, 30625], [19034, 12184], [39465, 32732], [19034, 25320],
         [39465, 23505], [39465, 10259], [39465, 17164], [19034, 20346], [19034, 39351], [19034, 34941], [19034, 33863],
         [39465, 27379], [19034, 36300], [39465, 37069], [39465, 38836], [19034, 10007], [19034, 156], [19034, 3088],
         [19034, 33523], [19034, 12055], [39465, 19144], [39465, 30851], [39465, 39351], [39465, 22750], [19034, 30125],
         [19034, 20563]]))
    print(Solution().minAreaRect([[3,2],[0,0],[3,3],[3,4],[4,4],[2,1],[4,3],[1,0],[4,1],[0,2]]))
