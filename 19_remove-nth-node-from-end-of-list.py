# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        stack = []
        dummyhead = ListNode(-1, head)
        temp = dummyhead

        while dummyhead:
            stack.append(dummyhead)
            dummyhead = dummyhead.next

        for _ in range(n):
            stack.pop()

        stack[-1].next = stack[-1].next.next
        return temp.next

    # def removeNthFromEnd(self, head, n):
    #     nPrevNodeFromEnd = None
    #     nthNodeFromEnd = None
    #
    #     dummyHead = head
    #
    #     traversingNodeCount = 0
    #     while dummyHead is not None:
    #         traversingNodeCount += 1
    #         if traversingNodeCount == n:
    #             nthNodeFromEnd = head
    #         elif traversingNodeCount > n:
    #             if nPrevNodeFromEnd == None:
    #                 nPrevNodeFromEnd = head
    #             else:
    #                 nPrevNodeFromEnd = nPrevNodeFromEnd.next
    #             nthNodeFromEnd = nthNodeFromEnd.next
    #         dummyHead = dummyHead.next
    #
    #     # remove if nth node is head.
    #     if nthNodeFromEnd == head:
    #         head = head.next
    #         return head
    #
    #     if nPrevNodeFromEnd is not None:
    #         nPrevNodeFromEnd.next = nPrevNodeFromEnd.next.next
    #     return head

    # # using stacks
    # def removeNthFromEnd(self, head, n):
    #     stack = []
    #     dummyHead = head
    #
    #     while dummyHead is not None:
    #         stack.append(dummyHead)
    #         dummyHead = dummyHead.next
    #
    #     for i in range(n - 1):
    #         if stack:
    #             stack.pop()
    #
    #     nthNodeFromEnd = None
    #     if stack:
    #         nthNodeFromEnd = stack.pop()
    #
    #     if nthNodeFromEnd == head:
    #         head = head.next
    #         return head
    #
    #     if stack:
    #         nPlusOnethNodeFromEnd = stack.pop()
    #
    #         # remove the node after nPlusOnethNodeFromEnd
    #         if nPlusOnethNodeFromEnd.next == None:
    #             return head
    #         nPlusOnethNodeFromEnd.next = nPlusOnethNodeFromEnd.next.next
    #     else:
    #         return None
    #     return head


if __name__ == '__main__':
    node = Solution().removeNthFromEnd(ListNode(1), 1)
    node = Solution().removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
    print(node)
