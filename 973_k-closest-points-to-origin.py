class Solution:
    def kClosest(self, points, k: int):
        return sorted(points, key=lambda x: pow(x[0] * x[0] + x[1] * x[1], 0.5))[0:k]


if __name__ == '__main__':
    print(Solution().kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2))
