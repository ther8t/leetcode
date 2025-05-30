# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        mergedList = None
        if list1.val < list2.val:
            sublist = self.mergeTwoLists(list1.next, list2)
            list1.next = sublist
            mergedList = list1
        else:
            sublist = self.mergeTwoLists(list2.next, list1)
            list2.next = sublist
            mergedList = list2


        return mergedList


if __name__ == '__main__':
    a = Solution().mergeTwoLists(ListNode(1, ListNode(2, ListNode(3, ListNode(6, None)))), ListNode(4, ListNode(5, ListNode(7, None))))
    print(a)
