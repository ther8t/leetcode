# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head):
        limit_right, limit_left, limit_top, limit_bottom = n, -1, -1, m
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0
        x, y = 0, 0
        mat = [[-1 for _ in range(n)] for _ in range(m)]

        while head:
            mat[x][y] = head.val
            head = head.next
            if direction == 0 and y + dirs[direction][1] == limit_right:
                limit_top += 1
                direction += 1
            elif direction == 1 and x + dirs[direction][0] == limit_bottom:
                limit_right -= 1
                direction += 1
            elif direction == 2 and y + dirs[direction][1] == limit_left:
                limit_bottom -= 1
                direction += 1
            elif direction == 3 and x + dirs[direction][0] == limit_top:
                limit_left += 1
                direction += 1
            direction %= 4
            x, y = x + dirs[direction][0], y + dirs[direction][1]

        return mat


if __name__ == '__main__':
    s = Solution()
    o = s.spiralMatrix(3, 5, ListNode(3, ListNode(0, ListNode(2, ListNode(6, ListNode(8, ListNode(1, ListNode(7, ListNode(9, ListNode(4, ListNode(2, ListNode(5, ListNode(5, ListNode(0))))))))))))))
    print(o)
