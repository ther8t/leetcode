# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root) -> bool:

        def dfs(node, mini, maxi):
            if not node:
                return True
            if node.val <= mini or node.val >= maxi:
                return False
            l = dfs(node.left, max(mini, -float('inf')), node.val)
            r = dfs(node.right, node.val, min(maxi, float('inf')))
            return l and r

        return dfs(root, -float('inf'), float('inf'))


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

    print(Solution().isValidBST(deserialize("[5,4,6,null,null,3,7]")))
    print(Solution().isValidBST(deserialize("[2,1,3]")))
    print(Solution().isValidBST(deserialize("[2,2,2]")))
