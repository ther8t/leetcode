# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random



class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        a = dict()
        a[None] = None

        temp = head
        while temp:
            a[temp] = (Node(temp.val))
            temp = temp.next

        temp = head
        while temp:
            a[temp].next = a[temp.next]
            a[temp].random = a[temp.random]
            temp = temp.next

        return a[head]


if __name__ == '__main__':
    a = [Node(7), Node(13), Node(11), Node(10), Node(1)]
    a[0].next = a[1]
    a[1].next = a[2]
    a[2].next = a[3]
    a[3].next = a[4]
    a[0].random = None
    a[1].random = a[0]
    a[2].random = a[4]
    a[3].random = a[2]
    a[4].random = a[0]

    print(Solution().copyRandomList(a[0]))

