import collections
import heapq


class Solution:
    # # TLE 32/33 at first but accepted later because of index_map[arr[prev_element_index]] = []
    # def minJumps(self, arr) -> int:
    #     if len(arr) == 1:
    #         return 0
    #     if arr[0] == arr[-1]:
    #         return 1
    #     index_map = collections.defaultdict(list)
    #     for index, num in enumerate(arr):
    #         index_map[num].append(index)
    #
    #     steps = [len(arr) - 1] * len(arr)
    #     steps[0] = 0
    #     steps_index_map = collections.defaultdict(list)
    #     steps_index_map[0].append(0)
    #
    #     for d in range(1, len(arr) - 1):
    #         # find all the elements of distance d-1. Make a list of all those which are at 1 more distance from
    #         # the current distance element ie at distance d. They will be those which are at a distance 1 index
    #         # from them or the same numbers
    #         all_prev_elements = steps_index_map[d - 1]
    #         for prev_element_index in all_prev_elements:
    #             reduce_distance = []
    #             if prev_element_index > 0: reduce_distance.append(prev_element_index - 1)
    #             if prev_element_index < len(arr) - 1: reduce_distance.append(prev_element_index + 1)
    #             reduce_distance += index_map[arr[prev_element_index]]
    #             del index_map[arr[prev_element_index]]
    #             for similar_index in reduce_distance:
    #                 if similar_index == len(arr) - 1:
    #                     return d
    #                 if steps[similar_index] > d:
    #                     steps_index_map[d].append(similar_index)
    #                     steps[similar_index] = d
    #
    #     return int(steps[-1])

    # # TLE
    # def minJumps(self, arr) -> int:
    #     if len(arr) == 1:
    #         return 0
    #     if arr[0] == arr[-1]:
    #         return 1
    #     index_map = collections.defaultdict(list)
    #     for index, num in enumerate(arr):
    #         index_map[num].append(index)
    #
    #     def dfs(position, steps):
    #         if steps > mid:
    #             return False
    #         if position == len(arr) - 1:
    #             return True
    #         next_positions = set()
    #         for i in index_map[arr[position]]:
    #             if steps + 1 < visited[i]:
    #                 next_positions.add(i)
    #         if position > 0 and steps + 1 < visited[position - 1]: next_positions.add(position - 1)
    #         if position < len(arr) - 1 and steps + 1 < visited[position + 1]: next_positions.add(position + 1)
    #
    #         for next_position in next_positions:
    #             visited[next_position] = steps + 1
    #             if dfs(next_position, steps + 1):
    #                 return True
    #         return False
    #
    #     left, right = 0, len(arr) - 1
    #     while left < right:
    #         mid = (left + right) // 2
    #         visited = [float('inf')] * len(arr)
    #         visited[0] = 0
    #         if dfs(0, 0):
    #             right = mid
    #         else:
    #             left = mid + 1
    #
    #     return left

    # # TLE 22:33
    # def minJumps(self, arr) -> int:
    #     if len(arr) == 1:
    #         return 0
    #     if arr[0] == arr[-1]:
    #         return 1
    #     index_map = collections.defaultdict(list)
    #     for index, num in enumerate(arr):
    #         index_map[num].append(index)
    #
    #     jumps = [len(arr) - 1] * len(arr)
    #     min_jumps = len(arr) - 1
    #
    #     def dfs(position, steps):
    #         nonlocal min_jumps
    #         if steps > min_jumps:
    #             return
    #         if position == len(arr) - 1:
    #             min_jumps = steps
    #             return
    #         next_positions = set()
    #         for i in index_map[arr[position]]:
    #             if steps + 1 < jumps[i]:
    #                 next_positions.add(i)
    #         if position > 0 and steps + 1 < jumps[position - 1]: next_positions.add(position - 1)
    #         if position < len(arr) - 1 and steps + 1 < jumps[position + 1]: next_positions.add(position + 1)
    #
    #         for next_position in next_positions:
    #             jumps[next_position] = steps + 1
    #             dfs(next_position, steps + 1)
    #
    #     dfs(0, 0)
    #     return min_jumps

    # # Accepted because of del index_map[arr[index]] otherwise TLE
    # def minJumps(self, arr) -> int:
    #     index_map = collections.defaultdict(list)
    #     for index, num in enumerate(arr):
    #         index_map[num].append(index)
    #
    #     jumps = [len(arr) - 1] * len(arr)
    #     jumps[0] = 0
    #     queue = [(0,0)]
    #
    #     while queue:
    #         jump, index = queue.pop(0)
    #         if jump > jumps[index]:
    #             continue
    #         if index == len(arr) - 1:
    #             return jump
    #
    #         next_nodes = set()
    #         if index > 0 and jump + 1 < jumps[index - 1]: next_nodes.add(index - 1)
    #         if index < len(arr) - 1 and jump + 1 < jumps[index + 1]: next_nodes.add(index + 1)
    #         for i in index_map[arr[index]]:
    #             if jump + 1 < jumps[i]:
    #                 next_nodes.add(i)
    #
    #         del index_map[arr[index]]
    #         for i in next_nodes:
    #             jumps[i] = jump + 1
    #             queue.append((jump + 1, i))
    #
    #     return len(arr) - 1


    """
    Revision 2:
    Simple BFS with priority queue on number of steps. You can also call it A* using heuristic. But the star of the show really is the del command.
    There is a case when it has to unnecessarily spend a huge amount of iterations searching in the position which are already visited just to find and check fail if it is visited.
    "del value_position_map[arr[position]]" - hero of the code.
    """
    def minJumps(self, arr) -> int:
        queue = [(0, 0)]
        visited = set()

        value_position_map = collections.defaultdict(set)
        for index, val in enumerate(arr):
            value_position_map[val].add(index)

        while queue:
            steps, position = heapq.heappop(queue)
            if position == len(arr) - 1:
                return steps

            if position + 1 < len(arr) and position + 1 not in visited:
                visited.add(position + 1)
                heapq.heappush(queue, (steps + 1, position + 1))

            if position - 1 >= 0 and position - 1 not in visited:
                visited.add(position - 1)
                heapq.heappush(queue, (steps + 1, position - 1))

            for index in value_position_map[arr[position]]:
                if index not in visited:
                    visited.add(index)
                    heapq.heappush(queue, (steps + 1, index))
            del value_position_map[arr[position]]

        return len(arr) - 1




    # # Bidirectional BFS
    # def minJumps(self, arr) -> int:
    #     n = len(arr)
    #     if n <= 1:
    #         return 0
    #     index_map = collections.defaultdict(list)
    #     for index, num in enumerate(arr):
    #         index_map[num].append(index)
    #
    #     visited = {0, n - 1}
    #     current = [0]
    #     other = [n - 1]
    #
    #     jumps = 0
    #
    #     while current:
    #         if len(other) < len(current):
    #             current, other = other, current
    #
    #         next_nodes = set()
    #         while current:
    #             index = current.pop(0)
    #
    #             for i in [index - 1, index + 1]:
    #                 if 0 <= i < n:
    #                     if i in other:
    #                         return jumps + 1
    #                     if i not in visited:
    #                         visited.add(i)
    #                         next_nodes.add(i)
    #
    #             for i in index_map[arr[index]]:
    #                 if i in other:
    #                     return jumps + 1
    #                 if i not in visited:
    #                     visited.add(i)
    #                     next_nodes.add(i)
    #             del index_map[arr[index]]
    #         current += list(next_nodes)
    #         jumps += 1
    #
    #     return len(arr) - 1


if __name__ == '__main__':
    print(Solution().minJumps(arr=[6, 1, 2, 3, 4, 1, 2, 3, 4, 7])) #5
    print(Solution().minJumps(arr=[100, -23, -23, 404, 100, 23, 23, 23, 3, 404])) #3
    print(Solution().minJumps(arr=[7, 6, 9, 6, 9, 6, 9, 7])) #1
