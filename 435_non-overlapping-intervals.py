import bisect
import functools


class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        a = [[-50000, 50000]]

        for s, e in intervals:
            start_index = bisect.bisect_left(a, [s, e])
            i = max(0, start_index - 1)

            temp = []
            while i < len(a) and e < a[i][0]:
                cs, ce = a[i]
                if cs <= s < e <= ce or s <= cs < ce <= e or cs <= s < ce <= e or s <= cs < e <= ce:
                    temp.append([max(cs, s), min(ce, e)])
                else:
                    temp.append(a[i])
                i += 1
            a = a[:start_index] + (temp if len(temp) else [[s, e]]) + a[i:]

        return len(intervals) - len(a)

    def eraseOverlapIntervals(self, intervals) -> int:
        intervals.sort()

        @functools.lru_cache(None)
        def dfs(index):
            if index == len(intervals):
                return 0
            first_non_overlapping_interval = len(intervals)
            for i in range(index + 1, len(intervals)):
                if intervals[index][1] <= intervals[i][0]:
                    first_non_overlapping_interval = i
                    break

            return max(dfs(first_non_overlapping_interval) + 1, dfs(index + 1))

        return len(intervals) - dfs(0)

    """
    This is the most ****** up solution. I still don't have the intuition for why this problem is a greedy solution.
    The idea behind this is to obviously sort this. And then select the minimum y when conflict arises. So for [1, 2] and [1, 3] we select 2 and the overlapping one is then rejected.
    """
    def eraseOverlapIntervals(self, intervals) -> int:
        intervals.sort()

        min_y = float('inf')
        ans = 0

        for x, y in intervals:
            if x < min_y:
                ans += 1
                min_y = min(min_y, y)
            else:
                min_y = y

        return ans - 1


if __name__ == '__main__':
    print(Solution().eraseOverlapIntervals(intervals = [[1,2],[2,3],[3,4],[1,3]]))
    print(Solution().eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
    print(Solution().eraseOverlapIntervals(intervals = [[1,2],[2,3]]))
