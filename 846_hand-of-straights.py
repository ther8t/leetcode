import collections


class Solution:
    def isNStraightHand(self, hand, groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        h = collections.Counter(hand)
        stack = []
        while h:
            selected = None
            if not stack:
                selected = min(h)
            else:
                if stack[-1] + 1 in h:
                    selected = stack[-1] + 1
            if selected == None:
                return False
            stack.append(selected)
            h[selected] -= 1
            if len(stack) == groupSize:
                stack = []
            if h[selected] == 0:
                del h[selected]
        return True


if __name__ == '__main__':
    # print(Solution().isNStraightHand(hand = [1,2,3,10,2,3,4,7,8], groupSize = 3))
    print(Solution().isNStraightHand(hand = [0,1], groupSize = 2))
