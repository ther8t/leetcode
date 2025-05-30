import heapq


class Solution:
    # def minMeetingRooms(self, intervals) -> int:
    #     intervals.sort(key=lambda x: (x[0], -x[1]))
    #
    #     stack = []
    #     rooms = 0
    #
    #     for start, end in intervals:
    #         while len(stack) > 0 and start >= stack[-1]:
    #             stack.pop()
    #         stack.append(start)
    #         rooms = max(len(stack), rooms)
    #         while len(stack) > 0 and end > stack[-1]:
    #             stack.pop()
    #         stack.append(end)
    #
    #     return rooms

    """
    Revision 2:
    This is a brilliant piece of code. I remember a similar algorithm for bracket checking and one for some level checking or something. Another similar question to which this can be related to is merging k sorted linkedlists.
    In that question as well we have to start a priority queue of the first element of the linkedlist and sort into the final list based on the least value.
    """
    def minMeetingRooms(self, intervals) -> int:
        rooms = []
        intervals.sort(key=lambda x:x[0])
        heapq.heappush(rooms, (intervals[0][1], intervals[0]))

        min_rooms = 1
        for interval in intervals[1:]:
            if interval[0] >= rooms[0][1][1]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, (interval[1], interval))
            min_rooms = max(len(rooms), min_rooms)

        return min_rooms



    # # Accepted : 88% Same as the common k problem. It's like counting brackets.
    # def minMeetingRooms(self, intervals) -> int:
    #     ptr_s, ptr_e = 0, 0
    #     starts, ends = [], []
    #
    #     for start, end in intervals:
    #         starts.append(start)
    #         ends.append(end)
    #
    #     rooms = 0
    #     min_rooms = 0
    #     starts.sort()
    #     ends.sort()
    #     while ptr_s < len(starts) and ptr_e < len(ends):
    #         if starts[ptr_s] < ends[ptr_e]:
    #             rooms += 1
    #             min_rooms = max(rooms, min_rooms)
    #             ptr_s += 1
    #         else:
    #             rooms -= 1
    #             ptr_e += 1
    #     return min_rooms

    # # Accepted : 50%
    # def minMeetingRooms(self, intervals) -> int:
    #     times = []
    #     for start, end in intervals:
    #         times.append((start, 1))
    #         times.append((end - 1, -1))
    #
    #     times.sort(key=lambda x: (x[0], -1*x[1]))
    #
    #     rooms = 0
    #     min_rooms = 0
    #     for time, counter in times:
    #         rooms += counter
    #         min_rooms = max(rooms, min_rooms)
    #
    #     return min_rooms


if __name__ == '__main__':
    print(Solution().minMeetingRooms([[8, 17], [5, 15], [6, 20]]))  # 3
    print(Solution().minMeetingRooms([[6, 15], [13, 20], [6, 17]]))  # 3
    print(Solution().minMeetingRooms([[13, 15], [1, 13]]))  # 1
    print(Solution().minMeetingRooms([[1, 5], [8, 9], [8, 9]]))  # 2
    print(Solution().minMeetingRooms([[0, 30], [5, 10], [15, 20]]))  # 2
    print(Solution().minMeetingRooms([[6, 17], [8, 9], [11, 12], [6, 9]]))  # 3
    print(Solution().minMeetingRooms([[5,8],[6,8]]))  # 2
