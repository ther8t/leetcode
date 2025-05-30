import collections
import heapq


class Solution:
    """
    TLE. Its wise to keep in mind the things we need to keep in visited.
    Initially I had mistakenly taken only (neighbour, jumps), but we can't take (neighbour, len(set(updated_set)) either because there maybe a case where a node visits x other nodes and we come from other direction with different set of visited nodes than previous.
    They are not same situation but it's treated like it.

    """
    def shortestPathLength(self, graph) -> int:
        n = len(graph)
        visited = set()
        queue = []
        min_moves = collections.defaultdict(int)

        for i in range(n):
            # number of jumps, - len(stack), current_node, stack
            heapq.heappush(queue, (0, -1, i, [i]))
            visited.add((i, 0, 1))

        while queue:
            jumps, stack_size, current_node, stack = heapq.heappop(queue)
            if len(set(stack)) == len(graph):
                return jumps

            for neighbour in graph[current_node]:
                if (neighbour, jumps + 1) not in visited:
                    updated_set = stack + [neighbour]
                    if len(set(updated_set)) == len(graph):
                        return jumps + 1
                    heapq.heappush(queue, (jumps + 1, -len(set(updated_set)), neighbour, updated_set))
                    visited.add((neighbour, jumps + 1, len(set(updated_set))))

        return -1


    """
    This indeed was a difficult question. I made it even more difficult by optimising beyond what was required.
    This is how I began.
    1. I started with a simple Dijistra. That TLEd
    2. I recognised that I could search for previous results by looking at the neighbours' stack. Much like the multipoint BFS I had done for some questions. But not like rotting oranges.
       This multipoint BFS/bidirectional BFS is like a question where we connect the two edges. There was a question I remember where I needed to have two queues and search for the neighbour in other queue.
       It's like that. Except there are many queues
    3. I made an optimisation that a path travelled from 0-1-2-3 can be accessed from 0 and 3 both. So for both it's mask would be 1111. I could use both. This though right is difficult to code.
    
    Lesson Learnt : I was right about the bitmask. I knew it was needed. Even if I am not able to code, I sure should mention this in the interview.
    """
    def shortestPathLength(self, graph) -> int:
        target = (1 << len(graph)) - 1
        n = len(graph)
        visited = set()
        queue = []

        for i in range(n):
            # number of jumps, - len(stack), current_node, stack
            heapq.heappush(queue, (0, i, 1 << i))
            visited.add((i, 1 << i))

        while queue:
            jumps, current_node, stack = heapq.heappop(queue)
            if stack == target:
                return jumps

            for neighbour in graph[current_node]:
                updated_stack = stack | 1 << neighbour
                if (neighbour, updated_stack) not in visited:
                    heapq.heappush(queue, (jumps + 1, neighbour, updated_stack))
                    visited.add((neighbour, updated_stack))

        return -1


    # def shortestPathLength(self, graph) -> int:
    #     target = pow(2, len(graph)) - 1
    #     n = len(graph)
    #     visited = set()
    #     queue = []
    #     min_moves = collections.defaultdict(int)
    #
    #     for i in range(n):
    #         # number of jumps, - len(stack), current_node, stack
    #         heapq.heappush(queue, (0, i, i, pow(2, i)))
    #         visited.add((0, i))
    #         min_moves[(i, i, pow(2, i))] = 0
    #
    #     while queue:
    #         jumps, starting_node, current_node, stack = heapq.heappop(queue)
    #         if stack == target:
    #             return jumps
    #
    #         for neighbour in graph[current_node]:
    #             if (stack | neighbour, neighbour) in visited:
    #                 continue
    #             min_done_moves = float('inf')
    #             for sn, end_node, remainder in min_moves:
    #                 if neighbour != sn and neighbour != end_node:
    #                     continue
    #                 if remainder | stack == target:
    #                     min_done_moves = min(min_done_moves, min_moves[sn, end_node, remainder])
    #             if min_done_moves != float('inf'):
    #                 return jumps + min_done_moves + 1
    #
    #             updated_set = stack | pow(2, neighbour)
    #             if (updated_set, neighbour) not in visited:
    #                 if updated_set == target:
    #                     return jumps + 1
    #                 if (starting_node, neighbour, updated_set) in min_moves:
    #                     min_moves[(starting_node, neighbour, updated_set)] = min(min_moves[(starting_node, neighbour, updated_set)], jumps + 1)
    #                 else:
    #                     min_moves[(starting_node, neighbour, updated_set)] = jumps + 1
    #                 heapq.heappush(queue, (jumps + 1, starting_node, neighbour, updated_set))
    #                 visited.add((updated_set, neighbour))
    #
    #     return -1

    def shortestPathLength(self, graph) -> int:
        n = len(graph)

        def check():
            visited = set()
            queue = []

            for i in range(n):
                # number of jumps, - len(stack), current_node, stack
                heapq.heappush(queue, (0, -1, i, [i]))
                visited.add((i, 0, 1))

            while queue:
                jumps, stack_size, current_node, stack = heapq.heappop(queue)
                if jumps > mid:
                    continue
                if len(set(stack)) == len(graph):
                    return True

                for neighbour in graph[current_node]:
                    if (neighbour, jumps + 1) not in visited:
                        updated_set = stack + [neighbour]
                        heapq.heappush(queue, (jumps + 1, -len(set(updated_set)), neighbour, updated_set))
                        visited.add((neighbour, jumps + 1, len(set(updated_set))))
        lo, hi = 0, 20

        while lo < hi:
            mid = (lo + hi) // 2
            if check():
                hi = mid
            else:
                lo = mid + 1

        return hi



if __name__ == '__main__':
    print(Solution().shortestPathLength(graph = [[1,2,3],[0],[0],[0]]))
    print(Solution().shortestPathLength(graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]))
    print(Solution().shortestPathLength([[1,4],[0,3,4,7,9],[6,10],[1,10],[1,0],[6],[7,2,5],[6,1,8],[7],[1],[2,3]]))
    print(Solution().shortestPathLength([[1,3],[0,2,3],[1],[0,1]]))
    print(Solution().shortestPathLength([[1,2,3,5],[0,5],[0,4],[0],[5,2],[0,4,1]]))
