import collections
from queue import PriorityQueue
from sortedcontainers import SortedList
import  q

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeKLists(self, lists):
        if not lists:
            return None
        simplified_list = []
        for list in lists:
            if list:
                current_list = []
                while list:
                    current_list.append(list.val)
                    list = list.next
                simplified_list.append(current_list)

        merged = []
        for i in range(len(simplified_list)):
            merged = heapq.merge(merged, simplified_list[i])
        merged_list = ListNode(-1)
        temp = merged_list
        while True:
            if not merged:
                break
            next_value = next(merged, None)
            if next_value:
                temp.next = ListNode(next_value)
                temp = temp.next
            else:
                break
        return merged_list.next

    # def mergeKLists(self, lists):
    #     ans = ListNode(-1, None)
    #     temp = ans
    #     queue = []
    #     value_map = collections.defaultdict(list)
    #
    #     for node in lists:
    #         if node:
    #             heapq.heappush(queue, node.val)
    #             value_map[node.val].append(node)
    #
    #     while queue:
    #         next_node_value = heapq.heappop(queue)
    #         next_node = value_map[next_node_value].pop(0)
    #         temp.next = ListNode(next_node_value)
    #         temp = temp.next
    #         if next_node.next:
    #             next_node = next_node.next
    #             heapq.heappush(queue, next_node.val)
    #             value_map[next_node.val].append(next_node)
    #
    #     return ans.next



    # def mergeKLists(self, lists):
    #     newList = ListNode(-1, None)
    #     q = PriorityQueue()
    #     for i in lists:
    #         if i:
    #             q.put((i.val, i))
    #     while not q.empty():
    #         minNode = minNodePoint = q.get()
    #         newList.next = minNodePoint
    #         newList = newList.next
    #         minNode = minNode.next
    #         if minNode:
    #             q.put((minNode.val, minNode))
    #     return newList.next

    #     def sortFunc(node):
    #         if node is None:
    #             return float('inf')
    #         return node.val
    #
    #     lists.sort(key=sortFunc)
    #     return self.mergeKListsRec(lists)
    #
    # def mergeKListsRec(self, lists):
    #     if len(lists) > 0:
    #         minHead = lists[0]
    #         if minHead is None:
    #             return None
    #         lists[0] = lists[0].next
    #         currentMinNextVal = float('inf') if lists[0] is None else lists[0].val
    #         itsNewPosition = 0
    #         for listElementIndex in range(1, len(lists)):
    #             if lists[listElementIndex] is not None and lists[listElementIndex].val < currentMinNextVal:
    #                 itsNewPosition = listElementIndex
    #             else:
    #                 break
    #
    #         mergedSubList = self.mergeKListsRec(lists[1:itsNewPosition + 1] + [lists[0]] + lists[itsNewPosition + 1:])
    #         minHead.next = mergedSubList
    #
    #         return minHead
    #     else:
    #         return None


if __name__ == '__main__':
    a = Solution().mergeKLists([None])
    # a = Solution().mergeKLists(
    #     [ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))])
    print(a)
    a = SortedList()
    a.add(1)
    a.add(2)
    a.add(4)
    a[a.index(4)] = 22
    print(a)


