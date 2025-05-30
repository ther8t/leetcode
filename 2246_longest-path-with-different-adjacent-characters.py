import collections


class Solution:
    def longestPath(self, parent, s: str) -> int:
        children = collections.defaultdict(list)
        for index, parent_index in enumerate(parent):
            children[parent_index].append(index)

        max_score = 0

        def dfs(node_index):
            nonlocal max_score
            scores = [0, 0]
            for child_node_index in children[node_index]:
                current_score = dfs(child_node_index)
                if s[node_index] != s[child_node_index]:
                    scores.append(current_score)
            scores.sort(reverse=True)
            max_score = max(max_score, scores[0] + scores[1] + 1)
            return max(scores) + 1

        dfs(0)
        return max_score




    # def longestPath(self, parent, s: str) -> int:
    #     n = len(parent)
    #     children = [[0, 0] for _ in range(n)]
    #     non_leaf_nodes = set(parent)
    #     queue = []
    #     visited = set()
    #     for i in range(n - 1, 0, -1):
    #         if i not in non_leaf_nodes:
    #             queue.append(i)
    #             visited.add(i)
    #
    #     while queue:
    #         current_node_index = queue.pop(0)
    #         if current_node_index == 0:
    #             break
    #         current_node_parent_index = parent[current_node_index]
    #         if s[current_node_index] != s[current_node_parent_index]:
    #             a = children[current_node_parent_index]
    #             a.append(max(children[current_node_index]) + 1)
    #             a.sort(reverse=True)
    #             children[current_node_parent_index] = a[:2]
    #         if current_node_parent_index not in visited:
    #             queue.append(current_node_parent_index)
    #             visited.add(current_node_parent_index)
    #
    #     a, b = max(children, key=lambda x: x[0] + x[1] + 1)
    #     return a + b + 1


if __name__ == '__main__':
    print(Solution().longestPath(parent = [-1,0,0,1,1,2], s = "abacbe"))
    print(Solution().longestPath(parent = [-1,0,0,0], s = "aabc"))
    print(Solution().longestPath([-1,137,65,60,73,138,81,17,45,163,145,99,29,162,19,20,132,132,13,60,21,18,155,65,13,163,125,102,96,60,50,101,100,86,162,42,162,94,21,56,45,56,13,23,101,76,57,89,4,161,16,139,29,60,44,127,19,68,71,55,13,36,148,129,75,41,107,91,52,42,93,85,125,89,132,13,141,21,152,21,79,160,130,103,46,65,71,33,129,0,19,148,65,125,41,38,104,115,130,164,138,108,65,31,13,60,29,116,26,58,118,10,138,14,28,91,60,47,2,149,99,28,154,71,96,60,106,79,129,83,42,102,34,41,55,31,154,26,34,127,42,133,113,125,113,13,54,132,13,56,13,42,102,135,130,75,25,80,159,39,29,41,89,85,19], "ajunvefrdrpgxltugqqrwisyfwwtldxjgaxsbbkhvuqeoigqssefoyngykgtthpzvsxgxrqedntvsjcpdnupvqtroxmbpsdwoswxfarnixkvcimzgvrevxnxtkkovwxcjmtgqrrsqyshxbfxptuvqrytctujnzzydhpal"))
