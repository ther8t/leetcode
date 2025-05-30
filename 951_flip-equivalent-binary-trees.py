# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
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

    def flipEquiv(self, root1, root2) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False
        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or (
                    self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))


if __name__ == '__main__':
    print(Solution().flipEquiv(Solution().deserialize('[1,2,3,4,5,6,null,null,null,7,8]'),
                               Solution().deserialize('[1,3,2,null,6,4,5,null,null,null,null,8,7]')))
