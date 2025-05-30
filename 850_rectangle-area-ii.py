import collections


class Solution:
    def rectangleArea(self, rectangles) -> int:
        rectangles.sort()
        sorted_rectangle = collections.defaultdict(set)

        for rectangle in rectangles:
            for x in [rectangle[0], rectangle[2]]:
                if x not in sorted_rectangle:
                    sorted_rectangle[x] = set()
                for index, (x1, y1, x2, y2) in enumerate(rectangles):
                    if x < x1:
                        break
                    if x1 <= x < x2:
                        sorted_rectangle[x].add((x1, y1, x2, y2))

        def get_y_overlap(coordinates):
            if not coordinates:
                return []
            coordinates.sort(key=lambda x: (x[1], x[3]))
            merged = [coordinates[0]]
            for i in range(1, len(coordinates)):
                if merged[-1][3] <= coordinates[i][1]:
                    merged.append(coordinates[i])
                else:
                    merged[-1] = (merged[-1][0], min(merged[-1][1], coordinates[i][1]), merged[-1][2],
                                  max(merged[-1][3], coordinates[i][3]))
            return merged

        xs = sorted(sorted_rectangle.keys())
        ptr = 0
        area = 0
        while ptr < len(xs) - 1:
            x = xs[ptr]
            rectangles_for_x = sorted_rectangle[x]
            if rectangles_for_x:
                for x1, y1, x2, y2 in get_y_overlap(list(rectangles_for_x)):
                    area += (xs[ptr + 1] - xs[ptr]) * (y2 - y1)
            ptr += 1

        return area % (pow(10, 9) + 7)


if __name__ == '__main__':
    print(Solution().rectangleArea(rectangles=[[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]))
    print(Solution().rectangleArea(rectangles=[[0, 0, 1000000000, 1000000000]]))
    print(Solution().rectangleArea([[0,0,1,1],[2,2,3,3]]))
    print(Solution().rectangleArea([[25, 20, 70, 27], [68, 80, 79, 100], [37, 41, 66, 76]]))
