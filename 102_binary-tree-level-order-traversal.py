# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import collections


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        q = []
        level_node = collections.defaultdict(list)

        q.append((root, 0))
        while q:
            node, level = q.pop(0)
            level_node[level].append(node.val)
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        return [level_node[i] for i in sorted(level_node)]

if __name__ == '__main__':

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

    print(Solution().levelOrder(deserialize("[3,9,20,null,null,15,7]")))
    print(Solution().levelOrder(deserialize("[1]")))
    print(Solution().levelOrder(deserialize("[]")))
