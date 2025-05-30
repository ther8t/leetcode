# Definition for singly-linked list.
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head):
        temp = head
        while temp:
            first = temp
            if not first:
                return head
            second = first.next
            if not second:
                return head
            first.next = ListNode(math.gcd(first.val, second.val), second)
            temp = second

        return head


if __name__ == '__main__':
    s = Solution()
    o = s.insertGreatestCommonDivisors(ListNode(18, ListNode(6, ListNode(10, ListNode(3)))))
    print(o)
