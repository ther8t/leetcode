# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleIt(self, head):

        def doubled(parent, node):
            if not node:
                return 0, None
            carry, next_node = doubled(node, node.next)
            current_val = 2 * node.val + carry
            if not parent and current_val // 10 > 0:
                return 0, ListNode(current_val // 10, ListNode(current_val % 10, next_node))
            return current_val // 10, ListNode(current_val % 10, next_node)

        _, ans = doubled(None, head)
        return ans


if __name__ == '__main__':
    ans = Solution().doubleIt(ListNode(5))
    ans = Solution().doubleIt(ListNode(9, ListNode(9, ListNode(9))))
    ans = Solution().doubleIt(ListNode(1, ListNode(9, ListNode(9))))
    print("abc")
