import bisect
import heapq

class Solution:
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort()

        merged = []
        lo, hi = intervals[0][0], intervals[0][1]
        for start, end in intervals:
            if start > hi:
                merged.append([lo, hi])
                lo, hi = start, end
            else:
                hi = max(hi, end)
        merged.append([lo, hi])

        return merged

    """
    Revision 2:
    Another similar implementation of the above code. Simpler to understand. 
    """
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort()

        merged = []
        for start, end in intervals:
            if merged and merged[-1][1] >= start:
                # overlap
                merged[-1][1] = max(end, merged[-1][1])
            else:
                # no overlap, simply append
                merged.append([start, end])

        return merged

    """
    Revision 2: This is a brilliant question. I have recently learnt of another technique to solve this question.
    But the sorting technique is by far the most brilliant way to solve this question.
    The algo above and the algo below have similar time complexity.
    Even though we use nlog(n) for sorting at first. We use log(n) n times in the second.
    """
    def merge(self, intervals):
        merged = []

        for lo, hi in intervals:
            start = bisect.bisect_left(merged, lo)
            end = bisect.bisect_right(merged, hi)

            sub_merged = []
            if start % 2 == 0:
                sub_merged.append(lo)
            if end % 2 == 0:
                sub_merged.append(hi)

            merged[start:end] = sub_merged

        out = []
        for i in range(0, len(merged), 2):
            out.append([merged[i], merged[i + 1]])

        return out

    def merge(self, intervals):
        a = list(heapq.merge(*intervals))
        print(a)

    # # Accepted : 5%
    # def merge(self, intervals):
    #     merged = SortedList()
    #
    #     def merge_interval(start, end):
    #         index = merged.bisect_left([start, end])
    #         index = index - 1 if index and start <= merged[index - 1][1] else index
    #
    #         to_del = set()
    #         start_val = start
    #         end_val = end
    #         for i in range(index, len(merged)):
    #             if start <= end < merged[i][0] <= merged[i][1] or merged[i][0] <= merged[i][1] < start <= end:
    #                 break
    #             start_val = min(start_val, merged[i][0])
    #             end_val = max(end_val, merged[i][1])
    #             to_del.add(tuple(merged[i]))
    #
    #         for d in to_del:
    #             merged.remove(list(d))
    #
    #         merged.add([start_val, end_val])
    #
    #     for start, end in intervals:
    #         merge_interval(start, end)
    #
    #     return merged

    """
    Attempt: Fired
    Accepted: 78%
    """
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])

        ans = []
        start, end = intervals[0][0], intervals[0][1]
        for s, e in intervals:
            if s > end:
                ans.append([start, end])
                start, end = s, e
                continue
            end = max(end, e)
        ans.append([start, end])

        return ans





if __name__ == '__main__':
    print(Solution().merge(intervals = [[1,3],[2,6],[15,18],[8,10]]))
    print(Solution().merge(intervals = [[1,4],[4,6]]))
    print(Solution().merge([[1,4],[2,3]]))
    print(Solution().merge([[1,4],[0,0]]))
    print(Solution().merge([[2,3],[5,5],[2,2],[3,4],[3,4]]))
    print(Solution().merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))
