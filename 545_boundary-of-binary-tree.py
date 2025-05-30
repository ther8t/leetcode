# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
    def boundaryOfBinaryTree(self, root):
        left, right, leaves = [], [], []

        def get_left(n):
            if not n:
                return
            left.append(n.val)
            if n.left:
                get_left(n.left)
            elif n.right:
                get_left(n.right)

        def get_right(n):
            if not n:
                return
            right.append(n.val)
            if n.right:
                get_right(n.right)
            elif n.left:
                get_right(n.left)

        def get_leaves(n):
            if not n:
                return
            if not n.left and not n.right:
                leaves.append(n.val)
            get_leaves(n.left)
            get_leaves(n.right)

        if root.left:
            get_left(root)
        if root.left or root.right:
            get_leaves(root)
        if root.right:
            get_right(root)

        return [root.val] + left[1:-1] + leaves + list(reversed(right[1:-1]))


if __name__ == '__main__':
    print(Solution().boundaryOfBinaryTree(deserialize("[1]")))
    print(Solution().boundaryOfBinaryTree(deserialize("[1,null,2,3,4]")))
    print(Solution().boundaryOfBinaryTree(deserialize("[1,2,3,4,5,6,null,null,null,7,8,9,10]")))
