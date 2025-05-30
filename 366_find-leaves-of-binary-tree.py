# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root):
        levelArray = []
        def populateArray(root):
            if root is None:
                return 0
            if root.left is None and root.right is None:
                levelArray.append((root.val, 0))
                return 0
            sum1 = populateArray(root.left)
            sum2 = populateArray(root.right)
            levelArray.append((root.val, max(sum1, sum2) + 1))
            return max(sum1, sum2) + 1

        populateArray(root)
        def sortFunc(node):
            return node[1]

        levelArray.sort(key=sortFunc)

        minLevel = levelArray[0][1]
        index = 0
        superArray = []
        subArray = []
        while index < len(levelArray):
            if levelArray[index][1] != minLevel:
                superArray.append(subArray)
                subArray = []
                minLevel = levelArray[index][1]
            subArray.append(levelArray[index][0])
            index+=1
        superArray.append(subArray)
        return superArray





    # def findLeaves(self, root):
    #     stack = []
    #     superArr = []
    #
    #     while root.left is not None or root.right is not None:
    #         myArr = []
    #         stack.append(root)
    #         while len(stack) > 0:
    #             poppedNode = stack.pop()
    #             if poppedNode.left is not None:
    #                 if poppedNode.left.left is None and poppedNode.left.right is None:
    #                     myArr.append(poppedNode.left.val)
    #                     poppedNode.left = None
    #                 else:
    #                     stack.append(poppedNode.left)
    #             if poppedNode.right is not None:
    #                 if poppedNode.right.left is None and poppedNode.right.right is None:
    #                     myArr.append(poppedNode.right.val)
    #                     poppedNode.right = None
    #                 else:
    #                     stack.append(poppedNode.right)
    #         superArr.append(myArr)
    #     superArr.append([root.val])
    #     return superArr



    """
    Revision 2:
    This is a very good question. At first I doubted because I was not able to figure out how I had come up with this solution at the starting of my preparation.
    It turns out that I was not even able to crack the problem then.
    This time atleast I got a solution, but it was wrong.
    My idea was to dfs through the tree and on discovering a leaf node reverse the stack and push each node into it's respective level.
    The trick with this problem is that because a node can occur in many paths and it's level is defined by the reverse order of the path. Same node can have multiple levels.
    Since we delete the leaf node and the proceed upwards, we need to take the max value of the node's level which is nothing but max(left_level, right_level) + 1.
    
    """
    def findLeaves(self, root):
        map_array = collections.defaultdict(list)

        def dfs(node):
            if not node:
                return -1
            current_node_level = max(dfs(node.left), dfs(node.right)) + 1
            map_array[current_node_level].append(node.val)
            return current_node_level

        dfs(root)
        out = []
        for level in sorted(map_array):
            out.append(map_array[level])

        return out




if __name__ == '__main__':
    print(Solution().findLeaves(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(6, TreeNode(7))))))
    # a = {"foo":2, "bar": 1}
    a = [1, 2, 3, 4, 5, 6]
    # print(next(a))
    # print(next(a))
    # print(next(a))
    # print(next(a))
#