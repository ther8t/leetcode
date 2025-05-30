import collections


class Solution:
    def placedCoins(self, edges, cost):
        neighbours = collections.defaultdict(list)
        for a, b in edges:
            neighbours[a].append(b)
            neighbours[b].append(a)

        coins = [0 for _ in range(len(cost))]

        def dfs(node):
            nonlocal coins
            top_values = [cost[node]]
            for n in neighbours[node]:
                if (n, node) in visited or (node, n) in visited:
                    continue
                visited.add((node, n))
                visited.add((n, node))
                top_values += dfs(n)

            top_values.sort(reverse=True)
            if len(top_values) < 3:
                coins[node] = 1
            else:
                coins[node] = max(top_values[0] * top_values[-1] * top_values[-2], top_values[0] * top_values[1] * top_values[2])
                if coins[node] < 0:
                    coins[node] = 0

            return top_values

        visited = set()
        dfs(0)
        return coins


if __name__ == '__main__':
    print(Solution().placedCoins(edges = [[0,1],[0,2],[0,3],[0,4],[0,5]], cost = [1,2,3,4,5,6]))
    print(Solution().placedCoins(edges = [[0,1],[0,2],[1,3],[1,4],[1,5],[2,6],[2,7],[2,8]], cost = [1,4,2,3,5,7,8,-4,2]))
    print(Solution().placedCoins(edges = [[0,1],[0,2]], cost = [1,2,-2]))
