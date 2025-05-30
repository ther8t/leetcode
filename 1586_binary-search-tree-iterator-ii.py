# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    # def __init__(self, root):
    #     visited = set()
    #     arr = []
    #
    #     def inorder(node):
    #         if (not node.left or node.left in visited) and (not node.right or node.right in visited):
    #             visited.add(node)
    #             arr.append(node.val)
    #             return
    #         if node.left:
    #             inorder(node.left)
    #         visited.add(node)
    #         arr.append(node.val)
    #         if node.right:
    #             inorder(node.right)
    #     inorder(root)
    #     self.arr = arr
    #     self.ptr = -1
    #
    # def hasNext(self) -> bool:
    #     return self.ptr < len(self.arr) - 1
    #
    # def next(self) -> int:
    #     if self.hasNext():
    #         self.ptr += 1
    #         return self.arr[self.ptr]
    #     return -1
    #
    # def hasPrev(self) -> bool:
    #     return self.ptr > 0
    #
    # def prev(self) -> int:
    #     if self.ptr > 0:
    #         self.ptr -= 1
    #         return self.arr[self.ptr]
    #     return -1

    def __init__(self, root):
        self.root = root
        self.present = self.left_most(self.root)
        self.present.left = TreeNode(-1)
        self.present = self.present.left

    def left_most(self, node):
        if not node.left and not node.right:
            return node
        if node.left:
            return self.left_most(node.left)
        return node

    def right_most(self, node):
        if not node.left and not node.right:
            return node
        if node.right:
            return self.right_most(node.right)
        return node

    def hasNext(self) -> bool:
        if self.present.right:
            return True
        stack = []
        temp = self.root
        stack.append((self.root, "root"))
        while temp != self.present:
            if self.present.val < temp.val:
                temp = temp.left
                stack.append((temp, "l"))
            else:
                temp = temp.right
                stack.append((temp, "r"))

        while stack and stack[-1][1] != 'l':
            stack.pop()

        if len(stack) > 1:
            return True
        return False

    def next(self) -> int:
        if self.present.right:
            self.present = self.left_most(self.present.right)
            return self.present.val
        stack = []
        temp = self.root
        stack.append((self.root, "root"))
        while temp != self.present:
            if self.present.val < temp.val:
                temp = temp.left
                stack.append((temp, "l"))
            else:
                temp = temp.right
                stack.append((temp, "r"))

        while stack and stack[-1][1] != 'l':
            stack.pop()

        if len(stack) > 1:
            self.present = stack[-2][0]
            return stack[-2][0].val
        return -1

    def hasPrev(self) -> bool:
        if self.present.left and self.present.left.val != -1:
            return True
        stack = []
        temp = self.root
        stack.append((self.root, "root"))
        while temp != self.present:
            if self.present.val < temp.val:
                temp = temp.left
                stack.append((temp, "l"))
            else:
                temp = temp.right
                stack.append((temp, "r"))

        while stack and stack[-1][1] != 'r':
            stack.pop()

        if len(stack) > 1:
            return True
        else:
            return False

    def prev(self) -> int:
        if self.present.left and self.present.left.val != -1:
            self.present = self.right_most(self.present.left)
            return self.present.val
        stack = []
        temp = self.root
        stack.append((self.root, "root"))
        while temp != self.present:
            if self.present.val < temp.val:
                temp = temp.left
                stack.append((temp, "l"))
            else:
                temp = temp.right
                stack.append((temp, "r"))

        while stack and stack[-1][1] != 'r':
            stack.pop()

        if len(stack) > 1:
            self.present = stack[-2][0]
            return stack[-2][0].val
        else:
            if self.root.left and self.root.left.val != -1:
                self.present = self.right_most(self.root)
                return self.present.val
            else:
                return -1


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
    obj = BSTIterator(deserialize("[49,36,null,5,45,0,25,42,46,null,3,15,32,null,44,null,null,null,4,8,null,29,35,null,null,null,null,null,null,null,31]"))
    print(obj.next())
    print(obj.hasPrev())
    print(obj.next())
    print(obj.hasPrev())
    print(obj.prev())
    print(obj.next())
    print(obj.hasPrev())
    print(obj.prev())
    print(obj.hasPrev())
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.hasPrev())
    print(obj.prev())
    print(obj.hasNext())
    print(obj.next())
    print(obj.hasPrev())
    print(obj.prev())
    print(obj.hasPrev())
    print(obj.prev())
    print(obj.next())
    print(obj.hasPrev())
    print(obj.prev())
    print(obj.hasPrev())
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.hasPrev())
    print(obj.prev())
    print(obj.hasPrev())
    print(obj.prev())
    print(obj.hasNext())
    print(obj.next())
