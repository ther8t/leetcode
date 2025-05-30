
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid):

        def form_tree(start_row, end_row, start_col, end_col):
            if end_row - start_row == 1:
                return Node(bool(grid[start_row][start_col]), True, None, None, None, None)
            mid_row = (start_row + end_row) // 2
            mid_col = (start_col + end_col) // 2
            top_left = form_tree(start_row, mid_row, start_col, mid_col)
            top_right = form_tree(start_row, mid_row, mid_col, end_col)
            bottom_left = form_tree(mid_row, end_row, start_col, mid_col)
            bottom_right = form_tree(mid_row, end_row, mid_col, end_col)

            if top_left.isLeaf and top_right.isLeaf and bottom_left.isLeaf and bottom_right.isLeaf and top_left.val == top_right.val == bottom_left.val == bottom_right.val:
                return Node(top_left.val, True, None, None, None, None)
            else:
                return Node(False, False, top_left, top_right, bottom_left, bottom_right)

        rows, cols = len(grid), len(grid[0])
        return form_tree(0, rows, 0, cols)


if __name__ == '__main__':
    a = Solution().construct(grid = [[0,1],[1,0]])
    print(a)
