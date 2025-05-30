import collections


class Solution:
    """
    Attempt #2
    Accepted 97%
    """
    def longestCycle(self, edges: list) -> int:
        n = len(edges)
        global_visited = set()
        max_len = -1

        for i in range(n):
            if i in global_visited:
                continue
            counter = 0
            local_visited = {}
            while i not in global_visited:
                local_visited[i] = counter
                global_visited.add(i)
                i = edges[i]
                counter += 1
                if i == -1:
                    break
                if i in local_visited:
                    max_len = max(max_len, counter - local_visited[i])
        return max_len


if __name__ == '__main__':
    print(Solution().longestCycle([3,3,4,2,3]))
    print(Solution().longestCycle([-1,4,-1,2,0,4]))
    print(Solution().longestCycle(edges = [2,-1,3,1]))
