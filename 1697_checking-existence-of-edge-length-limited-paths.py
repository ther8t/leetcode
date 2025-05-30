import collections
import heapq


class DSU:
    def __init__(self, n):
        self.representative = [i for i in range(n)]

    def find(self, element):
        if self.representative[element] != element:
            self.representative[element] = self.find(self.representative[element])
        return self.representative[element]

    def combine(self, element1, element2):
        representative_element1 = self.find(element1)
        representative_element2 = self.find(element2)

        if representative_element1 == representative_element2:
            return

        self.representative[representative_element1] = representative_element2


class Solution:
    """
        A similar algo to the DSU with just a few exception.
        We sort the queries as well as the edge list.
        We try to combine the edges only till the limit of the current query. Then we check if the current query is satisfied or not.
        We don't have to traverse the complete set of queries all the time because we can limit it by sorting.
        Something similar could also have been done in the previous code by sorting and then breaking the query index when the limit >= distance.
    """
    def distanceLimitedPathsExist(self, n: int, edgeList, queries):
        queries = sorted([(limit, n1, n2, index) for index, (n1, n2, limit) in enumerate(queries)])
        edgeList = sorted([(distance, n1, n2) for n1, n2, distance in edgeList])

        dsu = DSU(n)
        result = [False] * len(queries)
        ptr = 0
        for limit, n1, n2, index in queries:
            while ptr < len(edgeList) and edgeList[ptr][0] < limit:
                dsu.combine(edgeList[ptr][1], edgeList[ptr][2])
                ptr += 1
            if dsu.find(n1) == dsu.find(n2):
                result[index] = True

        return result

    # # TLE : This solution TLEs for obvious reason that we traverse the query list over and over again to check if the two nodes are connected. This has the same time as BFS + priority queue does.
    # def distanceLimitedPathsExist(self, n: int, edgeList, queries):
    #     query_limit_index_map = set()
    #     edge_heap = []
    #     connection_distance_map = collections.defaultdict(int)
    #     for n1, n2, d in edgeList:
    #         connection_distance_map[(n1, n2)] = min(connection_distance_map[(n1, n2)] if (n1, n2) in connection_distance_map else float('inf'), d)
    #         connection_distance_map[(n2, n1)] = min(connection_distance_map[(n2, n1)] if (n2, n1) in connection_distance_map else float('inf'), d)
    #
    #     for n1, n2, d in edgeList:
    #         heapq.heappush(edge_heap, (connection_distance_map[n1, n2], n1, n2))
    #
    #     for index, (n1, n2, limit) in enumerate(queries):
    #         query_limit_index_map.add((n1, n2, limit, index))
    #
    #     dsu = DSU(n)
    #     result = [False] * len(queries)
    #     while edge_heap:
    #         distance, n1, n2 = heapq.heappop(edge_heap)
    #         dsu.combine(n1, n2)
    #         to_remove = []
    #         for n1, n2, limit, index in query_limit_index_map:
    #             if limit <= distance:
    #                 to_remove.append((n1, n2, limit, index))
    #                 continue
    #             if dsu.find(n1) == dsu.find(n2):
    #                 result[index] = True
    #                 to_remove.append((n1, n2, limit, index))
    #
    #         for i in to_remove:
    #             query_limit_index_map.remove(i)

        return result


    """
    I made a grievous mistake in solving this question by taking visited as a set of indexes only.
    It causes a problem when I visit a path and it can't be visited again even though it may have a smaller distance to contribute.
    The thing which I also realised much clearly than before is that early exit is possible only in the case when I use priority queue. Otherwise I would have to complete the who bfs process.

    This question however TLEs. Understandably so because from a source node to a target node the process of making connections is repeated over and over again.
    My very initial thinking was about using DSUs. I built a class and then I began to code a bidirectional BFS only to realise very late in the night that I had not used DSU.
    That didn't work, perhaps for the same reason as taking just index in visited, I'll check that so I resorted to simple BFS.
    """
    # This is a bidirection BFS implementation. There is a lot of confusion. I thought I had completed it but there are several wrinkles which need to be ironed out.
    # def distanceLimitedPathsExist(self, n: int, edgeList, queries):
    #     connection_distance_map = collections.defaultdict(int)
    #     connections = collections.defaultdict(set)
    #
    #     for n1, n2, d in edgeList:
    #         connection_distance_map[(n1, n2)] = min(connection_distance_map[(n1, n2)] if (n1, n2) in connection_distance_map else float('inf'), d)
    #         connection_distance_map[(n2, n1)] = min(connection_distance_map[(n2, n1)] if (n2, n1) in connection_distance_map else float('inf'), d)
    #         connections[n1].add(n2)
    #         connections[n2].add(n1)
    #
    #     def bfs(i, j, limit):
    #         queuei = [(0, i)]
    #         queuej = [(0, j)]
    #         visitedi = collections.defaultdict(int)
    #         visitedi[i] = 0
    #         visitedj = collections.defaultdict(int)
    #         visitedj[j] = 0
    #
    #         while queuei and queuej:
    #             if len(queuei) > len(queuej):
    #                 queuei, queuej, visitedi, visitedj = queuej, queuei, visitedj, visitedi
    #             travelled_distance, node_index = heapq.heappop(queuei)
    #             if travelled_distance >= limit:
    #                 return False
    #             if node_index == j:
    #                 return True
    #
    #             for neighbour_index in connections[node_index]:
    #                 updated_distance = max(travelled_distance, connection_distance_map[(node_index, neighbour_index)])
    #                 if updated_distance < limit and (neighbour_index not in visitedi or visitedi[neighbour_index] > updated_distance):
    #                     visitedi[neighbour_index] = updated_distance
    #                     heapq.heappush(queuei, (updated_distance, neighbour_index))
    #         return False
    #
    #     out = []
    #     for n1, n2, limit in queries:
    #         out.append(bfs(n1, n2, limit))
    #
    #     return out

    # # TLE Simple BFS with priority queue.
    # def distanceLimitedPathsExist(self, n: int, edgeList, queries):
    #     connection_distance_map = collections.defaultdict(int)
    #     connections = collections.defaultdict(set)
    #
    #     for n1, n2, d in edgeList:
    #         connection_distance_map[(n1, n2)] = min(connection_distance_map[(n1, n2)] if (n1, n2) in connection_distance_map else float('inf'), d)
    #         connection_distance_map[(n2, n1)] = min(connection_distance_map[(n2, n1)] if (n2, n1) in connection_distance_map else float('inf'), d)
    #         connections[n1].add(n2)
    #         connections[n2].add(n1)
    #
    #     def bfs(i, j, limit):
    #         queue = [(0, i)]
    #         visited = collections.defaultdict(int)
    #
    #         while queue:
    #             travelled_distance, node_index = heapq.heappop(queue)
    #             if travelled_distance >= limit:
    #                 return False
    #             if node_index == j:
    #                 return True
    #
    #             for neighbour_index in connections[node_index]:
    #                 updated_distance = max(travelled_distance, connection_distance_map[(node_index, neighbour_index)])
    #                 if neighbour_index not in visited or visited[neighbour_index] > updated_distance:
    #                     visited[neighbour_index] = updated_distance
    #                     heapq.heappush(queue, (updated_distance, neighbour_index))
    #         return False
    #
    #     out = []
    #     for n1, n2, limit in queries:
    #         out.append(bfs(n1, n2, limit))
    #
    #     return out


if __name__ == '__main__':
    print(Solution().distanceLimitedPathsExist(n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]))
    print(Solution().distanceLimitedPathsExist(n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]]))
    print(Solution().distanceLimitedPathsExist(13, [[9,1,53],[3,2,66],[12,5,99],[9,7,26],[1,4,78],[11,1,62],[3,10,50],[12,1,71],[12,6,63],[1,10,63],[9,10,88],[9,11,59],[1,4,37],[4,2,63],[0,2,26],[6,12,98],[9,11,99],[4,5,40],[2,8,25],[4,2,35],[8,10,9],[11,9,25],[10,11,11],[7,6,89],[2,4,99],[10,4,63]], [[9,7,65],[9,6,1],[4,5,34],[10,8,43],[3,7,76],[4,2,15],[7,6,52],[2,0,50],[7,6,62],[1,0,81],[4,5,35],[0,11,86],[12,5,50],[11,2,2],[9,5,6],[12,0,95],[10,6,9],[9,4,73],[6,10,48],[12,0,91],[9,10,58],[9,8,73],[2,3,44],[7,11,83],[5,3,14],[6,2,33]]))





