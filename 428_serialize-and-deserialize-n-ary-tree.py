from collections import deque


# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        decoded = deque(data.split(","))
        if not decoded:
            return None
        node_queue = deque()
        root = Node(int(decoded.pop()), [])
        node_queue.append(root)
        decoded.pop()
        parent_queue = deque([root])
        children_queue = deque()

        while decoded:
            while parent_queue:
                while decoded and decoded[-1] != 'N':
                    new_child = Node(int(decoded.pop()), [])
                    parent_queue[0].children.append(new_child)
                    children_queue.append(new_child)
                decoded.popleft()
                parent_queue.popleft()
            parent_queue = children_queue
            children_queue = deque()

        return root





# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))