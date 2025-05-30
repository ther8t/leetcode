from bisect import bisect_left, bisect_right


class Solution:
    """
    Acepted 41%
    This is a brilliant question. It requires binary search over one of the arrays to measure if the remainder from the other array makes sense.
    The intuition here is that in an array the mid points will be more than or equal to all the 'selected' numbers.
    [1, 2] [5, 6, 7]  If I try to select [1] [5]. This does not make sense because 2 < 5. In the sorted combined array, 1 and 5 cannot come together.

    One crucial thing to consider here is lo <= hi, instead of lo < hi. This is because there maybe a case where we take all the elements of an array, which happens at lo == hi.
    """
    def findMedianSortedArrays(self, nums1, nums2):
        n1, n2 = len(nums1), len(nums2)
        if n1 < n2: return self.findMedianSortedArrays(nums2, nums1)
        target = (n1 + n2) // 2

        lo, hi = 0, n2
        while lo <= hi:
            mid2 = (lo + hi) // 2
            mid1 = target - mid2

            if mid1 - 1 >= 0 and 0 <= mid2 < n2 and nums2[mid2] < nums1[mid1 - 1]:
                lo = mid2 + 1
            elif mid2 - 1 >= 0 and 0 <= mid1 < n1 and nums1[mid1] < nums2[mid2 - 1]:
                hi = mid2
            else:
                if (n1 + n2) % 2 == 1:
                    return min(nums1[mid1] if 0 <= mid1 < n1 else float('inf'), nums2[mid2] if 0 <= mid2 < n2 else float('inf'))
                else:
                    first = [nums1[mid1 - 1] if 0 <= mid1 - 1 < n1 else -float('inf'), nums2[mid2 - 1] if 0 <= mid2 - 1 < n2 else -float('inf')]
                    second = [nums1[mid1] if 0 <= mid1 < n1 else float('inf'), nums2[mid2] if 0 <= mid2 < n2 else float('inf')]
                    return (max(first) + min(second)) / 2



    # # Wrong Answer : 2091/2098
    # def findMedianSortedArrays(self, nums1, nums2):
    #     lo, hi = min(nums1[0] if nums1 else float('inf'), nums2[0] if nums2 else float('inf')), max(nums1[-1] if nums1 else -float('inf'), nums2[-1] if nums2 else -float('inf'))
    #     target = (len(nums1) + len(nums2) + 1) // 2 - 1
    #     n1, n2 = 0, 0
    #
    #     while lo < hi:
    #         mid = (lo + hi) // 2
    #         n1, n2 = bisect_left(nums1, mid), bisect_left(nums2, mid)
    #         if n1 + n2 == target:
    #             a = []
    #             for i in range(n1, n1 + 2):
    #                 if i < len(nums1):
    #                     a.append(nums1[i])
    #             for i in range(n2, n2 + 2):
    #                 if i < len(nums2):
    #                     a.append(nums2[i])
    #             a.sort()
    #             if (len(nums1) + len(nums2)) % 2 == 1:
    #                 return a[0]
    #             else:
    #                 return (a[0] + a[1]) / 2
    #         if n1 + n2 < target:
    #             lo = mid + 1
    #         else:
    #             hi = mid

        # a = [nums1[n1], nums2[n2]]
        # a.sort()
        # if (len(nums1) + len(nums2)) % 2 == 1:
        #     return a[0]
        # else:
        #     return (a[0] + a[1]) / 2

    # def findMedianSortedArrays(self, nums1, nums2):
    #     ptr1=0
    #     ptr2=0
    #     new_array = []
    #     while ptr1 < len(nums1) and ptr2 < len(nums2):
    #         if nums1[ptr1] > nums2[ptr2]:
    #             new_array.append(nums2[ptr2])
    #             ptr2 += 1
    #         else :
    #             new_array.append(nums1[ptr1])
    #             ptr1 += 1
    #
    #     # add the remaining elements in.
    #     while ptr1 < len(nums1):
    #         new_array.append(nums1[ptr1])
    #         ptr1+=1
    #
    #     while ptr2 < len(nums2):
    #         new_array.append(nums2[ptr2])
    #         ptr2+=1
    #
    #
    #     if (len(nums1) + len(nums2))%2 == 1:
    #         return new_array[len(new_array)//2]
    #     else:
    #         return (new_array[len(new_array)//2] + new_array[len(new_array)//2 - 1])/2


if __name__ == '__main__':
    # print(Solution().findMedianSortedArrays(nums1 = [1,3], nums2 = [2]))
    # print(Solution().findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))
    print(Solution().findMedianSortedArrays([1, 2], [5, 6, 7]))
    print(Solution().findMedianSortedArrays([0,0], [0,0]))
    print(Solution().findMedianSortedArrays([], [1]))
    print(Solution().findMedianSortedArrays([], [1,2,3,4]))
    print(Solution().findMedianSortedArrays([2,2,4,4], [2,2,4,4]))
