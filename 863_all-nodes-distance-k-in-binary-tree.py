# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
    Revision 2:
    This is another way of solving the question. There is no direct need to calculate ancestory for all nodes.
    For this we just need the path to the node. We use stack and DFS to get that.
    After we have the path, all we need to do is to search down the nodes. Two things we need to take care of.
    Distance : Each node up in the hierarchy would need to traverse lesser and lesser distance because of it's distance from the target node.
    Visited : A node just be a distance of 2 from itself if we don't mark the distance. 1 up + 1 down = 2, But we need to avoid this sort of situations, so we mark all the nodes visited during search.
    """
    def distanceK(self, root, target, k: int):
        stack = [root]

        def dfs(node):
            nonlocal stack
            if not node:
                return
            if node == target:
                return True
            if node.left:
                stack.append(node.left)
                if dfs(node.left):
                    return True
                stack.pop()

            if node.right:
                stack.append(node.right)
                if dfs(node.right):
                    return True
                stack.pop()
            return False

        dfs(root)

        def search(node, distance):
            if distance < 0:
                return []
            if distance == 0:
                return [node.val]
            out = []
            if node.left and node.left not in visited:
                visited.add(node.left)
                out += search(node.left, distance - 1)
            if node.right and node.right not in visited:
                visited.add(node.right)
                out += search(node.right, distance - 1)
            return out

        visited = set()
        out = []
        for index, node in enumerate(reversed(stack)):
            if k - index < 0:
                break
            visited.add(node)
            out += search(node, k - index)

        return out








    # def distanceK(self, root, target, k: int):
    #     ancestor = {}
    #     ancestor[root] = None
    #
    #     def traverse(root):
    #         if root.left:
    #             ancestor[root.left] = root
    #             traverse(root.left)
    #         if root.right:
    #             ancestor[root.right] = root
    #             traverse(root.right)
    #
    #     traverse(root)
    #
    #     queue = [(0, target)]
    #     visited = set()
    #     visited.add(target)
    #     out = []
    #     while queue:
    #         distance, node = queue.pop(0)
    #         if distance == k:
    #             out.append(node.val)
    #
    #         if ancestor[node] and ancestor[node] not in visited:
    #             if distance + 1 == k:
    #                 out.append(ancestor[node].val)
    #             elif distance + 1 < k:
    #                 visited.add(ancestor[node])
    #                 queue.append((distance + 1, ancestor[node]))
    #
    #         if node.left and node.left not in visited:
    #             if distance + 1 == k:
    #                 out.append(node.left.val)
    #             elif distance + 1 < k:
    #                 visited.add(node.left)
    #                 queue.append((distance + 1, node.left))
    #
    #         if node.right and node.right not in visited:
    #             if distance + 1 == k:
    #                 out.append(node.right.val)
    #             elif distance + 1 < k:
    #                 visited.add(node.right)
    #                 queue.append((distance + 1, node.right))
    #
    #     return out


if __name__ == '__main__':
    t = deserialize("[3,5,1,6,2,0,8,null,null,7,4]")
    a = Solution().distanceK(t, t.left, 2)
    print(a)
