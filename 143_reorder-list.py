# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        temp = head
        while temp:
            stack.append(temp)
            temp = temp.next

        stack2 = []
        while len(stack) - len(stack2) > 1:
            stack2.append(stack.pop())

        stack[-1].next = None
        h = stack.pop() if len(stack) > len(stack2) else None

        while stack:
            s2p = stack2.pop()
            s2p.next = h
            h = s2p

            sp = stack.pop()
            sp.next = h
            h = sp

        head = h


if __name__ == '__main__':
    # print(Solution().reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))))
    print(Solution().reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))
