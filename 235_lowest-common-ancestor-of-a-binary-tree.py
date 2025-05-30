# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None

        def dfs(node):
            nonlocal ans
            if not node:
                return False
            current = node == p or node == q
            left = dfs(node.left)
            right = dfs(node.right)
            if current + left + right >= 2:
                ans = node
                return True
            return current or left or right

        dfs(root)
        return ans


    """
    Revision 2:
    This is a much cleaner and simpler method to understand and solve the problem.
    If the required node is found in the subarray it returns that node.
    If a node's left and right children return the finding, node is returned.
    
    Accepted : 98%
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return None
            left = dfs(node.left)
            right = dfs(node.right)
            if left and right:
                return node
            if node == p or node == q:
                return node
            return left or right

        return dfs(root)

    # Accepted : 36%
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return None
            l, r = dfs(node.left), dfs(node.right)
            if l and r:
                return node
            if node == p or node == q:
                return node
            return l or r

        return dfs(root)


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
    r = deserialize("[3,5,1,6,2,0,8,null,null,7,4]")
    print(Solution().lowestCommonAncestor(r, r.left, r.left.right.right).val)
