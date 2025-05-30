import heapq
from collections import deque

class Solution:
    """
    Revision 2:
    This was a good question and I had to think about it. I could not figure out the optimised solution. My first solution TLEed.
    My initial idea was to use sliding window to maintain <=k distance and find the max using iteration.
    What I didn't think of was that there is a faster way of finding the max. I could not figure out that there is way to split the equation in order to simplify the question in which we could reduce this to finding the max.
    Once you know that splitting the equation can lead to simplification, finding the max can be done by using priority queue.
    But that disrupt keeping the window. That we can do by popping >k before computing the max.
    How then do we push to the queue. We take into consideration indexes less than the current index only. So we keep adding the current index for the consideration of the future events.
    Since the whole array is ordered by x if we pop an element from the queue once it also becomes redundant for future use i.e. if x[1] - x[0] > k then x[2] - x[0] has to be more than k.
    """
    def findMaxValueOfEquation(self, points, k: int) -> int:
        queue = []

        score = -float('inf')
        for index, (x, y) in enumerate(points):
            while queue and x - queue[0][1][0] > k:
                heapq.heappop(queue)

            if queue:
                score2, (xj, yj), index2 = queue[0]
                score = max(score, yj - xj + y + x)
            heapq.heappush(queue, (-(y - x), [x, y], index))

        return score

    """
    Revision 2:
    This is a question which is similar to 239_sliding-window-maximum.
    This implementation is derived from similar principles. The idea behind this is that we use a queue to keep track of maximum yi-xi for all i < index
    There is no need for any value to exist below the max available to compare because its the max till that index. So we can remove these values monotonically at the time of insertion of the index.
    There is also no need for those indexes which are at a distance more than k from the x of index, so we need to remove those first.
    Append the index for the next iterations.
    
    Another question similar to this is 1438_longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit
    """
    def findMaxValueOfEquation(self, points, k: int) -> int:
        queue = deque()

        score = -float('inf')
        for index, (x, y) in enumerate(points):
            while queue and x - points[queue[0]][0] > k:
                queue.popleft()

            if queue:
                xj, yj = points[queue[0]]
                score = max(score, yj - xj + y + x)

            while queue and (points[queue[-1]][1] - points[queue[-1]][0]) < y - x:
                queue.pop()
            queue.append(index)
        return score


    # # Accepted
    # def findMaxValueOfEquation(self, points, k: int) -> int:
    #     ptrl, ptrc, ptrr = 0, 0, 0
    #
    #     max_value = -float("inf")
    #
    #     while ptrc < len(points):
    #         while ptrr + 1 < len(points) and abs(points[ptrr + 1][0] - points[ptrc][0]) <= k:
    #             ptrr += 1
    #
    #         max_value_index = ptrc
    #         for j in range(ptrl, ptrr + 1):
    #             if j == ptrc:
    #                 continue
    #             value = points[j][1] + points[ptrc][1] + abs(points[j][0] - points[ptrc][0])
    #             if value >= max_value:
    #                 max_value = value
    #                 max_value_index = j
    #
    #         ptrl = ptrc + 1
    #         ptrc = max_value_index if max_value_index > ptrc else ptrc + 1
    #
    #     return max_value

    def findMaxValueOfEquation(self, points, k: int) -> int:
        queue = [(-(points[0][1] - points[0][0]), 0)]

        ans = float('-inf')
        for i in range(1, len(points)):
            while queue and points[i][0] - points[queue[0][1]][0] > k:
                heapq.heappop(queue)
            if queue:
                ans = max(ans, points[i][1] + points[i][0] - queue[0][0])
            heapq.heappush(queue, (-(points[i][1] - points[i][0]), i))

        return ans


    def findMaxValueOfEquation(self, points, k: int) -> int:
        points.sort()




if __name__ == '__main__':
    print(Solution().findMaxValueOfEquation([[-17,-6],[-4,0],[-2,-16],[-1,2],[0,11],[6,18]], 13))
    print(Solution().findMaxValueOfEquation([[-17,5],[-10,-8],[-5,-13],[-2,7],[8,-14]], 4))
    print(Solution().findMaxValueOfEquation([[-19,-12],[-13,-18],[-12,18],[-11,-8],[-8,2],[-7,12],[-5,16],[-3,9],[1,-7],[5,-4],[6,-20],[10,4],[16,4],[19,-9],[20,19]], 6))
    print(Solution().findMaxValueOfEquation([[1,3],[2,0],[5,10],[6,-10]], k = 1))
    print(Solution().findMaxValueOfEquation(points = [[0,0],[3,0],[9,2]], k = 3))
