from sortedcontainers import SortedList


class Solution:
    """
    Revision 2:
    I am hugely surprised to that this is my original solution. I thought something as good as this would have been someone else's solution, and accepted in just a single attempt.
    TC : (m + n)log(m + n)
    """
    def minAvailableDuration(self, slots1, slots2, duration: int):
        a = SortedList()
        for start, end in slots1:
            a.add([start, 1])
            a.add([end, -1])

        for start, end in slots2:
            a.add([start, 1])
            a.add([end, -1])

        score = 0
        for i in range(len(a)):
            if score == 2 and a[i][0] - a[i - 1][0] >= duration:
                return [a[i - 1][0], a[i - 1][0] + duration]
            score += a[i][1]

        return []

    #
    # """
    # Revision 2:
    # I tried the approach similar to other questions about duration and range. The problem with this approach is that we need to traverse the whole array of slot 1 in order to find out if there is an overlap.
    # I tried using binary search to find out a position in the array where start and end fit. It works 20/25 test cases.
    # But in the test case where the range of slots2 spans across multiple ranges of slots1, it fails unless we can traverse the array, which is pointless because its brute force.
    #
    # """
    # def minAvailableDuration(self, slots1, slots2, duration: int):
    #     a = SortedList()
    #     for start, end in slots1:
    #         a.add(start)
    #         a.add(end)
    #
    #     for start, end in slots2:
    #         index = a.bisect_left(start)
    #         if index % 2 == 1 and min(a[index], end) - start >= duration:
    #             return [start, start + duration]
    #         index = a.bisect_left(end)
    #         if index % 2 == 1 and end - max(start, a[index - 1]) >= duration:
    #             return [max(start, a[index - 1]), max(start, a[index - 1]) + duration]

        return []

    """
    Attempt: Fired
    Accepted: 5%
    """
    def minAvailableDuration(self, slots1, slots2, duration: int):
        a = SortedList()
        for start, end in slots1:
            a.add((start, 1))
            a.add((end, -1))

        for start, end in slots2:
            a.add((start, 1))
            a.add((end, -1))

        current_sum = 0
        for i in range(len(a)):
            current_sum += a[i][1]
            if current_sum == 2 and a[i + 1][0] - a[i][0] >= duration:
                return [a[i][0], a[i][0] + duration]

        return []




if __name__ == '__main__':
    print(Solution().minAvailableDuration(slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8))
    print(Solution().minAvailableDuration(slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12))
    print(Solution().minAvailableDuration([[0,1000000000]], [[0,1000000000]], 1000000))
    print(Solution().minAvailableDuration([[10,12],[15, 25]], [[0,100]], 8))
