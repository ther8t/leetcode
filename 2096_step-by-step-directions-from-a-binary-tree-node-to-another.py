# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(self, root, startValue, destValue):
        def detectDirection(node, myDirection):
            if node is None:
                return "", False, False
            leftDirections, startFoundLeft, destFoundLeft = detectDirection(node.left, "L")
            rightDirections, startFoundRight, destFoundRight = detectDirection(node.right, "R")

            childTreeHasStartNode = startFoundRight or startFoundLeft
            childTreeHasDestNode = destFoundRight or destFoundLeft
            if childTreeHasStartNode and childTreeHasDestNode:
                # found both nodes in my child trees
                if startFoundLeft:
                    return leftDirections + rightDirections, True, True
                else:
                    return rightDirections + leftDirections, True, True

            if node.val == startValue:
                if childTreeHasDestNode:
                    return leftDirections + rightDirections, True, True
                else:
                    return "U", True, False

            if node.val == destValue:
                if childTreeHasStartNode:
                    return leftDirections + rightDirections, True, True
                else:
                    return myDirection, False, True

            if childTreeHasStartNode:
                return "U" + leftDirections + rightDirections, True, False

            if childTreeHasDestNode:
                return myDirection + leftDirections + rightDirections, False, True

            return "", False, False

        return detectDirection(root, "")[0]


    # MLE
    # def getDirections(self, root, startValue, destValue):
    #     ancestry = {}
    #
    #     def populateAncestry(node, nodesAncestry, direction):
    #         if node is None:
    #             return
    #         ancestry[node.val] = (nodesAncestry + [(node.val, direction)])
    #         populateAncestry(node.left, ancestry[node.val], "L")
    #         populateAncestry(node.right, ancestry[node.val], "R")
    #
    #     populateAncestry(root, [], "")
    #
    #     ancestryStart = ancestry[startValue]
    #     ancestryDest = ancestry[destValue]
    #
    #     firstCommonAncestryIndex = -1
    #     for i in range(min(len(ancestryStart), len(ancestryDest))):
    #         if ancestryStart[i][0] == ancestryDest[i][0]:
    #             firstCommonAncestryIndex += 1
    #         else:
    #             break
    #
    #     path = ""
    #     for i in range(len(ancestryStart) - 1, firstCommonAncestryIndex, -1):
    #         path += "U"
    #     for i in range(firstCommonAncestryIndex + 1, len(ancestryDest)):
    #         path += ancestryDest[i][1]
    #     return path

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

    """
    Revision 2: 
    This is a bit of a surprise. The solution I had thought would not be memory expensive turned out to exceed the Memory Limit.
    Turns out. AHHHHH!!!!
    Turns out the original method I had tried to solve it with is so good that the solution gets accepted by 99.94%.
    The idea is the same about comparing two paths, to the source path and destination.
    """
    def getDirections(self, root, startValue, destValue):
        def dfs(node, target, stack):
            if not node:
                return None
            if node.val == target:
                return []
            if node.left:
                if dfs(node.left, target, stack) is not None:
                    stack.appendleft("L")
                    return stack
            if node.right:
                if dfs(node.right, target, stack) is not None:
                    stack.appendleft("R")
                    return stack

        start_ancestry = dfs(root, startValue, collections.deque())
        dest_ancestry = dfs(root, destValue, collections.deque())

        while start_ancestry and dest_ancestry and start_ancestry[0] == dest_ancestry[0]:
            start_ancestry.popleft()
            dest_ancestry.popleft()

        return "U" * (len(start_ancestry)) + "".join(dest_ancestry)


if __name__ == '__main__':
    print(Solution().getDirections(
        Solution().deserialize('[2,1]'), 2, 1)) # L
    print(Solution().getDirections(
        Solution().deserialize('[2,8,9,7,5,1,6,null,null,null,null,null,4,null,3]'), 9, 3)) # RR
    print(Solution().getDirections(
        Solution().deserialize('[5,1,2,3,null,6,4]'), 3, 6)) #UURL
    print(Solution().getDirections(
        Solution().deserialize('[3,1,2]'), 2, 1)) # UL
    print(Solution().getDirections(
        Solution().deserialize('[1,null,10,12,13,4,6,null,15,null,null,5,11,null,2,14,7,null,8,null,null,null,9,3]'), 6, 15)) #UURR

