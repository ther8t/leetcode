class Solution:
    def removeInterval(self, intervals, toBeRemoved):
        remove_start, remove_end = toBeRemoved

        new_interval = []
        for index, (start, end) in enumerate(intervals):
            if start >= remove_end:
                new_interval += intervals[index:]
                break
            if end <= remove_start:
                new_interval.append(intervals[index])
                continue
            # There is an overall
            merged = [min(start, remove_start), max(remove_end, end)]
            if remove_start - merged[0] > 0:
                new_interval.append([merged[0], remove_start])
            if remove_end - merged[1]:
                new_interval.append([remove_end, merged[1]])

        return new_interval

    """
    Attempt: Fired
    Accepted: 75%
    """
    def removeInterval(self, intervals, toBeRemoved):
        remove_start, remove_end = toBeRemoved
        ans = []

        for index, (start, end) in enumerate(intervals):
            if end < remove_start:
                ans.append([start, end])
                continue
            if start > remove_end:
                ans += intervals[index:]
                break
            merged = (min(remove_start, start), max(end, remove_end))
            if merged[0] < remove_start:
                ans.append([merged[0], remove_start])
            if remove_end < merged[1]:
                ans.append([remove_end, merged[1]])

        return ans


if __name__ == '__main__':
    print(Solution().removeInterval(intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]))
    print(Solution().removeInterval(intervals = [[0,5]], toBeRemoved = [2,3]))
    print(Solution().removeInterval(intervals = [[-5,-4],[-3,-2],[1,2],[3,5],[8,9]], toBeRemoved = [-1,4]))
    print(Solution().removeInterval(intervals = [[0,5]], toBeRemoved = [2,3]))
