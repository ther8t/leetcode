# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

class Solution:
    def maxLevelSum(self, root) -> int:
        level_sum = collections.defaultdict(int)
        level_sum[0] = -float('inf')
        max_level = 0

        def bfs(node, level):
            nonlocal max_level
            if not node:
                return
            level_sum[level] += node.val
            max_level = max(max_level, level)

            bfs(node.right, level + 1)
            bfs(node.left, level + 1)

        bfs(root, 1)
        score = 0
        for i in range(max_level + 1):
            if level_sum[i] > level_sum[score]:
                score = i

        return score


if __name__ == '__main__':
    t = deserialize("[1,7,0,7,-8,null,null]")
    print(Solution().maxLevelSum(t))
    t = deserialize("[989,null,10250,98693,-89388,null,null,null,-32127]")
    print(Solution().maxLevelSum(t))
    t = deserialize("[1,2,3]")
    print(Solution().maxLevelSum(t))
