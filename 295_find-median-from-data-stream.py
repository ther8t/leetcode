import heapq

from sortedcontainers import SortedList

class MedianFinder:

    # def __init__(self):
    #     self.nums = SortedList()
    #
    # def addNum(self, num: int) -> None:
    #     self.nums.add(num)
    #
    # def findMedian(self) -> float:
    #     n = len(self.nums)
    #     if n % 2 == 0:
    #         return (self.nums[n // 2 - 1] + self.nums[n // 2]) / 2
    #     else:
    #         return self.nums[n // 2]

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)

        """
        Revision 2:
        This here is a genius move. I realised this only because I attempted the question and realised that adding to only a single heap would not solve this.
        Adding to only one heap would not sort the number being added. The number has to be passed from one heap to the other.
        The other thing is that even if you somehow figure out, which you can and I did, which heap to put the number in if we intend to insert the number in only one heap, we have to use two loops to balance.
        What I really mean is that if the new number was added to max_heap we need to check if max_heap > min_heap and vice versa, which changes the loop.
        """
        popped = heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, -popped)

        # balance the heaps.
        while len(self.min_heap) > len(self.max_heap):
            popped = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -popped)

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            n1, n2 = -self.max_heap[0], self.min_heap[0]
            return (n1 + n2) / 2
        else:
            return -self.max_heap[0]


if __name__ == '__main__':
    # Your MedianFinder object will be instantiated and called as such:
    obj = MedianFinder()
    obj.addNum(1)
    print(obj.findMedian())
    obj.addNum(2)
    print(obj.findMedian())
    obj.addNum(3)
    print(obj.findMedian())
    obj.addNum(4)
    print(obj.findMedian())
    obj.addNum(5)
    print(obj.findMedian())
