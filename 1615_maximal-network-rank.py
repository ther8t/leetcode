import collections


class Solution:
    def maximalNetworkRank(self, n: int, roads) -> int:
        network = collections.defaultdict(list)

        for city1, city2 in roads:
            network[city1].append(city2)
            network[city2].append(city1)

        cities_sorted = list(network.keys())

        max_network_rank = 0
        for i in range(len(cities_sorted) - 1):
            for j in range(i + 1, len(cities_sorted)):
                city1 = cities_sorted[i]
                city2 = cities_sorted[j]
                max_network_rank = max(max_network_rank,
                                       len(network[city1]) + len(network[city2]) + (-1 if city1 in network[city2] else 0))

        return max_network_rank


if __name__ == '__main__':
    print(Solution().maximalNetworkRank(5, [[2,3],[0,3],[0,4],[4,1]]))
