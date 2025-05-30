# Definition for a binary tree node.
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
    def printTree(self, root):
        def getHeight(node):
            if not node:
                return 0
            return max(getHeight(node.left), getHeight(node.right)) + 1

        tree_height = getHeight(root)
        a = [["" for _ in range(2 ** tree_height - 1)] for _ in range(tree_height)]

        def populate(node, lo, hi, height):
            if not node:
                return
            span = hi - lo + 1
            a[height][lo + span // 2] = str(node.val)
            populate(node.left, lo, lo + span // 2 - 1, height + 1)
            populate(node.right, lo + span // 2 + 1, hi, height + 1)

        populate(root, 0, 2 ** tree_height - 2, 0)
        return a


if __name__ == '__main__':
    t = deserialize("[1,2,3,null,4]")
    print(Solution().printTree(t))
    t = deserialize("[1,2]")
    print(Solution().printTree(t))
