# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deserialize(self, tree, index=0):
        if index >= len(tree):
            return None
        if tree[index] is None:
            return None
        my_node = TreeNode(tree[index])
        left_child = self.deserialize(tree, 2 * index + 1)
        right_child = self.deserialize(tree, 2 * index + 2)
        if left_child:
            my_node.left = left_child
        if right_child:
            my_node.right = right_child

        return my_node

    def serialize(self, root, queue=None):
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

    # def search_tree_for_child(self, root, search_val):
    #     if not root:
    #         return None
    #     # if root.val == search_val:
    #     #     return root
    #     if root.left and root.left.val == search_val:
    #         return root
    #     if root.right and root.right.val == search_val:
    #         return root
    #     result = self.search_tree_for_child(root.left, search_val)
    #     if result:
    #         return result
    #     return self.search_tree_for_child(root.right, search_val)
    #
    # def remaining_tree(self, root, to_delete):
    #     if root is None:
    #         return []
    #
    #     left_remaining_trees = self.remaining_tree(root.left, to_delete)
    #     right_remaining_trees = self.remaining_tree(root.right, to_delete)
    #
    #     trees = []
    #     if root.left and root.left.val in to_delete:
    #         if root.left.left:
    #             trees.append(root.left.left)
    #         if root.left.right:
    #             trees.append(root.left.right)
    #         root.left = None
    #     if root.right and root.right.val in to_delete:
    #         if root.right.left:
    #             trees.append(root.right.left)
    #         if root.right.right:
    #             trees.append(root.right.right)
    #         root.right = None
    #
    #     return left_remaining_trees + trees + right_remaining_trees
    #
    # def delNodes(self, root, to_delete):
    #     dummy_node = TreeNode(-1)
    #     dummy_node.left = root
    #     trees = self.remaining_tree(dummy_node, set(to_delete))
    #     if dummy_node.left:
    #         trees.append(root)
    #     return trees


    """
    Revision 2:
    This was supposed to be easy, but I did it some other way in the first iteration.
    There were a couple of problems with the second iteration as well. Take care of it the next time.
    1. We need to settle the subtrees before we settle a node. There is a case where we add the child node of a deleted node as independent node and that child node is also supposed to be deleted. That node should not exist in the out array but it ends up being there.
    2. Since root is the starting point and all nodes which are added to out must be added through their parents, on their parent being deleted, root is not privy to such a thing because it doesnt have a parent.
       So if root is not in the to_delete list, it cannot be added. 
    """
    def delNodes(self, root, to_delete):
        to_delete = set(to_delete)
        out = []

        def dfs(node, parent):
            if not node:
                return
            dfs(node.left, node)
            dfs(node.right, node)
            if node.val in to_delete:
                if parent and parent.left and parent.left == node:
                    parent.left = None
                elif parent and parent.right and parent.right == node:
                    parent.right = None

                if node.left:
                    out.append(node.left)
                if node.right:
                    out.append(node.right)

        dfs(root, None)
        if root.val not in to_delete:
            out.append(root)
        return out


    # # not my code but good code this is basically dfs, not deleting actually but only appending the children of the one's who are being deleted.
    # def delNodes(self, root, to_delete):
    #
    #     res = set()
    #
    #     to_delete = set(to_delete)
    #
    #     def helper(root):
    #         nonlocal res
    #         if not root:
    #             return None
    #         if root.val in to_delete:
    #             if root in res:  # if in res, correct previous assumption
    #                 res.remove(root)
    #             if root.left:
    #                 res.add(root.left)  # add children-->assume not in to_delete
    #                 helper(
    #                     root.left)  # do not assign result to anything: no parent after delete! Just modify object in res array
    #             if root.right:
    #                 res.add(root.right)
    #                 helper(root.right)
    #             return None  # return None: to be assigned to left/right child
    #         else:
    #             # leaves root in res array and modifies children
    #             root.left = helper(root.left)
    #             root.right = helper(root.right)
    #             return root
    #
    #     res.add(root)
    #     helper(root)
    #     return list(res)

    # # 5%
    # def delNodes(self, root, to_delete):
    #     trees = [root]
    #     for index, to_delete_node_val in enumerate(to_delete):
    #         for tree_root in trees:
    #             if tree_root.val == to_delete_node_val:
    #                 if tree_root.left:
    #                     trees.append(tree_root.left)
    #                 if tree_root.right:
    #                     trees.append(tree_root.right)
    #                 trees.remove(tree_root)
    #             search_result = self.search_tree_for_child(tree_root, to_delete_node_val)
    #             if search_result:
    #                 to_delete_node = search_result
    #                 if search_result.left and search_result.left.val == to_delete_node_val:
    #                     to_delete_node = search_result.left
    #                     search_result.left = None
    #                 elif search_result.right and search_result.right.val == to_delete_node_val:
    #                     to_delete_node = search_result.right
    #                     search_result.right = None
    #                 if to_delete_node.left:
    #                     trees.append(to_delete_node.left)
    #                 if to_delete_node.right:
    #                     trees.append(to_delete_node.right)
    #                 break
    #     return trees


if __name__ == '__main__':
    a = Solution().deserialize([1, 2, 3, 4, 5, 6, 7])
    b = Solution().delNodes(a, [5, 3])
    for i in b:
        print(Solution().serialize(i))
