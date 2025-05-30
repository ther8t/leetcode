# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Revision 2:
    It is indeed a real shame that I was not able to solve this even the second time.
    I would do this again.
    I have written it again so I remember. This indeed was my cup of tea question.
    """
    def findDuplicateSubtrees(self, root):
        path_map = collections.defaultdict(TreeNode)
        out = set()

        def traversal(node):
            if not node:
                return "N"
            left_sub_tree = traversal(node.left)
            right_sub_tree = traversal(node.right)
            current_path = "(" + left_sub_tree + ")" + "(" + str(node.val) + ")" + "(" + right_sub_tree + ")"
            if current_path in path_map:
                out.add(path_map[current_path])
            else:
                path_map[current_path] = node
            return current_path

        traversal(root)
        return list(out)



    # def findDuplicateSubtrees(self, root):
    #     path_map = collections.defaultdict(int)
    #     duplicate_subtree_roots = []
    #
    #     def traversal(node):
    #         if not node:
    #             return ""
    #         left_path = traversal(node.left)
    #         right_path = traversal(node.right)
    #         my_subtree_path = ("l" + left_path) + "," + str(node.val) + "," + ("r" + right_path)
    #         if my_subtree_path in path_map.keys() and path_map[my_subtree_path] == 1:
    #             duplicate_subtree_roots.append(node)
    #         path_map[my_subtree_path]+=1
    #         return my_subtree_path
    #     traversal(root)
    #     return duplicate_subtree_roots

    # Wrong Answer : It's a shame that I was not able to solve this. This is classic my cup of tea problem statement. Recursion + ds
    # def findDuplicateSubtrees(self, root):
    #     duplicate_subtree_roots = set()
    #
    #     def compare(node1, node2, strict):
    #         if not node1 and not node2:
    #             return True
    #         if node1 and node2 and node1.val == node2.val:
    #             left_compare = compare(node1.left, node2.left, strict)
    #             right_compare = compare(node1.right, node2.right, strict)
    #             if left_compare and right_compare:
    #                 return True
    #         if not strict and node2:
    #             left_compare = compare(node1, node2.left, strict)
    #             if left_compare:
    #                 return True
    #             right_compare = compare(node1, node2.right, strict)
    #             if right_compare:
    #                 return True
    #         return False
    #
    #     def iterate(stack, root):
    #         if not root:
    #             return
    #         right_node = root.right
    #         left_node = root.left
    #         left_right_compare = compare(left_node, right_node, False)
    #         if left_node and right_node and left_right_compare:
    #             duplicate_subtree_roots.add(left_node)
    #             stack.append(right_node)
    #
    #         if not left_right_compare and right_node:
    #             for node in stack:
    #                 right_compare = compare(right_node, node, False)
    #                 if right_compare:
    #                     duplicate_subtree_roots.add(right_node)
    #                     break
    #             stack.append(right_node)
    #
    #         if not left_right_compare and left_node:
    #             for node in stack:
    #                 left_compare = compare(left_node, node, False)
    #                 if left_compare:
    #                     duplicate_subtree_roots.add(left_node)
    #                     break
    #         iterate(stack, root.left)
    #     iterate([], root)
    #     return list(duplicate_subtree_roots)

    # def findDuplicateSubtrees(self, root):
    #     duplicate_subtree_roots = set()
    #
    #     def compare_all(node1, node2):
    #         compare(node1, node2)
    #         if node2:
    #             compare(node1, node2.left)
    #             compare(node1, node2.right)
    #
    #     def compare(node1, node2):
    #         if not node1 and not node2:
    #             return True
    #         if node1 and node2 and node1.val == node2.val:
    #             left_compare = compare(node1.left, node2.left)
    #             right_compare = compare(node1.right, node2.right)
    #             if left_compare and right_compare:
    #                 return True
    #         return False
    #
    #     def iterate(stack, root):
    #         if not root:
    #             return
    #         right_node = root.right
    #         if right_node:
    #             for node in stack:
    #                 right_compare = compare(right_node, node)
    #                 if right_compare:
    #                     duplicate_subtree_roots.add(right_node)
    #
    #             left_right_compare = compare(root.left, right_node)
    #             if not left_right_compare:
    #                 stack.append(right_node)
    #
    #         left_node = root.left
    #         if left_node:
    #             for node in stack:
    #                 left_compare = compare(left_node, node)
    #                 if left_compare:
    #                     duplicate_subtree_roots.add(left_node)
    #         iterate(stack, root.left)
    #     iterate([], root)
    #     return list(duplicate_subtree_roots)


    # # Wrong Answer : i failed to recognise that a node whose all descendants compare and have popped out in previous iteration would be different from the one who is a leaf node.
    # # A leaf node would be accepted but such a node would not be.
    # def findDuplicateSubtrees(self, root):
    #     all_paths = []
    #     similar_path_nodes = []
    #
    #     def dfs(stack, node, side):
    #         if not node:
    #             return
    #         stack.append((node, side))
    #         if node and not node.left and not node.right:
    #             path = stack.copy()
    #             path.reverse()
    #             all_paths.append(path)
    #         if node.left:
    #             dfs(stack, node.left, "L")
    #         if node.right:
    #             dfs(stack, node.right, "R")
    #         stack.pop()
    #
    #     def sort_split_compare(paths):
    #         if len(paths) == 0:
    #             return
    #         ptrl = 0
    #         ptrr = 0
    #
    #         # sort on the basis of the first index
    #         paths.sort(key=lambda x: x[0][0].val if x and len(x) > 0 else float('inf'))
    #         delete_paths = []
    #         while ptrl < len(paths):
    #             if len(paths[ptrl]) == 0:
    #                 continue
    #             while (ptrr < len(paths) and len(paths[ptrr]) > 0 and paths[ptrl][0][0].val == paths[ptrr][0][0].val) and \
    #                     ((paths[ptrl][0][1] == paths[ptrr][0][1]) or
    #                      (len(paths[ptrl])==2 or len(paths[ptrr])==2) or
    #                      (len(paths[ptrl])>1 and len(paths[ptrr])>1 and (paths[ptrl][1][0].val!=paths[ptrr][1][0].val or paths[ptrl][1][1]!=paths[ptrr][1][1]))):
    #                 ptrr += 1
    #             if ptrr - ptrl >= 2:
    #                 similar_path_nodes.append(paths[ptrl][0][0])
    #                 for i in range(ptrl, ptrr):
    #                     paths[i].pop(0)
    #                     if len(paths[i]) == 1: delete_paths.append(paths[i])
    #             else:
    #                 delete_paths.append(paths[ptrl])
    #             ptrl = ptrr
    #
    #         for i in delete_paths:
    #             paths.remove(i)
    #
    #         return sort_split_compare(paths)
    #
    #     dfs([], root, "Ro")
    #     sort_split_compare(all_paths)
    #
    #     return similar_path_nodes

    def deserialize(self, string):
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
    # a = (Solution().findDuplicateSubtrees(Solution().deserialize('[2,1,1]')))
    a = (Solution().findDuplicateSubtrees(Solution().deserialize('[1,2,3,4,null,2,4,null,null,4]')))
    # a = (Solution().findDuplicateSubtrees(Solution().deserialize('[0,0,0,0,null,null,0,null,null,0,0]')))
    # a = (Solution().findDuplicateSubtrees(Solution().deserialize('[0,0,0,0,null,null,0,null,null,null,0]')))
    # a = (Solution().findDuplicateSubtrees(Solution().deserialize('[0,0,0,0,null,null,0,0,0,0,0]')))
    print(a)
