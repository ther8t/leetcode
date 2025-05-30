import collections
import heapq


class Solution:
    def mostBooked(self, n: int, meetings) -> int:
        ptr = 0
        vacant_queue = []
        occupied_queue = []
        meetings.sort()
        for i in range(n):
            heapq.heappush(vacant_queue, i)
        counter = collections.Counter()

        while ptr < len(meetings):
            current_time = meetings[ptr][0]
            if not vacant_queue:
                current_time = max(meetings[ptr][0], occupied_queue[0][0] if occupied_queue else 0)
            while occupied_queue and occupied_queue[0][0] <= current_time:
                popped_time, popped_meeting_room_index = heapq.heappop(occupied_queue)
                heapq.heappush(vacant_queue, popped_meeting_room_index)
            while vacant_queue and ptr < len(meetings):
                if meetings[ptr][0] > current_time:
                    break
                vacant_meeting_room_index = heapq.heappop(vacant_queue)
                counter[vacant_meeting_room_index] += 1
                heapq.heappush(occupied_queue, (current_time + meetings[ptr][1] - meetings[ptr][0], vacant_meeting_room_index))
                ptr += 1

        # I am actually surprised by one thing 
        return max(counter, key=lambda x: counter[x])


    """
    There is one thing which I fail to understand. The accepted approach is to fill in as many vacant rooms as possible before current time.
    I had an approach of using a for loop to iterate over meetings. I vacate the rooms before my time and then find the room with least index.
    This happened one meeting room allocation per iteration. For some reason this is incorrect.
    """
    def mostBooked(self, n: int, meetings) -> int:
        vacant, occupied = [], []
        for i in range(n):
            heapq.heappush(vacant, (i, -1))

        meetings.sort()
        counter = collections.defaultdict(int)
        ptr = 0
        while ptr < len(meetings):
            current_time = meetings[ptr][0]
            if not vacant:
                current_time = occupied[0][0]

            while occupied and occupied[0][0] <= current_time:
                _, room_id = heapq.heappop(occupied)
                heapq.heappush(vacant, (room_id, -1))

            while vacant and ptr < len(meetings) and meetings[ptr][0] <= current_time:
                room_id, _ = heapq.heappop(vacant)
                counter[room_id] += 1
                heapq.heappush(occupied, (current_time + meetings[ptr][1] - meetings[ptr][0], room_id))
                ptr += 1

        return max(counter, key=lambda x: counter[x])


if __name__ == '__main__':
    print(Solution().mostBooked(n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]))
    print(Solution().mostBooked(n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]))
    print(Solution().mostBooked(2, [[4,11],[1,13],[8,15],[9,18],[0,17]]))
