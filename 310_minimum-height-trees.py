import collections
import heapq


class Solution:
    def findMinHeightTrees(self, n: int, edges):
        neighbours = collections.defaultdict(list)

        for a, b in edges:
            neighbours[a].append(b)
            neighbours[b].append(a)

        edge_weight = collections.defaultdict(int)

        h = []
        for node in neighbours:
            if len(neighbours[node]) == 1:
                edge_weight[(node, neighbours[node][0])] = 1
                edge_weight[(neighbours[node][0], node)] = 1
                heapq.heappush(h, (1, node, neighbours[node][0]))

        ans = 0
        while h:
            weight, s, d = heapq.heappop(h)
            if (s, d) in edge_weight and edge_weight[(s, d)] < weight:
                continue
            ans = max(ans, weight)

            for n in neighbours[d]:
                if (d, n) in edge_weight and edge_weight[(d, n)] <= weight + 1:
                    continue
                edge_weight[(d, n)] = weight + 1
                edge_weight[(n, d)] = weight + 1
                heapq.heappush(h, (weight + 1, d, n))

        ans_set = set()
        for s, d in edge_weight:
            if edge_weight[(s, d)] == ans:
                ans_set.add(s)
                ans_set.add(d)

        return list(ans_set)


if __name__ == '__main__':
    print(Solution().findMinHeightTrees(n = 4, edges = [[1,0],[1,2],[1,3]]))
    print(Solution().findMinHeightTrees(n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]))
