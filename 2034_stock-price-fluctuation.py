from sortedcontainers import SortedDict
from heapq import heappush, heappop

class StockPrice:
    def __init__(self):
        self.latest_time = 0
        # Store price of each stock at each timestamp.
        self.timestamp_price_map = {}

        # Store stock prices in sorted order to get min and max price.
        self.max_heap = []
        self.min_heap = []

    def update(self, timestamp: int, price: int) -> None:
        # Update latestTime to latest timestamp.
        self.timestamp_price_map[timestamp] = price
        self.latest_time = max(self.latest_time, timestamp)

        # Add latest price for timestamp.
        heappush(self.min_heap, (price, timestamp))
        heappush(self.max_heap, (-price, timestamp))

    def current(self) -> int:
        # Return latest price of the stock.
        return self.timestamp_price_map[self.latest_time]

    def maximum(self) -> int:
        price, timestamp = self.max_heap[0]

        # This step is shear genius
        # Since we only add the new entries, duplicates also get added to the mix. It's impossible to remove them from the heap in O(1), so we need to tackle them in here.
        # This not only tackles and returns the maximum but removes all those values which would have come for the same time which were greater than the latest value.
        # Pop pairs from heap with the price doesn't match with hashmap.
        while -price != self.timestamp_price_map[timestamp]:
            heappop(self.max_heap)
            price, timestamp = self.max_heap[0]

        return -price

    def minimum(self) -> int:
        price, timestamp = self.min_heap[0]

        """
        Revision 2:
        This is fairly simple logic and nothing to be afraid of. The thing is that since there are a lot of updates and with no way to remove those old entries from the heaps, they remain.
        It would never be a bother it those entries are never the ones which are minimum or maximum.
        However if they are minimum or maximum, we don't want them. How then do you identify them?
        Their price and timestamp will not match the ones in the stock price map.
        """
        # Pop pairs from heap with the price doesn't match with hashmap.
        while price != self.timestamp_price_map[timestamp]:
            heappop(self.min_heap)
            price, timestamp = self.min_heap[0]

        return price

    # def __init__(self):
    #     self.stock = {}
    #     self.latestTimestamp = 0
    #     self.sortedMap = SortedDict()
    #
    # def update(self, timestamp: int, price: int) -> None:
    #     self.latestTimestamp = max(self.latestTimestamp, timestamp)
    #     if timestamp in self.stock.keys():
    #         oldPrice = self.stock[timestamp]
    #         self.stock[timestamp] = price
    #
    #         if self.sortedMap[oldPrice] > 1:
    #             self.sortedMap[oldPrice] -= 1
    #         else:
    #             del self.sortedMap[oldPrice]
    #
    #     self.stock[timestamp] = price
    #     if price in self.sortedMap:
    #         self.sortedMap[price] += 1
    #     else:
    #         self.sortedMap[price] = 1
    #
    # def current(self) -> int:
    #     return self.stock[self.latestTimestamp]
    #
    # def maximum(self) -> int:
    #     return self.sortedMap.peekitem(- 1)[0]
    #
    # def minimum(self) -> int:
    #     return self.sortedMap.peekitem(0)[0]


if __name__ == '__main__':
    s = StockPrice()
    s.update(1, 10)
    s.update(2, 5)
    print(s.current())
    print(s.maximum())
    s.update(1, 3)
    print(s.maximum())
    s.update(4, 2)
    print(s.minimum())

    a = []
    heappush(a, 15)
    heappush(a, 1)
    heappush(a, 7)
    heappush(a, 2)
    heappush(a, 10)
    heappop(a)
    print(a)
    # a = SortedDict()
    # a[2] = 10
    # a[1] = 12
    # a[3] = 2
    #
    # print(a)

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
