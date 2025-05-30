from sortedcontainers import SortedList


class Solution:
    """
    Interesting question.
    I have done one such question before. There was a shuffling of the equation needed. The rest was same as finding the numbers greater than our current number which is also similar to another question.
    Remember the question about segment tree. The classic question which I got correct in the first try and yet had to spend so much time trying to figure out because of Segment tree.
    """
    def numberOfPairs(self, nums1, nums2, diff: int) -> int:
        n = len(nums1)
        d = [nums1[i] - nums2[i] for i in range(n)]
        a = SortedList()
        ans = 0
        for number in reversed(d):
            index = a.bisect_left(number - diff)
            ans += (len(a) - index)
            a.add(number)
        return ans

    """
    Attempt: Fired
    Accepted: 74%
    """
    def numberOfPairs(self, nums1, nums2, diff: int) -> int:
        n = len(nums1)
        d = [nums1[i] - nums2[i] for i in range(n)]
        a = SortedList()
        ans = 0

        for number in d:
            index = a.bisect_right(number + diff)
            ans += index
            a.add(number)

        return ans


if __name__ == '__main__':
    print(Solution().numberOfPairs(nums1 = [3,2,5], nums2 = [2,2,1], diff = 1))
    print(Solution().numberOfPairs(nums1 = [3,-1], nums2 = [-2,2], diff = -1))

