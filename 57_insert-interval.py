import bisect


class Solution:

    """
    Attempt: Fired
    Accepted: 76%
    """
    def insert(self, intervals, newInterval):
        a = []
        for i in range(len(intervals)):
            a.append(intervals[i][0])
            a.append(intervals[i][1])

        start_index = bisect.bisect_left(a, newInterval[0])
        start_index = start_index - 1 if start_index % 2 == 1 else start_index
        end_index = bisect.bisect_right(a, newInterval[1])
        end_index = end_index + 1 if end_index % 2 == 1 else end_index

        a = a[:start_index] + [min(newInterval[0], a[start_index] if 0 <= start_index < len(a) else float('inf')), max(newInterval[1], a[end_index - 1] if 0 <= end_index < len(a) else -float('inf'))] + a[end_index:]
        ans = []
        for i in range(0, len(a), 2):
            ans.append([a[i], a[i + 1]])

        return ans

    """
    Attempt: Fired
    This is the exact same solution, just in a different form.
    Accepted: 26%
    """
    def insert(self, intervals, newInterval):
        a = []
        for i in range(len(intervals)):
            a.append(intervals[i][0])
            a.append(intervals[i][1])

        start_index = bisect.bisect_left(a, newInterval[0])
        end_index = bisect.bisect_right(a, newInterval[1])
        s = []
        """
        This is a crucial combination which needs to be remembered. I understand this but this became a little difficult to make on the spot.
        """
        if start_index % 2 == 0:
            s.append(newInterval[0])
        if end_index % 2 == 0:
            s.append(newInterval[1])

        a[start_index:end_index] = s
        ans = []
        for i in range(0, len(a), 2):
            ans.append([a[i], a[i + 1]])

        return ans


if __name__ == '__main__':
    print(Solution().insert(intervals = [[1,3],[6,9]], newInterval = [2,5]))
    print(Solution().insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))
    print(Solution().insert([], [5,7]))
    print(Solution().insert([[1,5]], [6,8]))
    print(Solution().insert([[1,5]], [2,3]))
