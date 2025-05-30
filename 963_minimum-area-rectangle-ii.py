import collections
import math


class Solution:
    def find_slope(self, point1, point2):
        return round(math.atan2((point2[1] - point1[1]), (point2[0] - point1[0])), 5)


    def find_distance(self, point1, point2):
        return pow(pow(point2[1] - point1[1], 2) + pow(point2[0] - point1[0], 2), 0.5)

    def find_angle(self, point1, point2, point3):
        if point1 == point2 or point2 == point3 or point3 == point1:
            return 0
        return round(math.atan2(point3[1] - point2[1], point3[0] - point2[0]) - math.atan2(point1[1] - point2[1],
                                                                                     point1[0] - point2[0]), 5)

    def minAreaFreeRect(self, points) -> float:
        slope_distance_map = collections.defaultdict(list)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                slope = self.find_slope(points[i], points[j])
                if slope>0:
                    slope_distance_map[self.find_slope(points[i], points[j])].append(
                        (i, j, self.find_distance(points[i], points[j])))
                else:
                    slope_distance_map[self.find_slope(points[j], points[i])].append(
                        (j, i, self.find_distance(points[j], points[i])))

        min_area = float('inf')
        for slope in slope_distance_map:
            similar_slope_points = slope_distance_map[slope]
            for i in range(len(similar_slope_points)):
                for j in range(i + 1, len(similar_slope_points)):
                    if similar_slope_points[i][2] == similar_slope_points[j][2]:
                        point1 = points[similar_slope_points[i][0]]
                        point2 = points[similar_slope_points[i][1]]
                        point3 = points[similar_slope_points[j][0]]
                        point4 = points[similar_slope_points[j][1]]
                        distance = -1
                        if self.find_angle(point2, point1, point3) == round(math.pi / 2, 5) or self.find_angle(point2, point1,
                                                                                                     point3) == -round(math.pi / 2, 5):
                            distance = self.find_distance(point1, point3)
                        if self.find_angle(point1, point2, point4) == round(math.pi / 2, 5) or self.find_angle(point1, point2,
                                                                                                     point4) == -round(math.pi / 2, 5):
                            distance = self.find_distance(point2, point4)
                        if distance != -1:
                            area = distance * similar_slope_points[i][2]
                            min_area = min(area, min_area)
        return 0 if min_area == float('inf') else round(min_area, 5)


if __name__ == '__main__':
    print(Solution().minAreaFreeRect([[55,46],[38,58],[15,61],[75,15],[17,37],[115,55],[62,34],[49,30],[51,119],[9,45],[11,79],[41,13]]))
    print(Solution().minAreaFreeRect([[7,3],[8,12],[13,5],[6,2],[8,0],[12,8],[14,2],[2,6]]))
    print(Solution().minAreaFreeRect([[24420,16685],[20235,25520],[14540,20845],[20525,14500],[16876,24557],[24085,23720],[25427,18964],[21036,14573],[24420,23315],[22805,24760],[21547,25304],[16139,23952],[21360,14645],[24715,17120],[19765,25520],[19388,25491],[22340,25005],[25520,19765],[25365,21320],[23124,15443],[20845,14540],[24301,16532],[16685,24420],[25100,17875],[22125,25100],[15699,23468],[14592,21131],[25460,19155],[17837,25084],[23468,24301],[25460,20845],[18453,25304],[21131,14592],[22805,15240],[19475,25500],[15443,23124],[25355,21360],[15285,22880],[20000,25525],[24085,16280],[22163,25084],[22880,15285],[14916,22163],[16280,24085],[24875,17400],[22600,24875],[14573,21036],[25427,21036],[17120,24715],[25500,19475]]))
    print(Solution().minAreaFreeRect([[29100,31115],[29672,9379],[32675,13240],[18635,34300],[32259,27488],[20000,5635],[26084,33013],[34196,17803],[28619,31492],[12512,32259],[25525,33260],[33760,15875],[33949,23432],[31556,28533],[5788,22091],[6240,24125],[24240,33725],[31556,11467],[6275,24240],[13240,32675],[8373,28436],[28436,31627],[30115,30200],[21972,5771],[27488,32259],[21972,34229],[34229,18028],[24240,6275],[26084,6987],[5635,20000],[29100,8885],[15760,33725],[22091,5788],[11564,31627],[32376,27293],[33524,15157],[5771,21972],[7741,27488],[21365,5700],[10900,31115],[11467,31556],[33013,26084],[30200,30115],[11381,31492],[26760,7325],[9885,30200],[24956,33483],[12707,32376],[31492,28619],[26760,32675]]))
