import collections
import heapq


class Solution:
    def maximumScore(self, scores, edges) -> int:
        if len(edges) == 0:
            return -1
        neighbours = collections.defaultdict(set)
        for node1, node2 in edges:
            neighbours[node1].add((scores[node2], node2))
            neighbours[node2].add((scores[node1], node1))

        for n in neighbours:
            neighbours[n] = sorted(neighbours[n], reverse=True)

        max_sum = -1
        for node1, node2 in edges:
            node1_neighbours = neighbours[node1]
            node2_neighbours = neighbours[node2]
            if not node1_neighbours or not node2_neighbours:
                continue

            node0, node3 = None, None
            for score, node in node1_neighbours:
                if node != node2:
                    node0 = node
                    break
            for score, node in node2_neighbours:
                if node != node1 and node != node0:
                    node3 = node
                    break
            if node0 is not None and node3 is not None and node0 != node3:
                max_sum = max(max_sum, scores[node0] + scores[node1] + scores[node2] + scores[node3])

            node0, node3 = None, None
            for score, node in node2_neighbours:
                if node != node1:
                    node3 = node
                    break
            for score, node in node1_neighbours:
                if node != node2 and node != node3:
                    node0 = node
                    break
            if node0 is not None and node3 is not None and node0 != node3:
                max_sum = max(max_sum, scores[node0] + scores[node1] + scores[node2] + scores[node3])

        return max_sum

    # def maximumScore(self, scores, edges) -> int:
    #     if len(edges) == 0:
    #         return -1
    #     neighbours = collections.defaultdict(list)
    #     for node1, node2 in edges:
    #         neighbours[node1].append((scores[node2], node2))
    #         neighbours[node2].append((scores[node1], node1))
    #
    #     for n in neighbours:
    #         neighbours[n] = sorted(neighbours[n], reverse=True)
    #
    #     queue = []
    #     for node1, node2 in edges:
    #         heapq.heappush(queue, (-1 * (scores[node1] + scores[node2]), node1, node2))
    #
    #     max_sum = -1
    #     while queue:
    #         negative_sum, node1, node2 = heapq.heappop(queue)
    #         node1_neighbours = neighbours[node1]
    #         node2_neighbours = neighbours[node2]
    #         if not node1_neighbours or not node2_neighbours:
    #             continue
    #
    #         node0, node3 = None, None
    #         for score, node in node1_neighbours:
    #             if node != node2:
    #                 node0 = node
    #                 break
    #         for score, node in node2_neighbours:
    #             if node != node1 and node != node0:
    #                 node3 = node
    #                 break
    #         if node0 is not None and node3 is not None and node0 != node3:
    #             max_sum = max(max_sum, scores[node0] + scores[node1] + scores[node2] + scores[node3])
    #
    #         node0, node3 = None, None
    #         for score, node in node2_neighbours:
    #             if node != node1:
    #                 node3 = node
    #                 break
    #         for score, node in node1_neighbours:
    #             if node != node2 and node != node3:
    #                 node0 = node
    #                 break
    #         if node0 is not None and node3 is not None and node0 != node3:
    #             max_sum = max(max_sum, scores[node0] + scores[node1] + scores[node2] + scores[node3])
    #
    #     return max_sum


if __name__ == '__main__':
    print(Solution().maximumScore([6,17,3,22,27,18,10,26,30,22,16,18], [[0,1],[6,7],[0,2],[6,8],[0,3],[6,9],[0,4],[6,10],[0,5],[6,11],[1,2],[7,8],[1,3],[7,9],[1,4],[7,10],[1,5],[7,11],[2,3],[8,9],[2,4],[8,10],[2,5],[8,11],[3,4],[9,10],[3,5],[9,11],[4,5],[10,11]]))
    print(Solution().maximumScore([18,6,4,9,8,2], [[0,1],[0,2],[0,3],[0,4],[0,5],[1,2],[1,3],[1,4],[1,5],[2,3],[2,4],[2,5],[3,4],[3,5],[4,5]]))
    print(Solution().maximumScore([14, 12, 10, 8, 1, 2, 3, 1],
                                  [[0, 1], [0, 2], [0, 3], [0, 4], [1, 5], [1, 6], [1, 7], [1, 2]])) #44
