# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root, k: int) -> int:
        ans = []

        def traverse(node):
            nonlocal ans
            if not node:
                return
            traverse(node.left)
            ans.append(node)
            traverse(node.right)

        traverse(root)
        return ans[k - 1].val

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
    root = deserialize("[3,1,4,null,2]")
    print(Solution().kthSmallest(root, 3))
    root = deserialize("[5,3,6,2,4,null,null,1]")
    print(Solution().kthSmallest(root, 3))
