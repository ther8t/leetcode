# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        if not inorder:
            return None
        current_node = preorder[0]
        inorder_index = -1
        for i in range(len(inorder)):
            if inorder[i] == current_node:
                inorder_index = i
                break
        left_tree = self.buildTree(preorder[1:inorder_index + 1], inorder[:inorder_index])
        right_tree = self.buildTree(preorder[inorder_index + 1:], inorder[inorder_index + 1:])
        return TreeNode(current_node, left_tree, right_tree)


if __name__ == '__main__':
    a = Solution().buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])
    a = Solution().buildTree(preorder = [-1], inorder = [-1])
    print(a)
