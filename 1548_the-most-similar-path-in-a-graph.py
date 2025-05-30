import collections
import heapq


class Solution:
    """
    This question was fairly simple as well. Why the solution never came to me in the first iteration eludes me.
    I originally started with DFS. I soon realised that I could reach the result and return it before completing the whole DFS if I used Dijikstra.

    I used Dijikstra but I failed to recognise that I could mark some of the nodes visited.
    This created a huge problem because I then began to eliminate the nodes which did not exist in the graph.
    After a lot of change I rolled back to the original code which had TLEd before and added a visited set. It worked!!
    """
    def mostSimilar(self, n: int, roads, names, targetPath):
        connections = collections.defaultdict(list)

        for n1, n2 in roads:
            connections[n1].append(n2)
            connections[n2].append(n1)

        queue = []
        visited = set()
        for node_index in range(len(names)):
            heapq.heappush(queue, (0 if names[node_index] == targetPath[0] else 1, -1, node_index, [node_index]))
            visited.add((0 if names[node_index] == targetPath[0] else 1, -1, node_index))

        while queue:
            edit_distance, h, current_node_index, stack = heapq.heappop(queue)
            if len(stack) == len(targetPath):
                return stack
            index = len(stack)

            for neighbour in connections[current_node_index]:
                updated_edit_distance = edit_distance + (0 if names[neighbour] == targetPath[index] else 1)
                if (updated_edit_distance, h - 1, neighbour) not in visited:
                    heapq.heappush(queue, (updated_edit_distance, h - 1, neighbour, stack + [neighbour]))
                    visited.add((updated_edit_distance, h - 1, neighbour))


if __name__ == '__main__':
    print(Solution().mostSimilar(n = 5, roads = [[0,2],[0,3],[1,2],[1,3],[1,4],[2,4]], names = ["ATL","PEK","LAX","DXB","HND"], targetPath = ["ATL","DXB","HND","LAX"]))
    print(Solution().mostSimilar(n = 4, roads = [[1,0],[2,0],[3,0],[2,1],[3,1],[3,2]], names = ["ATL","PEK","LAX","DXB"], targetPath = ["ABC","DEF","GHI","JKL","MNO","PQR","STU","VWX"]))
    print(Solution().mostSimilar(n = 6, roads = [[0,1],[1,2],[2,3],[3,4],[4,5]], names = ["ATL","PEK","LAX","ATL","DXB","HND"], targetPath = ["ATL","DXB","HND","DXB","ATL","LAX","PEK"]))
    print(Solution().mostSimilar(3, [[2,0],[2,1],[0,1]], ["CIA","MGA","CUU"], ["GNV","LSI","VAK","ADB","MSQ","ANS","KTN","YXD","WNA","BAQ","CJC","DOH","ORY","LAX","DRO","LIH","KER","IPH","YPR","MAO","MLH","LCY"]))
    print(Solution().mostSimilar(5, [[1,2],[2,4],[4,1],[4,0],[3,0]], ["CBB","ERF","CBB","RSC","CBB"], ["CBB","RSC","RSC","CBB","ERF","CBB","RSC","RSC","CBB","CBB","CBB","ERF","ERF","CBB","CBB","ERF","CBB","CBB","RSC","CBB","CBB","CBB","RSC","ERF","ERF","CBB","CBB","CBB","RSC","ERF","CBB","RSC","ERF","RSC","CBB","ERF","RSC","RSC","CBB","RSC","CBB","CBB","RSC","CBB","ERF","CBB","RSC"]))
    print(Solution().mostSimilar(25, [[0,1],[1,6],[3,6],[2,3],[2,4],[4,5],[6,5],[6,7],[8,7],[8,12],[8,9],[10,9],[12,11],[12,9],[16,15],[15,14],[14,13],[14,19],[19,13],[20,19],[21,19],[22,19],[23,19],[24,19],[13,17],[17,18],[13,6],[18,12]], ["ICN","IKT","ATH","TBS","TLV","LCA","DME","AUH","CGK","DPS","KUL","BKK","SIN","LED","SVO","BEG","TIV","MSQ","PEK","PRG","DUB","MXP","ORY","CRL","AMS"], ["AXX","TBS","DME"]))
