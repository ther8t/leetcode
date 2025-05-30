import collections


class DetectSquares:

    """
    Revision 2:
    This is a good question. The idea is fairly simple but the catch is that there maybe duplicate coordinates. And since there are duplicates so for four points and 4 duplicates 1*2*3*4 would be the total count.
    I had the same idea about keeping x cooridinates and coordinates mapped and find the points from there on. The problem gets complicated specially because of the duplicate coordinates. I forgot about it completely.
    """
    def __init__(self):
        self.coordinates = collections.defaultdict(int)
        self.xOrderedCoordinates = collections.defaultdict(list)

    def add(self, point) -> None:
        self.coordinates[(point[0], point[1])] += 1
        self.xOrderedCoordinates[point[0]].append((point[0], point[1]))

    def count(self, point) -> int:
        distances = set()
        for i in self.xOrderedCoordinates[point[0]]:
            if i[0] == point[0] and i[1]!=point[1]:
                distances.add(i[1] - point[1])

        x = point[0]
        y = point[1]
        count = 0
        for d in distances:
            if (x - d, y) in self.coordinates and (x - d, y + d) in self.coordinates:
                val1 = self.coordinates[(x - d, y)]
                val2 = self.coordinates[(x - d, y + d)]
                val3 = self.coordinates[(x, y + d)]
                val4 = self.coordinates[(x, y)] if (x, y) in self.coordinates else 1
                count += (val1*val2*val3)

            if (x + d, y) in self.coordinates and (x + d, y + d) in self.coordinates:
                val1 = self.coordinates[(x + d, y)]
                val2 = self.coordinates[(x + d, y + d)]
                val3 = self.coordinates[(x, y + d)]
                val4 = self.coordinates[(x, y)] if (x, y) in self.coordinates else 1
                count += (val1*val2*val3)

        return count


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)

if __name__ == '__main__':
    d = DetectSquares()
    d.add([3, 10])
    d.add([11, 2])
    d.add([3, 2])
    print(d.count([11, 10]))
    print(d.count([14, 8]))
    d.add([11, 2])
    print(d.count([11, 10]))

    # d = DetectSquares()
    # d.add([5, 10])
    # d.add([10, 5])
    # d.add([10, 10])
    # print(d.count([5, 5]))
    # d.add([3, 0])
    # d.add([8, 0])
    # d.add([8, 5])
    # print(d.count([3, 5]))
    # d.add([9, 0])
    # d.add([9, 8])
    # d.add([1, 8])
    # print(d.count([1, 0]))
    # d.add([0, 0])
    # d.add([8, 0])
    # d.add([8, 8])
    # print(d.count([0, 8]))
    # d.add([1, 9])
    # d.add([2, 9])
    # d.add([2, 10])
    # print(d.count([1, 10]))
    # d.add([7, 8])
    # d.add([2, 3])
    # d.add([2, 8])
    # print(d.count([7, 3]))
    # d.add([9, 10])
    # d.add([9, 5])
    # d.add([4, 5])
    # print(d.count([4, 10]))
    # d.add([0, 9])
    # d.add([4, 5])
    # d.add([4, 9])
    # print(d.count([0, 5]))
    # d.add([1, 10])
    # d.add([10, 1])
    # d.add([10, 10])
    # print(d.count([1, 1]))
    # d.add([10, 0])
    # d.add([2, 0])
    # d.add([2, 8])
    # print(d.count([10, 8]))
    # d.add([7, 6])
    # d.add([4, 6])
    # d.add([4, 9])
    # print(d.count([7, 9]))
    # d.add([10, 9])
    # d.add([10, 0])
    # d.add([1, 0])
    # print(d.count([1, 9]))
    # d.add([0, 9])
    # d.add([8, 1])
    # d.add([0, 1])
    # print(d.count([8, 9]))
    # d.add([3, 9])
    # d.add([10, 9])
    # d.add([3, 2])
    # print(d.count([10, 2]))
    # d.add([3, 8])
    # d.add([9, 2])
    # d.add([3, 2])
    # print(d.count([9, 8]))
    # d.add([0, 9])
    # d.add([7, 9])
    # d.add([0, 2])
    # print(d.count([7, 2]))
    # d.add([10, 1])
    # d.add([1, 10])
    # d.add([10, 10])
    # print(d.count([1, 1]))
    # d.add([6, 10])
    # d.add([2, 6])
    # d.add([6, 6])
    # print(d.count([2, 10]))
    # d.add([6, 0])
    # d.add([6, 2])
    # d.add([8, 2])
    # print(d.count([8, 0]))