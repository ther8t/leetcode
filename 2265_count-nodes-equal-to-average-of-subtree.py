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

def serialize(root, queue=None):
    if root is None:
        return []
    serialized = []
    if queue is None:
        queue = [root]

    while len(queue) > 0:
        popped = queue.pop(0)
        if popped:
            serialized.append(popped.val)
            if popped.left or popped.right:
                queue.append(popped.left)
                queue.append(popped.right)
        else:
            serialized += "N"
    return serialized


class Solution:
    def averageOfSubtree(self, root) -> int:
        ans = 0

        def getSumCount(node):
            nonlocal ans
            if node is None:
                return 0, 0
            left_sum, left_count = getSumCount(node.left)
            right_sum, right_count = getSumCount(node.right)

            if (node.val + left_sum + right_sum) // (left_count + right_count + 1) == node.val:
                ans += 1
            return node.val + left_sum + right_sum, (left_count + right_count + 1)

        getSumCount(root)
        return ans


if __name__ == '__main__':
    print(Solution().averageOfSubtree(deserialize('[4,8,5,0,1,null,6]')))
    print(Solution().averageOfSubtree(deserialize('[1]')))
