# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else Node(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                kid = kids.pop()
                if kid:
                    kid.parent = node
                node.left = kid
            if kids:
                kid = kids.pop()
                if kid:
                    kid.parent = node
                node.right = kid
    return root

class Solution:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        current = leaf
        original_parent = leaf.parent
        while current != root:
            if current.left:
                current.right = current.left
                current.left = None
            current.left = original_parent
            next_current = original_parent
            next_original_parent = original_parent.parent
            if current.parent.left == current:
                current.parent.left = None
            if current.parent.right == current:
                current.parent.right = None
            original_parent.parent = current
            current = next_current
            original_parent = next_original_parent

        leaf.parent = None

        return leaf



if __name__ == '__main__':
    t = deserialize("[3,5,1,6,2,0,8,null,null,7,4]")
    print(Solution().flipBinaryTree(root = t, leaf = t.left.right.left))
