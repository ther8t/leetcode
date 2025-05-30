from collections import deque


class Solution:
    def longestSubarray(self, nums, limit: int) -> int:
        maxq = deque()
        minq = deque()
        max_length = 1
        l = 0

        for i in range(len(nums)):
            while maxq and maxq[-1] < nums[i]: maxq.pop()
            while minq and minq[-1] > nums[i]: minq.pop()
            maxq.append(nums[i])
            minq.append(nums[i])
            while maxq[0] - minq[0] > limit:
                if maxq[0] == nums[l]: maxq.popleft()
                if minq[0] == nums[l]: minq.popleft()
                l += 1
            max_length = max(max_length, i - l + 1)
        return max_length


    """
    Revision 2 :
    This is almost the same implementation as the above code. This question is more of a lesson for me. I had given much effort to quality than the number of questions I did when I was solving questions for Google.
    After swimming I was more focused on the quantity of the questions which I am getting to regret. My preparation for those topics of the questions is far better than my prep for the topics which I did to satisfy my quantity thirst.
    This is one of those questions for which I viewed the solutions perhaps too early. There are so many questions I have begun to realise are similar to this question. 1499_max-value-of-equation and more questions in the description of that question.
    
    Algo:
    The algo goes something like this.
    I keep a track of the ascending and descending order of an array monotonically. This means that in order to find a 
    maximum and minimum over a range I would store the numbers in such a way that for minimum the numbers above a number 
    will always be more and a number of higher index having lower value will replace all the numbers of lower index and 
    higher value because the current value would be the minimum.
    
    I do this for both min and max. 
    Once done I would have the minimum and maximum at every index. The only thing I need to take care of is that the 
    minimum and maximum are within a specific range.
    To keep track of that I use a sliding window starting at index 0 and adding each number into both min and max queues.
    A number can be popped from the queues in two ways. Either the number is out of the given 'limit', in which case we 
    would change the width of sliding window by shifting the left edge incrementally till it reaches the limit.(Why not 
    right limit? Because we are moving from left to right, that would already be taken care of.)
    The other way a number can be popped from the queue is if it encounters a number greater than itself in max queue or
    smaller than itself in a min queue.
    """
    def longestSubarray(self, nums, limit: int) -> int:
        maxq = deque()
        minq = deque()
        max_length = 1
        lo = 0

        for i in range(len(nums)):
            while maxq and nums[maxq[-1]] < nums[i]: maxq.pop()
            while minq and nums[minq[-1]] > nums[i]: minq.pop()
            maxq.append(i)
            minq.append(i)
            while nums[maxq[0]] - nums[minq[0]] > limit:
                if maxq[0] == lo: maxq.popleft()
                if minq[0] == lo: minq.popleft()
                lo += 1

            max_length = max(max_length, i - lo + 1)
        return max_length




    # def longestSubarray(self, nums, limit: int) -> int:
    #     a = SortedList()
    #     max_length = 0
    #     ptr1 = 0
    #
    #     for index, num in enumerate(nums):
    #         max_index = ptr1 - 1
    #         while a and abs(num - a[0][0]) > limit:
    #             removed_index = a[0][1]
    #             a.pop(0)
    #             max_index = max(max_index, removed_index)
    #         while a and abs(num - a[-1][0]) > limit:
    #             removed_index = a[-1][1]
    #             a.pop()
    #             max_index = max(max_index, removed_index)
    #
    #         for i in range(ptr1, max_index + 1):
    #             if (nums[i], i) in a:
    #                 a.remove((nums[i], i))
    #
    #         ptr1 = max_index + 1
    #         a.add((num, index))
    #         max_length = max(max_length, len(a))
    #
    #     return max_length


if __name__ == '__main__':
    # print(Solution().longestSubarray([10,4,1,2,7,2], limit = 5)) #3
    # print(Solution().longestSubarray([8,2,4,7], limit = 4)) #2
    # print(Solution().longestSubarray([10,1,2,4,7,2], limit = 5)) #4
    # print(Solution().longestSubarray([4,2,2,2,4,4,2,2], limit = 0)) #3
    # print(Solution().longestSubarray([1,5,6,7,8,10,6,5,6], 4)) #5
    # print(Solution().longestSubarray([2,2,2,4,4,2,5,5,5,5,5,2], 2)) #6
    print(Solution().longestSubarray([4,10,2,6,1], 10)) #5
