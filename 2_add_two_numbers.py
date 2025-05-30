# Definition for singly-linked list.


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        ll = ListNode(0, None)
        current = ll
        output = []
        while ((l1 is not None) or (l2 is not None)) or carry is not 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            current_sum = l1_val + l2_val + carry
            current_unit_digit = current_sum % 10
            carry = current_sum // 10
            ll.next = ListNode(current_unit_digit, None)
            ll = ll.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return current.next


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


if __name__ == '__main__':
    s = Solution()
    o = s.addTwoNumbers(ListNode(2, ListNode(4, ListNode(3, None))), ListNode(5, ListNode(6, ListNode(4, None))))
    print(o)
