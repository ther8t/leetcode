import bisect


class Solution:

    def threeSumSmaller(self, nums, target):
        nums.sort()
        count = 0
        for i in range(len(nums) - 2):
            count += self.twoSumSmaller(nums[i + 1:], target - nums[i])
        return count

    def twoSumSmaller(self, nums, target):
        left = 0
        right = len(nums) - 1
        count = 0

        while left < right:
            # find the max, because there is no use going beyond that.
            if nums[left] + nums[right] >= target:
                right -= 1
                continue
            count += (right - left)
            left += 1

        return count


    """
    Revision 2:
    This is a solution similar to the above solution, except for just one difference. I have used bisect to find the right, where as in the above solution, there's a clever little trick used.
    Since the elements are sorted in the array, if we increment the left pointer, the right pointer can either stay there or move left from the original position. It cannot move right. So we don't need to start fresh each time.
    """
    def threeSumSmaller(self, nums, target):
        n = len(nums)
        nums.sort()

        ans = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                k = bisect.bisect_left(nums, target - nums[i] - nums[j])
                if k > j:
                    ans += (k - j - 1)

        return ans

    """
    Attempt: Fired
    This is the same as above. the only change is that I have added lo.
    The concept is very simple. For two number, find the all the third numbers. The twist is in the search. Ofcourse binary search for sorted array.
    But, the issue is let's say you have [0, 1, 2, 3, 4, 5, 6, 7, 8], 7 + 8 = 15, let's say target was 20, so [0, 1, 2, 3, 4] are the third number, but for 0, 7, we would have considered 8 so the pair [0, 7, 8] was already considered..
    So we check only for the [j + 1:] 
    """
    def threeSumSmaller(self, nums, target):
        n = len(nums)
        nums.sort()

        ans = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                k = bisect.bisect_left(nums, target - nums[i] - nums[j], lo=j + 1)
                ans += (k - j - 1)

        return ans


if __name__ == '__main__':
    print(Solution().threeSumSmaller([-2,0,1,3], 2)) #2
    print(Solution().threeSumSmaller([0, -4, -1, 1, -1, 2], -5)) #1
    print(Solution().threeSumSmaller([-3,-1,-4,-4,0,2,-2], -8)) #5
    print(Solution().threeSumSmaller([3,1,0,-2], 4)) #3
