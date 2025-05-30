import collections


class Solution:
    """
    Attempt: Fired
    Accepted: 36%

    Very important concept to be taken care of. A very good, very fundamental question.
    I figured out the concept of a tree not having a loop.
    But I could not figure out the concept of two separate trees.
    [[1, 2],[3, 4]] Two separate trees 1--2 3--4
    """
    def validTree(self, n: int, edges) -> bool:
        visited_node = set()
        neighbours = collections.defaultdict(set)

        for a, b in edges:
            neighbours[a].add(b)
            neighbours[b].add(a)

        h = [0]
        visited_node.add(0)
        while h:
            current_node = h.pop(0)
            for next_node in neighbours[current_node]:
                if next_node in visited_node:
                    return False
                visited_node.add(next_node)
                neighbours[next_node].remove(current_node)
                h.append(next_node)

        return True and len(visited_node) == n


if __name__ == '__main__':
    a = Solution().validTree(n = 5, edges = [[0,1],[0,2],[0,3],[1,4]])
    a = Solution().validTree(n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]])
    a = Solution().validTree(4, [[0,1],[2,3]])
    print(a)
