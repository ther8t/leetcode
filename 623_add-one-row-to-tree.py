class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


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
    def addOneRow(self, root, val: int, depth: int):
        if depth == 1:
            return TreeNode(val, root)

        def addRow(node, d):
            if not node:
                return
            if d == depth - 1:
                node.left = TreeNode(val, node.left)
                node.right = TreeNode(val, None, node.right)
                return
            addRow(node.left, d + 1)
            addRow(node.right, d + 1)

        addRow(root, 1)
        return root


if __name__ == '__main__':
    print(Solution().addOneRow(deserialize("[4,2,6,3,1,5]"), val = 1, depth = 2))
