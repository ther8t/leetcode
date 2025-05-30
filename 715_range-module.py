from bisect import bisect_left as bl, bisect_right as br

class RangeModule:

    def __init__(self):
        self._X = []


    """
    Revision 2:
    There is a sort of similar question dealing with merging intervals which is 56_merge-intervals.
    The difference is between how we receive intervals. In that question we have all the intervals at out disposal in one go.
    We could simply sort them and then merge them.
    In this case we need to find the position of if the current element in the already sorted and merged list and then remerge it.
    Both are equally time complex and a must learn.
    """

    def addRange(self, left: int, right: int) -> None:
        # Main Logic
        #   If idx(left) or idx(right) is odd, it's in a interval. So don't add it.
        #   If idx(left) or idx(right) is even, it's not in any interval. So add it as new interval
        #   Slice array[idx(left) : idx(right)]
        #       1) both odd: Nothing is added. Merge all middle intervals.
        #       2) both even: Add new intervals. Merge all middle intervals
        #       3) idx(left) is even: update start point of next interval with left
        #       4) idx(right) is even: update end point of previous interval with right
        # Bisect_left vs. Bisect_right
        #   left need to proceed all interval closing at left, so use Bisect_left
        #   right need to go after all interval openning at right, so use Bisect_right

        # i, j = bl(self._X, left), br(self._X, right)
        # self._X[i: j] = [left] * (i % 2 == 0) + [right] * (j % 2 == 0)
        start = bl(self._X, left)
        end = br(self._X, right)
        subtrack = []
        if start % 2 == 0:
            subtrack.append(left)
        if end % 2 == 0:
            subtrack.append(right)
        self._X[start:end] = subtrack

    def queryRange(self, left: int, right: int) -> bool:
        # Main logic
        #   If idx of left/right is odd, it's in a interval. Else it's not.
        #   If idx of left&right is the same, they're in the same interval
        # Bisect_left vs. Bisect_right
        #   [start, end). Start is included. End is not.
        #   so use bisect_right for left
        #   so use bisect_left for right
        i, j = br(self._X, left), bl(self._X, right)
        return i == j and i % 2 == 1

    def removeRange(self, left: int, right: int) -> None:
        # Main Logic
        #   If idx(left) is odd, the interval that contains left need to change end point to left
        #   If idx(right) is odd, the interval that contains right need to change start point to right
        #   Else, everything from idx(left) to idx(right) is removed. Nothing is changed.
        # Bisect_left vs. Bisect_right
        #   Same as addRange

        # i, j = bl(self._X, left), br(self._X, right)
        # self._X[i: j] = [left] * (i % 2 == 1) + [right] * (j % 2 == 1)

        start = bl(self._X, left)
        end = br(self._X, right)
        subtrack = []
        if start % 2 == 1:
            subtrack.append(left)
        if end % 2 == 1:
            subtrack.append(right)
        self._X[start:end] = subtrack

    # # ACCEPTED
    # def __init__(self):
    #     self.range = []
    #
    # def absolute_overlap(self, left, right, interval):
    #     return (left <= interval[0] and interval[1] <= right) or (interval[0] <= left and right <= interval[1])
    #
    # def partial_overlap(self, left, right, interval):
    #     return (left < interval[0] <= right < interval[1]) or (interval[0] < left <= interval[1] < right)
    #
    # def addRange(self, left: int, right: int) -> None:
    #     overlap = []
    #     overlap_range_min = left
    #     overlap_range_max = right
    #     for interval in self.range:
    #         if interval[0] > right:
    #             break
    #         if self.absolute_overlap(left, right, interval) or self.partial_overlap(left, right, interval):
    #             overlap_range_min = min(overlap_range_min, interval[0])
    #             overlap_range_max = max(overlap_range_max, interval[1])
    #             overlap.append(interval)
    #
    #     for i in overlap:
    #         self.range.remove(i)
    #
    #     # insert the new value
    #     self.range.append([overlap_range_min, overlap_range_max])
    #
    #     # bubble down
    #     for i in range(len(self.range) - 1, - 1, -1):
    #         if i - 1 >= 0 and self.range[i - 1][0] > self.range[i][0]:
    #             temp = self.range[i - 1]
    #             self.range[i - 1] = self.range[i]
    #             self.range[i] = temp
    #         else:
    #             break
    #
    # def queryRange(self, left: int, right: int) -> bool:
    #     for interval in self.range:
    #         if interval[0] > right:
    #             break
    #         if interval[0] <= left and right <= interval[1]:
    #             return True
    #     return False
    #
    # def removeRange(self, left: int, right: int) -> None:
    #     overlap = []
    #     remainder = []
    #     overlap_range_min = left
    #     overlap_range_max = right
    #     for interval in self.range:
    #         if interval[0] > right:
    #             break
    #         if self.absolute_overlap(left, right, interval) or self.partial_overlap(left, right, interval):
    #             overlap_range_min = min(overlap_range_min, interval[0])
    #             overlap_range_max = max(overlap_range_max, interval[1])
    #             overlap.append(interval)
    #
    #         if self.partial_overlap(left, right, interval):
    #             if left < interval[0] and right != interval[1]:
    #                 remainder.append([right, interval[1]])
    #             if right > interval[1] and interval[0] != left:
    #                 remainder.append([interval[0], left])
    #
    #         if self.absolute_overlap(left, right, interval) and (interval[0] <= left and right <= interval[1]):
    #             if interval[0] != left:
    #                 remainder.append([interval[0], left])
    #             if right != interval[1]:
    #                 remainder.append([right, interval[1]])
    #
    #     for i in overlap:
    #         self.range.remove(i)
    #
    #     # insert and bubble down.
    #     for interval in remainder:
    #         self.range.append(interval)
    #         for i in range(len(self.range) - 1, - 1, -1):
    #             if i - 1 >= 0 and self.range[i - 1][0] > self.range[i][0]:
    #                 temp = self.range[i - 1]
    #                 self.range[i - 1] = self.range[i]
    #                 self.range[i] = temp
    #             else:
    #                 break


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)

if __name__ == '__main__':
    obj = RangeModule()
    obj.addRange(5, 8)
    obj.addRange(4, 7)
    obj.removeRange(7, 8)
    obj.removeRange(8, 9)
    obj.addRange(8, 9)
    obj.removeRange(1, 3)
    obj.addRange(1, 8)
    print(obj.queryRange(2, 4))
    print(obj.queryRange(2, 9))
    print(obj.queryRange(4, 6))

    # obj.addRange(10, 20)
    # obj.removeRange(14,16)
    # print(obj.queryRange(10, 14))
    # print(obj.queryRange(13, 15))
    # print(obj.queryRange(16, 17))
