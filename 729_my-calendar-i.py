import sortedcontainers


class MyCalendar:
    def __init__(self):
        self.calendar = sortedcontainers.SortedList()

    def book(self, start: int, end: int) -> bool:
        index = self.calendar.bisect_left((start, end))
        if (index > 0 and start < self.calendar[index - 1][1]) or (
                index < len(self.calendar) and end > self.calendar[index][0]):
            return False
        self.calendar.add((start, end))
        return True

    # # Accepted : Using LinkedList
    # class LinkedList:
    #     def __init__(self, start, end, next_node=None):
    #         self.start = start
    #         self.end = end
    #         self.next_node = next_node
    #
    # def __init__(self):
    #     self.calendar = None
    #
    # def book(self, start: int, end: int) -> bool:
    #     iterator = self.calendar
    #     if not self.calendar:
    #         self.calendar = self.LinkedList(start, end, None)
    #         return True
    #
    #     prev_node = None
    #     while iterator and start >= iterator.end:
    #         prev_node = iterator
    #         iterator = iterator.next_node
    #
    #     if not prev_node:
    #         # compare with iterator and add if possible. This would be added to the start of the node.
    #         if end <= iterator.start:
    #             self.calendar = self.LinkedList(start, end, self.calendar)
    #             return True
    #         else:
    #             return False
    #     if not iterator:
    #         if prev_node.end <= start:
    #             prev_node.next_node = self.LinkedList(start, end, None)
    #             return True
    #         else:
    #             return False
    #     if prev_node.end <= start and end <= iterator.start:
    #         prev_node.next_node = self.LinkedList(start, end, iterator)
    #         return True
    #     else:
    #         return False


# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
print(obj.book(47, 50))
print(obj.book(33, 41))
print(obj.book(39, 45))
print(obj.book(33, 42))
print(obj.book(25, 32))
print(obj.book(26, 35))
print(obj.book(19, 25))
print(obj.book(3, 8))
print(obj.book(8, 13))
print(obj.book(18, 27))
