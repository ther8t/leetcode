from queue import PriorityQueue
import heapq


class Solution:
    def getOrder(self, tasks):
        ptr2, R = 0, pow(10, 9)

        indexedTasks = []
        for index, val in enumerate(tasks):
            indexedTasks.append((index, val))

        def sortFunc(node):
            return node[1][0]

        orderArray = []
        sortedTasks = sorted(indexedTasks, key=sortFunc)
        initialTime = 0
        heap = []

        while ptr2 < len(sortedTasks) or len(heap) > 0:
            if len(heap) == 0 and initialTime < sortedTasks[ptr2][1][0]:
                initialTime = sortedTasks[ptr2][1][0]
            while ptr2 < len(sortedTasks) and sortedTasks[ptr2][1][0] <= initialTime:
                heapq.heappush(heap, (sortedTasks[ptr2][1][1] * R + sortedTasks[ptr2][0], sortedTasks[ptr2]))
                ptr2 += 1

            apnaTimeAaGaya = heapq.heappop(heap)
            orderArray.append(apnaTimeAaGaya[1][0])

            initialTime = initialTime + apnaTimeAaGaya[1][1][1]
        return orderArray

    # # Accepted
    # def getOrder(self, tasks):
    #     ptr2, R = 0, pow(10, 9)
    #
    #     indexedTasks = []
    #     for index, val in enumerate(tasks):
    #         indexedTasks.append((index, val))
    #
    #     def sortFunc(node):
    #         return node[1][0]
    #
    #     orderArray = []
    #     sortedTasks = sorted(indexedTasks, key=sortFunc)
    #     initialTime = 0
    #     q = PriorityQueue()
    #
    #     while ptr2 < len(sortedTasks) or q.qsize() > 0:
    #         if q.qsize() == 0 and initialTime < sortedTasks[ptr2][1][0]:
    #             initialTime = sortedTasks[ptr2][1][0]
    #         while ptr2 < len(sortedTasks) and sortedTasks[ptr2][1][0] <= initialTime:
    #             q.put((sortedTasks[ptr2][1][1] * R + sortedTasks[ptr2][0], sortedTasks[ptr2]))
    #             ptr2 += 1
    #
    #         apnaTimeAaGaya = q.get()
    #         orderArray.append(apnaTimeAaGaya[1][0])
    #
    #         initialTime = initialTime + apnaTimeAaGaya[1][1][1]
    #     return orderArray


if __name__ == '__main__':
    print(Solution().getOrder(tasks=[[7, 1], [6, 3], [1, 3]]))
    print(Solution().getOrder(
        tasks=[[35, 36], [11, 7], [15, 47], [34, 2], [47, 19], [16, 14], [19, 8], [7, 34], [38, 15], [16, 18], [27, 22],
               [7, 15], [43, 2], [10, 5], [5, 4], [3, 11]]))
