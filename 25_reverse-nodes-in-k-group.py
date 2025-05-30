# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    """
    Revision 2:
    Lesson #1 : Don't try and be Bond. If you know a code would work code it first and then try and make it look pretty. I tried to make the if condition in reverse_group be a single condition and i am sure there must be a way to do that.
    But remember, A working looks better than a non-working pretty code, which looks more empty and despondent.
    This is the O(1) space complexity algo.
    """
    def reverseKGroup(self, head, k):

        def reverse_group(parent, head, position):
            if k % 2 == 1 and position == (k - 1) // 2:
                return head
            if k % 2 == 0 and position == (k - 1) // 2:
                tail = head.next
                head.next = tail.next
                tail.next = head
                parent.next = tail
                return tail
            if position <= (k - 1) // 2:
                sub_list_tail = head.next
                sub_list_head = reverse_group(head, head.next, position + 1)
                parent.next = sub_list_tail.next
                head.next = sub_list_tail.next.next
                sub_list_tail.next.next = sub_list_head
                sub_list_tail.next = head

                return parent.next

        parent = dummy_head = ListNode(-1)
        temp_head = dummy_head.next = head
        while temp_head:
            counter = 0
            tail = temp_head
            while counter < k and tail:
                tail = tail.next
                counter += 1

            if counter == k:
                reverse_group(parent, temp_head, 0)

            parent = temp_head
            temp_head = tail

        return dummy_head.next

    # def reverseKGroup(self, head, k):
    #     if head is None:
    #         return None
    #     headPointer = head
    #
    #     nodesStack = []
    #     counter = k
    #     tail = None
    #     reversedList = dummyReversedListHead = ListNode(-1)
    #     while head is not None and counter > 0:
    #         nodesStack.append(head)
    #         head = head.next
    #         tail = head
    #         counter -= 1
    #
    #     if counter is 0:
    #         # reverse the list by popping the stack and adding as tail
    #         while len(nodesStack) > 0:
    #             node = nodesStack.pop()
    #             reversedList.next = node
    #             reversedList = reversedList.next
    #         # get reversed list starting from tail.next
    #         # append reversed subList to current reversed list
    #         reversedSubList = self.reverseKGroup(tail, k)
    #         headPointer.next = reversedSubList
    #         # return current head
    #         return dummyReversedListHead.next
    #     else:
    #         return headPointer


if __name__ == '__main__':
    a = Solution().reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 1)
    print(a)
