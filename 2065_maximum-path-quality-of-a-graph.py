import collections
import heapq


class Solution:
    """
    Accepted 24%
    """
    def maximalPathQuality(self, values, edges, maxTime: int) -> int:
        visited = set()
        stack = [(-values[0], 0, 0, [0], [])]
        node_neighbours = collections.defaultdict(list)
        edge_weight = collections.defaultdict(int)

        for s, e, w in edges:
            node_neighbours[s].append(e)
            node_neighbours[e].append(s)
            edge_weight[(s, e)] = w
            edge_weight[(e, s)] = w

        highest_score = 0

        while stack:
            current_score, current_node, current_time, node_visited, path_visited = heapq.heappop(stack)
            if current_time > maxTime:
                continue
            if current_node == 0:
                highest_score = max(highest_score, -current_score)

            for n in node_neighbours[current_node]:
                next_time = current_time + edge_weight[(current_node, n)]
                new_path = tuple(node_visited + [n])

                # what is interesting is that the code also works with new_path not in visited.
                # The only condition then is to check if a path has been visited in the current traversed path, not that it's been globally traversed.
                # if new_path not in visited and (current_node, n) not in path_visited and next_time <= maxTime:
                if (current_node, n) not in path_visited and next_time <= maxTime:
                    new_score = current_score
                    if n not in node_visited:
                        new_score = current_score - values[n]
                    visited.add(new_path)
                    heapq.heappush(stack, (new_score, n, next_time, node_visited + [n], path_visited + [(current_node, n)]))

        return highest_score


if __name__ == '__main__':
    # print(Solution().maximalPathQuality(values = [0,32,10,43], edges = [[0,1,10],[1,2,15],[0,3,10]], maxTime = 49))
    # print(Solution().maximalPathQuality(values = [5,10,15,20], edges = [[0,1,10],[1,2,10],[0,3,10]], maxTime = 30))
    # print(Solution().maximalPathQuality(values = [1,2,3,4], edges = [[0,1,10],[1,2,11],[2,3,12],[1,3,13]], maxTime = 50))
    print(Solution().maximalPathQuality([100000000,100000000,100000000,100000000,100000000,100000000,100000000,100000000,100000000,100000000], [[0,1,10],[1,2,10],[2,3,10],[3,4,10],[4,5,10],[5,6,10],[6,7,10],[7,8,10],[8,9,10],[0,9,10]], 100))
