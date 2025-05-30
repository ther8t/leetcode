import collections
import heapq

from sortedcontainers import SortedList


class Solution:
    # Accepted
    def busiestServers(self, k: int, arrival, load):
        request_counter = [0]*k
        occupied_servers = []
        free_servers = SortedList()
        for i in range(k):
            free_servers.add(i)

        for index, (arrival_time, processing_time) in enumerate(zip(arrival, load)):
            while len(occupied_servers) > 0 and occupied_servers[0][0] <= arrival_time:
                finish_time, server_address = heapq.heappop(occupied_servers)
                free_servers.add(server_address)

            default_server = index % k
            if not list(free_servers):
                continue
            allocated_server_index = free_servers.bisect_left(default_server)
            if allocated_server_index == len(free_servers):
                allocated_server = free_servers[0]
            else:
                allocated_server = free_servers[allocated_server_index]

            free_servers.remove(allocated_server)
            heapq.heappush(occupied_servers, (arrival_time + processing_time, allocated_server))
            request_counter[allocated_server] += 1

        max_requests_handled = max(request_counter)

        max_bearing_servers = []
        for server_address, requests_handled in enumerate(request_counter):
            if requests_handled == max_requests_handled:
                max_bearing_servers.append(server_address)

        return max_bearing_servers


if __name__ == '__main__':
    # print(Solution().busiestServers())
    print(Solution().busiestServers(k = 3, arrival = [1,2,3], load = [10,12,11]))
    print(Solution().busiestServers(3, [1,2,3,4,8,9,10], [5,2,10,3,1,2,2]))
