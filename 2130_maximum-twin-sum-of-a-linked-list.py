# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head) -> int:
        a = []

        while head:
            a.append(head.val)
            head = head.next

        max_twin_sum = -float('inf')
        for i in range(len(a)//2):
            max_twin_sum = max(max_twin_sum, a[i] + a[len(a) - 1 - i])

        return max_twin_sum

    # # Accepted : 5%
    # def pairSum(self, head) -> int:
    #     def max_pair_sum(h):
    #         if not h.next:
    #             return h.val + head.val, head.next
    #         current_max_sum, twin_node = max_pair_sum(h.next)
    #         current_max_sum = max(current_max_sum, twin_node.val + h.val)
    #         return current_max_sum, twin_node.next
    #
    #     return int(max_pair_sum(head)[0])


if __name__ == '__main__':
    print(Solution().pairSum(ListNode(5, ListNode(4, ListNode(2, ListNode(1))))))
