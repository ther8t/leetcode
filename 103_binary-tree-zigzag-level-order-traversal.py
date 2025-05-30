# Definition for a binary tree node.
from collections import deque, defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        levels = defaultdict(deque)

        def dfs(node, level):
            if level % 2 == 1:
                levels[level].appendleft(node.val)
            else:
                levels[level].append(node.val)
            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)

        dfs(root, 0)
        ans = []
        for l in range(len(levels)):
            ans.append(list(levels[l]))

        return ans

    # def zigzagLevelOrder(self, root):
    #     if not root:
    #         return []
    #
    #     levels = defaultdict(deque)
    #     queue = [(root, 0)]
    #     while queue:
    #         node, level = queue.pop(0)
    #         if level % 2 == 0:
    #             levels[level].append(node.val)
    #         else:
    #             levels[level].appendleft(node.val)
    #         if node.left:
    #             queue.append((node.left, level + 1))
    #         if node.right:
    #             queue.append((node.right, level + 1))
    #
    #     ans = []
    #     for l in range(len(levels)):
    #         ans.append(list(levels[l]))
    #
    #     return ans

def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root


if __name__ == '__main__':
    print(Solution().zigzagLevelOrder(deserialize("[3,9,20,null,null,15,7]")))
    print(Solution().zigzagLevelOrder(deserialize("[1]")))
    print(Solution().zigzagLevelOrder(None))


