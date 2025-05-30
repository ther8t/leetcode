# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root) -> int:
        node_score_map = {}

        def dfs(node):
            if not node:
                return 0
            score = node.val - 1 + dfs(node.right) + dfs(node.left)
            node_score_map[node] = score
            return score

        dfs(root)
        ans = 0
        for i in node_score_map:
            ans += abs(node_score_map[i])

        return ans

    def distributeCoins(self, root) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            l, r = dfs(node.left), dfs(node.right)
            ans += abs(l) + abs(r)
            return l + r + node.val - 1

        dfs(root)
        return ans



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
    print(Solution().distributeCoins(deserialize("[3,0,0]")))
    print(Solution().distributeCoins(deserialize("[0,3,0]")))
    print(Solution().distributeCoins(deserialize("[4,0,null,null,0,null,0]")))
    print(Solution().distributeCoins(deserialize("[1,0,0,null,3]")))
