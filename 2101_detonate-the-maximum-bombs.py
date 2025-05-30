import collections


class Solution:
    """
    This one is the standard case of me overthinking. Perhaps I should lay off the coffee. For some reason DFS at every node wasn't good enough for me.
    😭 Alas!! that was the solution.
    """
    def maximumDetonation(self, bombs) -> int:
        n = len(bombs)
        size = [-1] * n
        bomb_index_range_index_map = collections.defaultdict(list)

        for index, (x, y, r) in enumerate(bombs):
            for j, (a, b, r2) in enumerate(bombs):
                if (x - a) * (x - a) + (y - b) * (y - b) - r * r <= 0:
                    bomb_index_range_index_map[index].append(j)

        def dfs(index):
            sub_nodes = 0
            for child_index in bomb_index_range_index_map[index]:
                if child_index in visited:
                    continue
                visited.add(child_index)
                sub_nodes += dfs(child_index)
            return sub_nodes + 1

        for i in range(n):
            visited = set()
            visited.add(i)
            size[i] = dfs(i)

        return max(size)


if __name__ == '__main__':
    print(Solution().maximumDetonation(bombs = [[2,1,3],[6,1,4]]))
    print(Solution().maximumDetonation(bombs = [[1,1,5],[10,10,5]]))
    print(Solution().maximumDetonation(bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]))
