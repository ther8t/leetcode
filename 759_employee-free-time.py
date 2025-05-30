# Definition for an Interval.
import heapq


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    """
    Revision 2:
    This question is similar to 56_merge-intervals. There are two ways to merge the intervals before we find the remainder.
    1. We add the non-overlapping intervals into the array and binary search the overlapping ones to find where they must be placed. Then merge them.
    2. Sort the intervals based on their start. Now that we know that start[j] >= start[i] with j > i. We can know if there is an overlap if the end of the last interval of the final array > the start of the next one. In which case we simply update the end of the last interval.
    """
    def employeeFreeTime(self, schedule):
        remaining = []
        free_time = []
        """
        Revision 2:
        * means unpack. In this case it would mean for [[i1, i2, i3], [i4, i5, i6]], * would unpack the array of intervals and arrange all the intervals. BUT
        and this is a big BUT the intervals inside the array must be sorted internally. This merge, NOT sort. In this case they are but it would not be the case in every problem.
        
        The rest of the code is similar to 56_merge-interval. 
        """
        for interval in heapq.merge(*schedule, key=lambda x: (x.start, x.end)):
            if remaining and remaining[-1].end >= interval.start:
                remaining[-1].end = max(remaining[-1].end, interval.end)
            else:
                if remaining:
                    free_time.append(Interval(remaining[-1].end, interval.start))
                remaining.append(interval)
        return free_time


    # # Accepted 5%
    # def employeeFreeTime(self, schedule):
    #     def diff(interval1, interval2):
    #         if interval1.end <= interval2.start or interval2.end <= interval1.start:
    #             return [interval1]
    #
    #         if interval1.start < interval2.start < interval1.end <= interval2.end:
    #             return [Interval(interval1.start, interval2.start)]
    #
    #         if interval2.start <= interval1.start < interval2.end < interval1.end:
    #             return [Interval(interval2.end, interval1.end)]
    #
    #         if interval1.start < interval2.start < interval2.end < interval1.end:
    #             return [Interval(interval1.start, interval2.start), Interval(interval2.end, interval1.end)]
    #
    #         if interval2.start <= interval1.start < interval1.end <= interval2.end:
    #             return []
    #
    #     remaining = [Interval(-float('inf'), float('inf'))]
    #
    #     for employee_schedule in schedule:
    #         for interval in employee_schedule:
    #             temp = []
    #             for remaining_interval in remaining:
    #                 temp += diff(remaining_interval, interval)
    #             remaining = temp
    #
    #     if remaining and remaining[0].start == -float('inf'):
    #         remaining = remaining[1:]
    #
    #     if remaining and remaining[-1].end == float('inf'):
    #         remaining = remaining[:-1]
    #
    #     return remaining


if __name__ == '__main__':
    print(Solution().employeeFreeTime([[Interval(7,24),Interval(29,33),Interval(45,57),Interval(66,69),Interval(94,99)],[Interval(6,24),Interval(43,49),Interval(56,59),Interval(61,75),Interval(80,81)],[Interval(5,16),Interval(18,26),Interval(33,36),Interval(39,57),Interval(65,74)],[Interval(9,16),Interval(27,35),Interval(40,55),Interval(68,71),Interval(78,81)],[Interval(0,25),Interval(29,31),Interval(40,47),Interval(57,87),Interval(91,94)]]))
