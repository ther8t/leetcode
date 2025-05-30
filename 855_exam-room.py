import heapq
from sortedcontainers import SortedList


class ExamRoom:

    def allot_seat_distance(self, start, end):
        if start == -1:
            alloted_seat = 0
        elif end == self.n:
            alloted_seat = self.n - 1
        else:
            alloted_seat = (start + end) // 2
        return min(alloted_seat - start, end - alloted_seat)

    def __init__(self, n: int):
        self.n = n
        self.heap = [(-1, -1, n)]
        self.intervals = SortedList()
        self.intervals.add((-1, n))

    def seat(self) -> int:
        distance, start, end = heapq.heappop(self.heap)
        if start == -1:
            alloted_seat = 0
        elif end == self.n:
            alloted_seat = self.n - 1
        else:
            alloted_seat = start + self.allot_seat_distance(start, end)
        heapq.heappush(self.heap, (-self.allot_seat_distance(start, alloted_seat), start, alloted_seat))
        heapq.heappush(self.heap, (-self.allot_seat_distance(alloted_seat, end), alloted_seat, end))
        self.intervals.remove((start, end))
        self.intervals.add((start, alloted_seat))
        self.intervals.add((alloted_seat, end))
        return alloted_seat

    def leave(self, p: int) -> None:
        interval_index = self.intervals.bisect_left((p, p))
        first_interval, second_interval = self.intervals[interval_index - 1], self.intervals[interval_index]
        self.intervals.remove(first_interval)
        self.intervals.remove(second_interval)
        self.intervals.add((first_interval[0], second_interval[1]))
        self.heap.remove((-self.allot_seat_distance(first_interval[0], first_interval[1]), first_interval[0], first_interval[1]))
        self.heap.remove((-self.allot_seat_distance(second_interval[0], second_interval[1]), second_interval[0], second_interval[1]))
        heapq.heapify(self.heap)
        heapq.heappush(self.heap, (-self.allot_seat_distance(first_interval[0], second_interval[1]), first_interval[0], second_interval[1]))


# Your ExamRoom object will be instantiated and called as such:
obj = ExamRoom(8)
print(obj.seat())
print(obj.seat())
print(obj.seat())
print(obj.leave(0))
print(obj.leave(7))
print(obj.seat())
print(obj.seat())
print(obj.seat())
print(obj.seat())
print(obj.seat())
print(obj.seat())
print(obj.seat())
