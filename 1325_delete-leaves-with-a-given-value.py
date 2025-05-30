# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root, target: int):
        def dfs(node, parent):
            if not node:
                return
            dfs(node.left, node)
            dfs(node.right, node)
            if not node.left and not node.right and node.val == target:
                if parent and parent.left and parent.left == node:
                    parent.left = None
                if parent and parent.right and parent.right == node:
                    parent.right = None
            return node
        a = dfs(root, None)
        return None if not a.left and not a.right and a.val == target else a


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

    a = Solution().removeLeafNodes(deserialize("[1,2,3,2,null,2,4]"), 2)
    # a = Solution().removeLeafNodes(deserialize("[1,1,1]"), 1)
    print(a)
