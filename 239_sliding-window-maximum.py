import collections
import heapq
from collections import deque

from sortedcontainers import SortedList

class Solution:
    def maxSlidingWindow(self, nums, k: int):
        n = len(nums)
        window = collections.deque()

        out = []
        for i in range(min(n, k)):
            while window and nums[i] > nums[window[-1]]:
                window.pop()
            window.append(i)

        out.append(nums[window[0]])

        for i in range(k, n):
            if window and window[0] == i - k:
                window.popleft()
            while window and nums[window[-1]] < nums[i]:
                window.pop()
            window.append(i)
            out.append(nums[window[0]])

        return out


    # def maxSlidingWindow(self, nums, k: int):
    #     n = len(nums)
    #     queue = []
    #
    #     def clean_queue(i):
    #         if queue and queue[0] == i - k:
    #             queue.pop(0)
    #
    #         while queue and nums[queue[-1]] < nums[i]:
    #             queue.pop()
    #
    #     for i in range(k):
    #         clean_queue(i)
    #         queue.append(i)
    #
    #     out = [nums[queue[0]]]
    #     for i in range(k, n):
    #         clean_queue(i)
    #         queue.append(i)
    #         out.append(nums[queue[0]])
    #
    #     return out

    # # Accepted : 5%
    # def maxSlidingWindow(self, nums, k: int):
    #     n = len(nums)
    #     nums = [-float('inf')] + nums
    #     window = SortedList(nums[:k])
    #
    #     out = []
    #     for i in range(n - k + 1):
    #         window.remove(nums[i])
    #         window.add(nums[i + k])
    #         out.append(window[-1])
    #
    #     return out


    """
    Revision 2:
    As luck would have it. This question was done right after 1499_max-value-of-equation. This is a similar question to that.
    That question had some layers to it before we could bring it down to the level of this question and yet that is a medium and this is hard. Anyway.
    But the thing is that both of these questions are similar in their approach.
    I implemented that logic and this gets accepted by 8%. Fairly low given that we have an elegant solution at hand.
    """
    # def maxSlidingWindow(self, nums, k: int):
    #     n = len(nums)
    #     window = []
    #
    #     out = []
    #     for i in range(min(n, k)):
    #         heapq.heappush(window, (-nums[i], i))
    #
    #     out.append(nums[window[0][1]])
    #
    #     for i in range(k, n):
    #         while window and i - window[0][1] >= k:
    #             heapq.heappop(window)
    #         heapq.heappush(window, (-nums[i], i))
    #         out.append(nums[window[0][1]])
    #
    #     return out

    """
    Revision 2:
    This is a nice observation. I tried using monotonic stack to solve this problem which is a simpler and faster way of solving the problem.
    Logic aside which is the same for both codes. deque is faster because that got accepted by 95% while [] was accepted by 5%.
    """
    def maxSlidingWindow(self, nums, k: int):
        n = len(nums)
        window = deque()

        out = []
        for i in range(min(n, k)):
            while window and nums[window[-1]] < nums[i]:
                window.pop()
            window.append(i)
        out.append(nums[window[0]])

        for i in range(k, n):
            if window[0] == i - k:
                window.popleft()
            while window and nums[window[-1]] < nums[i]:
                window.pop()
            window.append(i)
            out.append(nums[window[0]])

        return out


if __name__ == '__main__':
    print(Solution().maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
    print(Solution().maxSlidingWindow(nums = [1], k = 1))
    print(Solution().maxSlidingWindow([1,3,1,2,0,5], 3))
