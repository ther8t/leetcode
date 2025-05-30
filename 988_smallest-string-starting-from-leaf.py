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
    """
    Wrong answer:
    But this is a brilliant problem statement, simple and yet brilliant. There are multiple edge cases in this.
    This attempt returns the string upwards comparing them at their parents. But the problem with this is that "" should not compare to any string for any parent.
    Secondly, if you compare at a parent level and the strings give out an output, the final answer may not be true.
        Compare string ab and abab, means ab wins but if there is z above the current trailing b, means abz comes after ababz
    """
    def smallestFromLeaf(self, root) -> str:
        def dfs(node: TreeNode):
            smallest_string = chr(ord("z") + 1)
            if node.left:
                smallest_string = min(smallest_string, dfs(node.left) + chr(node.val + ord('a')))
            if node.right:
                smallest_string = min(smallest_string, dfs(node.right) + chr(node.val + ord('a')))

            return chr(node.val + ord('a')) if smallest_string == chr(ord("z") + 1) else smallest_string

        return dfs(root)

    def smallestFromLeaf(self, root) -> str:
        smallest_string = chr(ord("z") + 1)

        def dfs(node: TreeNode, s):
            nonlocal smallest_string
            if not node:
                return
            if not node.left and not node.right:
                # The comparison has only to be done at the leaf of the tree.
                smallest_string = min(smallest_string, "".join(reversed(s + chr(node.val + ord('a')))))
                return
            dfs(node.left, s + chr(node.val + ord('a')))
            dfs(node.right, s + chr(node.val + ord('a')))

        dfs(root, "")
        return smallest_string


if __name__ == '__main__':
    print(Solution().smallestFromLeaf(deserialize("[4,0,1,1]")))
    print(Solution().smallestFromLeaf(deserialize("[0,1,2,3,4,3,4]")))
    print(Solution().smallestFromLeaf(deserialize("[25,1,3,1,3,0,2]")))
    print(Solution().smallestFromLeaf(deserialize("[2,2,1,null,1,0,null,0]")))
    print(Solution().smallestFromLeaf(deserialize("[25,1,null,0,0,1,null,null,null,0]")))
