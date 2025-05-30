import bisect

from sortedcontainers import SortedList


class Solution:

    """
    Revision 2:
    This question is another variation of the 715_range-module. I have that opened in another tab but I didn't need to see it to use it.
    It's a brilliant piece of code to use array to mark and merge ranges.
    The only difference is calculating the effort. Which frankly took more time than merging, which this time was an easy business.
    The problem I faced with overlapping indexes was that there is no fixed pattern with an array like there is with array of intervals which you can see to check if there is an overlap or not.
    The start_index could start with an even index or an odd index. But once the intervals were sorted out. It became easy to check for overlaps.
    """
    def amountPainted(self, paint):
        painted = []
        effort = []

        for start, end in paint:
            start_index = bisect.bisect_left(painted, start)
            end_index = bisect.bisect_right(painted, end)
            overlap = []
            if start_index % 2 == 0:
                overlap.append(start)
            if end_index % 2 == 0:
                overlap.append(end)

            already_painted_length = 0
            # The line below is here because we can't be sure if the starting index would be an even or an odd number and an interval can only start with an even.
            # So in order to check for an overlap we need a complete interval.
            ptr = start_index if start_index % 2 == 0 else start_index - 1
            # Please notice that I have used end_index and not (end_index + 1). Although end_index should be included in the loop.
            # It is however included in the previous iteration of the loop if it is required which means that the end_index must have been an odd number.
            # or if it an even number then that means that we don't need that end_index because there is a partial overlap at the end and end_index is a newly created entry.
            for i in range(ptr, end_index, 2):
                if i < len(painted) and not (painted[i + 1] < start or end < painted[i]):
                    already_painted_length += min(painted[i + 1], end) - max(start, painted[i])
                else:
                    already_painted_length += 0

            painted[start_index:end_index] = overlap
            effort.append(end - start - already_painted_length)

        return effort




    # def amountPainted(self, paint):
    #     painted = []
    #     worklog = []
    #     for index, (toPaintStart, toPaintEnd) in enumerate(paint):
    #         print(index, toPaintStart, toPaintEnd)
    #         # search for index in painted where paint's start < painted end and other index where paint end < painted start
    #         overlapStart = toPaintStart
    #         overlapEnd = toPaintEnd
    #         workAlreadyDone = 0
    #         overlap = False
    #         toRemove = []
    #         for paintedIndex, (paintedStart, paintedEnd) in enumerate(painted):
    #             if (toPaintStart >= paintedStart and toPaintStart <= paintedEnd and toPaintStart <= paintedEnd) or (
    #                     toPaintStart <= paintedStart and toPaintEnd >= paintedEnd) or (
    #                     toPaintStart <= paintedStart and toPaintEnd <= paintedEnd and toPaintEnd >= paintedStart):
    #                 overlap = True
    #             else:
    #                 if overlap:
    #                     break
    #             if overlap:
    #                 overlapStart = min(overlapStart, paintedStart)
    #                 overlapEnd = max(overlapEnd, paintedEnd)
    #                 workAlreadyDone += (paintedEnd - paintedStart)
    #                 toRemove.append(painted[paintedIndex])
    #
    #         for i in toRemove:
    #             painted.remove(i)
    #
    #         overlapIndex = 0
    #         for paintedIndex, (paintedStart, paintedEnd) in enumerate(painted):
    #             if paintedEnd < overlapStart:
    #                 overlapIndex = paintedIndex + 1
    #             if overlapStart<paintedEnd:
    #                 break
    #         painted.insert(overlapIndex, [overlapStart, overlapEnd])
    #         worklog.append(overlapEnd - overlapStart - workAlreadyDone)
    #
    #     return worklog

    # TLE
    # def amountPainted(self, paint):
    #     # find the min and the max
    #     minIndex = float('inf')
    #     maxIndex = 0
    #     for start, end in paint:
    #         minIndex = min(minIndex, start)
    #         maxIndex = max(maxIndex, end)
    #
    #     painted = {index: 0 for index in range(minIndex, maxIndex + 1)}
    #     workDone = []
    #
    #     for start, end in paint:
    #         work = 0
    #         for index in range(start, end):
    #             if painted[index]==0:
    #                 painted[index] = 1
    #                 work+=1
    #         workDone.append(work)
    #
    #     return workDone


if __name__ == '__main__':
    print(Solution().amountPainted([[8,9],[16,20],[18,19],[10,15],[7,9],[7,15]]))
    print(Solution().amountPainted([[81,87],[73,74],[74,79],[59,74],[45,68],[16,22],[33,98],[81,89],[54,88],[32,71],[34,38],[33,39],[25,96],[95,97],[2,32],[57,68],[18,93],[31,36],[76,89],[32,75],[71,79],[16,44],[56,78],[55,62],[14,38],[49,85],[45,85],[65,75],[12,66],[47,90],[64,100],[55,72],[33,42],[26,56],[63,97],[20,23],[15,85],[37,94],[17,74],[51,88],[51,60],[90,97],[86,95],[49,75],[59,71],[25,57],[24,44],[92,100],[27,30]]))
    print(Solution().amountPainted([[4,5],[2,5],[2,4],[0,1]]))
    print(Solution().amountPainted(paint = [[1,4],[4,7],[5,8]]))
    print(Solution().amountPainted(paint = [[1,4],[5,8],[4,7]]))
    print(Solution().amountPainted(paint = [[1,5],[2,4]]))
