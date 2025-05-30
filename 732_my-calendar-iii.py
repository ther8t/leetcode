import collections


class MyCalendarThree:

    # def __init__(self):
    #     self.covered_areas = {}
    #     self.max_k = 0
    #
    # def book(self, start: int, end: int) -> int:
    #     k = 1
    #     intersections = {(start, end): 1}
    #     for index, (area_start, area_end) in enumerate(self.covered_areas):
    #         if not area_end <= start and not end <= area_start:
    #             # there is an intersection
    #             intersection_start = max(area_start, start)
    #             intersection_end = min(area_end, end)
    #             intersections[(intersection_start, intersection_end)] = max(self.covered_areas[(area_start, area_end)] + 1, intersections.get((intersection_start, intersection_end), 1))
    #             k = max(k, intersections[(intersection_start, intersection_end)])
    #     for intersection in intersections:
    #         self.covered_areas[intersection] = intersections[intersection]
    #     self.max_k = max(self.max_k, k)
    #     return self.max_k

    # def __init__(self):
    #     self.delta = collections.Counter()
    #
    # # This is not my solution but this is a good implementation. It's like counting brackets and depth value would be the same as the max number of brackets started without closing
    # # ()((())) = 3
    # def book(self, start, end):
    #     self.delta[start] += 1
    #     self.delta[end] -= 1
    #     active = ans = 0
    #     for x in sorted(self.delta):
    #         active += self.delta[x]
    #         if active > ans: ans = active
    #
    #     return ans


    """
    Revision 2:
    This is the implementation which I had not remembered. But I understand it well and it's brilliant.
    This implementation is SLOWER but brilliant none the less.
    I have made some optimisations to it, but some due care needs to be taken.
    1. Ending the loop when the limit crosses beyond end because there would not be any new change.
    2. Because of the previous change, we need to make sure we store the max from previous iterations and update it.

    This is similar to two questions. One was merging pairs of intervals or overlap pairs if interval or something.
    The other one was count the depth of brackets.
    """
    def __init__(self):
        self.delta = collections.Counter()
        self.prev_max = 0

    def book(self, start, end):
        self.delta[start] += 1
        self.delta[end] -= 1

        max_count = self.prev_max
        current_count = 0
        for key in sorted(self.delta):
            if key > end:
                break
            current_count += self.delta[key]
            max_count = max(max_count, current_count)
        self.prev_max = max(max_count, self.prev_max)
        return max_count



# Your MyCalendarThree object will be instantiated and called as such:
obj = MyCalendarThree()
print(obj.book(26,35))
print(obj.book(26,32))
print(obj.book(25,32))
print(obj.book(18,26))
print(obj.book(40,45))
print(obj.book(19,26))
print(obj.book(48,50))
print(obj.book(1,6))
print(obj.book(46,50))
print(obj.book(11,18))

