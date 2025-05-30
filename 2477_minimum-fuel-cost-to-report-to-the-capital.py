import collections
import math


class Solution:
    def minimumFuelCost(self, roads, seats: int) -> int:
        conneted = collections.defaultdict(list)

        for a, b in roads:
            conneted[a].append(b)
            conneted[b].append(a)

        visited = set()
        road_weight = collections.defaultdict(int)

        def dfs(node):
            children_count = 0
            for n in conneted[node]:
                if n not in visited:
                    visited.add(n)
                    children = dfs(n)
                    road_weight[tuple(sorted([node, n]))] = children
                    children_count += children

            return children_count + 1

        visited.add(0)
        dfs(0)
        return sum([math.ceil(road_weight[r] / seats) for r in road_weight])



if __name__ == '__main__':
    print(Solution().minimumFuelCost(roads = [[0,1],[0,2],[0,3]], seats = 5))
    print(Solution().minimumFuelCost(roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], seats = 2))
    print(Solution().minimumFuelCost(roads = [], seats = 1))
