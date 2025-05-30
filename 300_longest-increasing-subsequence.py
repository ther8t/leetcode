from bisect import bisect_left


class Solution:

    """
    Revision 2 : This is a cruitial algorithm that runs on O(nlogn) which is faster than the conventional O(n2) using DP. A similar question for this is 354_russian-doll-envelopes
    """
    def lengthOfLIS(self, nums) -> int:
        lis = []
        for num in nums:
            index = bisect_left(lis, num)
            if index == len(lis):
                lis.append(num)
            else:
                lis[index] = num

        return len(lis)


if __name__ == '__main__':
    print(Solution().lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]))
    print(Solution().lengthOfLIS(nums=[0, 1, 0, 3, 2, 3]))
    print(Solution().lengthOfLIS(nums=[7, 7, 7, 7, 7, 7, 7]))
    print(Solution().lengthOfLIS(nums=[1,3,0,6,2,3,7]))
    print(Solution().lengthOfLIS(nums=[3,5,6,2,5,4,19,5,6,7,12]))

