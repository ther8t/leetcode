import collections
import heapq


class DSU:

    def __init__(self, length):
        self.parent = [i for i in range(length)]
        self.size = [1] * length

    def find(self, a):
        if a != self.parent[a]:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def unite(self, a, b):
        parent_a, parent_b = self.find(a), self.find(b)
        if parent_a == parent_b:
            return
        if self.size[parent_a] < self.size[parent_b]:
            a, b = b, a
            parent_a, parent_b = parent_b, parent_a

        self.parent[parent_b] = parent_a
        self.size[parent_a] += self.size[parent_b]


class Solution:
    """
    I figured this out because of a hint given I saw. My original thinking was to fix a single point as a root and DFS all other nodes from there.
    The paths that we would eventually get would then be compare with others of the same values to check if they have any greater value above them which would prevent them from being a good path.
    This would have been an O(n3) solution.

    After seeing the hint about starting with the smallest number first, it just dawned on me in a flash that DSU would be a good DS.
    Then it was pretty much connecting the dots.
    """
    def numberOfGoodPaths(self, vals, edges) -> int:
        val_index_map, value_neighbour_map = collections.defaultdict(list), collections.defaultdict(set)

        for index, val in enumerate(vals):
            val_index_map[val].append(index)

        for node1_index, node2_index in edges:
            value_neighbour_map[node1_index].add(node2_index)
            value_neighbour_map[node2_index].add(node1_index)

        dsu = DSU(len(vals))
        out = 0
        for val in sorted(val_index_map):
            for index in val_index_map[val]:
                for neighbour in value_neighbour_map[index]:
                    if vals[index] >= vals[neighbour]:
                        dsu.unite(index, neighbour)
            parent_index_map = collections.defaultdict(list)
            for index in val_index_map[val]:
                parent_index_map[dsu.find(index)].append(index)

            for parent in parent_index_map:
                children_length = len(parent_index_map[parent])
                out += ((children_length) * (children_length - 1) // 2 + children_length)

            """
            This was a clever optimisation.
            Pat on my back that I actually did figure it out.
            My original method was to compare all the indexes with each other like handshakes. This would have been an O(n2) operation.
            But then I figure that all I need to compare is if the indexes have the same parent. I grouped the one's with the same parent together. n*(n-1)/2 - total number of handshakes.
            + the number of children because each one is a good path onto itself.
            """
            # for i in range(len(val_index_map[val])):
            #     for j in range(i, len(val_index_map[val])):
            #         if dsu.find(val_index_map[val][i]) == dsu.find(val_index_map[val][j]):
            #             out += 1
        return out


    """
    Revision 2:
    I was able to gather at first sight that this is a question about DSU.
    My first attempt to solving this question was to consider edges. The weight of the edges I chose was the max of the nodes connected with that edge.
    I simply move in an increasing edge weight and check for all the nodes of higher weight if they connect.
    This is redundant because if we connect the ones which are lower val than our number we only simply need to check our number.
    Accepted 79%
    """
    def numberOfGoodPaths(self, vals, edges) -> int:
        edge_connect_map = collections.defaultdict(list)
        for n1, n2 in edges:
            edge_connect_map[max(vals[n1], vals[n2])].append((n1, n2))

        similar = collections.defaultdict(list)
        for i, v in enumerate(vals):
            similar[v].append(i)

        dsu = DSU(len(vals))

        out = 0
        for weight in sorted(edge_connect_map):
            for n1, n2 in edge_connect_map[weight]:
                dsu.unite(n1, n2)

            parent_children_map = collections.defaultdict(list)
            for index in similar[weight]:
                parent_children_map[dsu.find(index)].append(index)

            for parent in parent_children_map:
                children_count = len(parent_children_map[parent])
                out += children_count * (children_count - 1) // 2

            """
            Remember:
            Instead of checking for all the higher values than the weight, we SHOULD just check for the nodes with values == weight
            The nodes of higher values would not be connected anyway, because they have still not had the chance to appear in the iteration.
            """
            # for s in sorted(similar, reverse=True):
            #     if s < weight:
            #         break
            #     arr = similar[s]
            #     for i in range(len(arr)):
            #         for j in range(i + 1, len(arr)):
            #             n1, n2 = arr[i], arr[j]
            #             if dsu.find(n1) == dsu.find(n2):
            #                 out += 1


        return out + len(vals)





if __name__ == '__main__':
    print(Solution().numberOfGoodPaths(vals = [1,1,2,2,3], edges = [[0,1],[1,2],[2,3],[2,4]]))
    print(Solution().numberOfGoodPaths(vals = [1], edges = []))
    print(Solution().numberOfGoodPaths(vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]))
    print(Solution().numberOfGoodPaths([2,4,1,2,2,5,3,4,4], [[0,1],[2,1],[0,3],[4,1],[4,5],[3,6],[7,5],[2,8]]))
