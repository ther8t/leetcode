# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deserialize(self, string):
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

    def maxPathSum(self, root) -> int:
        ans = -float('inf')
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            left_max = dfs(node.left)
            right_max = dfs(node.right)
            ans = max(ans, left_max + right_max + node.val, node.val, node.val + left_max, node.val + right_max)
            return max(left_max + node.val, right_max + node.val, node.val)

        dfs(root)
        return ans


if __name__ == '__main__':
    print(Solution().maxPathSum(
        Solution().deserialize('[1,2,3]')))
    print(Solution().maxPathSum(
        Solution().deserialize('[-10,9,20,null,null,15,7]')))
    print(Solution().maxPathSum(
        Solution().deserialize('[9,6,-3,null,null,-6,2,null,null,2,null,-6,-6,-6]')))
