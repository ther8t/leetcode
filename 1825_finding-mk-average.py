import collections
from sortedcontainers import SortedList


class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.first = SortedList()
        self.second = SortedList()
        self.third = SortedList()
        self.window = collections.deque()
        self.sum = 0

    def addElement(self, num: int) -> None:
        self.window.append(num)
        if len(self.window) > self.m:
            # remove the last_number from the window and the list.
            to_be_removed = self.window.popleft()
            if self.first[0] <= to_be_removed <= self.first[-1]:
                self.first.remove(to_be_removed)
                third_popped = self.third.pop(0)
                self.second.add(third_popped)
                self.sum += third_popped
                second_popped = self.second.pop(0)
                self.sum -= second_popped
                self.first.add(second_popped)
            elif self.second[0] <= to_be_removed <= self.second[-1]:
                self.second.remove(to_be_removed)
                third_popped = self.third.pop(0)
                self.second.add(third_popped)
                self.sum += third_popped
                self.sum -= to_be_removed
            else:
                self.third.remove(to_be_removed)

        # add to the list and balance it the best you can.
        self.first.add(num)
        if len(self.first) > self.k:
            popped = self.first.pop()
            self.second.add(popped)
            self.sum += popped
        if len(self.second) > self.m - 2 * self.k:
            popped_from_second = self.second.pop()
            self.third.add(popped_from_second)
            self.sum -= popped_from_second


    def calculateMKAverage(self) -> int:
        return self.sum // (self.m - 2 * self.k) if len(self.window) == self.m else -1


    # # Wrong Answer 16/17 Can you believe it!!??
    # def __init__(self, m: int, k: int):
    #     self.m = m
    #     self.k = k
    #     self.m_block = SortedList()
    #     self.window = collections.deque()
    #     self.average = None
    #
    # def addElement(self, num: int) -> None:
    #     if len(self.m_block) < self.m:
    #         self.m_block.add(num)
    #         self.window.append(num)
    #         if len(self.m_block) == self.m:
    #             self.average = sum(self.m_block[self.k:-self.k]) / (self.m - 2 * self.k)
    #         return
    #
    #     if self.average is None:
    #         self.average = sum(self.m_block[self.k:-self.k]) / (self.m - 2 * self.k)
    #
    #     # remove the number
    #     popped = self.window.popleft()
    #     popped_index = self.m_block.bisect_left(popped)
    #     if popped_index < self.k:
    #         self.average -= self.m_block[self.k] / (self.m - 2 * self.k)
    #     elif self.k <= popped_index < self.m - self.k:
    #         self.average -= popped / (self.m - 2 * self.k)
    #     else:
    #         self.average -= self.m_block[-self.k - 1] / (self.m - 2 * self.k)
    #     self.m_block.remove(popped)
    #
    #     # add the number
    #     self.window.append(num)
    #     index = self.m_block.bisect_left(num)
    #     self.m_block.add(num)
    #     if index < self.k:
    #         self.average += self.m_block[self.k] / (self.m - 2 * self.k)
    #     elif self.k <= index < self.m - self.k:
    #         self.average += num / (self.m - 2 * self.k)
    #     else:
    #         self.average += self.m_block[-self.k - 1] / (self.m - 2 * self.k)
    #
    # def calculateMKAverage(self) -> int:
    #     return -1 if self.average is None else int(self.average)

# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()


if __name__ == '__main__':
    mk = MKAverage(3, 1)
    mk.addElement(17612)
    mk.addElement(74607)
    print(mk.calculateMKAverage())
    mk.addElement(8272)
    mk.addElement(33433)
    print(mk.calculateMKAverage())
    mk.addElement(15456)
    mk.addElement(64938)
    print(mk.calculateMKAverage())
    mk.addElement(99741)

    mk = MKAverage(3, 1)
    mk.addElement(3)
    mk.addElement(1)
    print(mk.calculateMKAverage())
    mk.addElement(10)
    print(mk.calculateMKAverage())
    mk.addElement(5)
    mk.addElement(5)
    mk.addElement(5)
    print(mk.calculateMKAverage())