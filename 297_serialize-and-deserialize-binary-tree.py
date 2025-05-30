# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        queue = [root]
        out = []

        while queue:
            popped = queue.pop(0)
            if popped:
                out.append(str(popped.val))
                queue.append(popped.left)
                queue.append(popped.right)
            else:
                out.append("None")
        return ",".join(out)


    """
    Revision 2:
    I had read and reproduced this algo, which I got off leetcode for seriealizing and deserializing a binary tree.
    This is although a similar algo to children being at 2*n + 1 and 2*n + 2 but is more cleaner.
    The idea is to pop the list and append to the current element in another list. The children would be available in sequence only.
    """
    def deserialize(self, data):
        data = data.split(",")
        for i in range(len(data)):
            if data[i] == 'None':
                data[i] = None
            else:
                data[i] = TreeNode(data[i])

        data_reverse = data[::-1]
        data_reverse.pop()

        for node in data:
            if node:
                if data_reverse: node.left = data_reverse.pop()
                if data_reverse: node.right = data_reverse.pop()

        return data[0]

    # def deserialize(self, data):
    #     """Decodes your encoded data to tree.
    #
    #     :type data: str
    #     :rtype: TreeNode
    #     """
    #     data = data.split(",")
    #     n = len(data)
    #     children_pointer = 0
    #
    #     if not data or data[0] == "None":
    #         return None
    #     else:
    #         data[0] = TreeNode(data[0])
    #     for i in range(n):
    #         if not data[i] or data[i] == "None":
    #             continue
    #         for j in [children_pointer + 1, children_pointer + 2]:
    #             if j < n:
    #                 if data[j] == "None":
    #                     data[j] = None
    #                 else:
    #                     data[j] = TreeNode(data[j])
    #         if children_pointer + 1 < n:
    #             data[i].left = data[children_pointer + 1]
    #         if children_pointer + 2 < n:
    #             data[i].right = data[children_pointer + 2]
    #         children_pointer += 2
    #
    #     return data[0]


# Your Codec object will be instantiated and called as such:
root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4, TreeNode(6), TreeNode(7)), TreeNode(5)))
# root = None
ser = Codec()
deser = Codec()
print(ser.serialize(root))
ans = deser.deserialize(ser.serialize(root))
print(ans)