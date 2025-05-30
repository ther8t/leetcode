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
    def sumNumbers(self, root) -> int:
        ans = 0

        def dfs(node, num):
            nonlocal ans
            if not node.left and not node.right:
                ans += int(num + str(node.val))
                return
            if node.left:
                dfs(node.left, num + str(node.val))
            if node.right:
                dfs(node.right, num + str(node.val))

        dfs(root, "")
        return ans


if __name__ == '__main__':
    print(Solution().sumNumbers(deserialize("[1,2,3]")))
    print(Solution().sumNumbers(deserialize("[4,9,0,5,1]")))
