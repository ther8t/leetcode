# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        dummyHead = tempHead = ListNode(-1)
        dummyHead.next = head

        while tempHead and tempHead.next and tempHead.next.next:
            swapNode1 = tempHead.next
            swapNode2 = tempHead.next.next

            swapNode1.next = swapNode2.next
            swapNode2.next = tempHead.next
            tempHead.next = swapNode2

            tempHead = swapNode1

        return dummyHead.next



if __name__ == '__main__':
    a = Solution().swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
    print(a)
