# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def treeQueries(self, root, queries):
        parent, height, value = collections.defaultdict(TreeNode), collections.defaultdict(int), collections.defaultdict(TreeNode)

        def dfs(node):
            if not node:
                return 0
            value[node.val] = node
            if not node.left and not node.right:
                return 0
            if node.left:
                parent[node.left] = node
            if node.right:
                parent[node.right] = node
            height[node] = max(dfs(node.left), dfs(node.right)) + 1
            return height[node]

        dfs(root)
        parent[root] = None
        height[None] = -1

        def get_updated_height(node, updated_height):
            parent_node = parent[node]
            if not parent_node:
                return updated_height
            parent_updated_height = 0
            for child_node in [parent_node.left, parent_node.right]:
                parent_updated_height = max(parent_updated_height, height[child_node] + 1 if not child_node or child_node != node else updated_height + 1)
            return get_updated_height(parent_node, parent_updated_height)


        ans = []
        for node_value in queries:
            node = value[node_value]
            ans.append(get_updated_height(node, -1))

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
    print(Solution().treeQueries(root = deserialize("[1,3,4,2,null,6,5,null,null,null,null,null,7]"), queries = [4]))
    print(Solution().treeQueries(root = deserialize("[5,8,9,2,1,3,7,4,6]"), queries = [3,2,4,8]))
    print(Solution().treeQueries(root = deserialize("[1,null,5,3,null,2,4]"), queries = [3,5,4,2,4]))
