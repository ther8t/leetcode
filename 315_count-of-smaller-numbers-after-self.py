import bisect
from sortedcontainers import SortedList


class Solution:
    """
    Revision 2 : This is a new and simplified algo of the first algo I had coded for this question. The remaining approaches to the question are a good study in segment tree but are too overly complicated.
    """
    # Accepted : 99.88%
    def countSmaller(self, nums):
        out = []
        a = SortedList()

        for num in reversed(nums):
            out.append(a.bisect_left(num))
            a.add(num)

        return list(reversed(out))


    def countSmaller(self, nums):
        OFFSET = 10 ** 4
        size = 2 * OFFSET + 1
        tree = [0] * (2 * size)

        # tree = [0] * (4 * OFFSET + 1) can't do this.
        # The reason we leave the first index empty is because when we update a number it boils down to 0
        # (for example : 31, 15, 7, 3, 1, 0). If we begin at 0 we'll have to update 0th index but that also means that
        # we can't stop the iteration because 0//2 = 0 so 0, 0, 0, 0... will follow

        def update(number):
            leaf_address = size + number + OFFSET

            while leaf_address > 0:
                tree[leaf_address] += 1
                leaf_address //= 2

        def query(left, right):
            left = size + left + OFFSET
            right = size + right + OFFSET

            result = 0
            while left <= right:
                if left % 2 == 1:
                    result += tree[left]
                    left += 1
                left //= 2

                if right % 2 == 0:
                    result += tree[right]
                    right -= 1
                right //= 2

            return result

        out = []
        for num in reversed(nums):
            update(num)
            out.append(query(-OFFSET, num - 1))

        return list(reversed(out))

    # # TLE
    # def countSmaller(self, nums):
    #     MAX_SIZE = 10
    #     size = 2 * MAX_SIZE + 1
    #     tree = [0] * (2 * size)
    #
    #     # def get_sum_from_to(arr_index_from, arr_index_to, arr_lo=1, arr_hi=size, tree_position=1):
    #     #     # mid = (left + right) // 2
    #     #     # first_half : [left : mid]
    #     #     # second_half : [mid + 1 : right]
    #     #     # is there an overlap with the first?
    #     #     if arr_index_to < arr_lo or arr_index_from > arr_index_to:
    #     #         # no overlap
    #     #         return 0
    #     #     if arr_index_from <= arr_lo and arr_hi <= arr_index_to:
    #     #         # the current array range is within the series we want to sum
    #     #         # This also returns for a complete overlap
    #     #         return tree[tree_position]
    #     #     mid = (arr_lo + arr_hi) // 2
    #     #     return get_sum_from_to(arr_index_from, arr_index_to, arr_lo, mid, 2 * tree_position) + get_sum_from_to(arr_index_from, arr_index_to, mid + 1, arr_hi, 2 * tree_position + 1)
    #
    #     def update(arr_index, increment):
    #         leaf_index = arr_index + size
    #
    #         while leaf_index >= 1:
    #             tree[leaf_index] += increment
    #             leaf_index //= 2
    #
    #     def query(f, t):
    #         f += size
    #         t += size
    #
    #         left, right = f, t
    #         result = 0
    #         while left < right:
    #             if left % 2 == 1:
    #                 result += tree[left]
    #                 left += 1
    #             left //= 2
    #
    #             if right % 2 == 1:
    #                 right -= 1
    #                 result += tree[right]
    #             right //= 2
    #
    #         return result
    #
    #
    #
    #     # construct_tree(1, len(freq), 1)
    #     out = []
    #     for num in reversed(nums):
    #         out.append(query(0, num + MAX_SIZE))
    #         update(num + MAX_SIZE, 1)
    #
    #     return list(reversed(out))


    # # TLE
    # def countSmaller(self, nums):
    #     MAX_SIZE = 10 ** 4
    #     freq = [0] * (2 * MAX_SIZE + 1)
    #     tree = [0] * (4 * len(freq))
    #
    #     def construct_tree(arr_lo, arr_hi, tree_position=1):
    #         if arr_lo == arr_hi:
    #             tree[tree_position] = freq[arr_lo - 1]
    #             return tree[tree_position]
    #         mid = (arr_lo + arr_hi) // 2
    #         tree[tree_position] = construct_tree(arr_lo, mid, 2 * tree_position) + construct_tree(mid + 1, arr_hi, 2 * tree_position + 1)
    #
    #         return tree[tree_position]
    #
    #     """
    #     Gets the sum of the nums [1(starting, 1-indexed) : nums(inclusive)]
    #     """
    #     def get_sum(arr_index, arr_lo=1, arr_hi=len(freq), tree_position=1):
    #         # mid = (left + right) // 2
    #         # first_half : [left : mid]
    #         # second_half : [mid + 1 : right]
    #         # is there an overlap with the first?
    #         if arr_index + 1 < arr_lo and arr_index + 1 < arr_hi:
    #             return 0
    #         if arr_lo <= arr_index + 1 and arr_hi <= arr_index + 1:
    #             return tree[tree_position]
    #         mid = (arr_lo + arr_hi) // 2
    #         return get_sum(arr_index, arr_lo, mid, 2 * tree_position) + get_sum(arr_index, mid + 1, arr_hi, 2 * tree_position + 1)
    #
    #     def get_sum_from_to(arr_index_from, arr_index_to, arr_lo=1, arr_hi=len(freq), tree_position=1):
    #         # mid = (left + right) // 2
    #         # first_half : [left : mid]
    #         # second_half : [mid + 1 : right]
    #         # is there an overlap with the first?
    #         if arr_index_to < arr_lo or arr_index_from > arr_index_to:
    #             # no overlap
    #             return 0
    #         if arr_index_from <= arr_lo and arr_hi <= arr_index_to:
    #             # the current array range is within the series we want to sum
    #             # This also returns for a complete overlap
    #             return tree[tree_position]
    #         mid = (arr_lo + arr_hi) // 2
    #         return get_sum_from_to(arr_index_from, arr_index_to, arr_lo, mid, 2 * tree_position) + get_sum_from_to(arr_index_from, arr_index_to, mid + 1, arr_hi, 2 * tree_position + 1)
    #
    #     def update(arr_index, increment, arr_lo=1, arr_hi=len(freq), tree_position=1):
    #         if arr_lo <= arr_index + 1 <= arr_hi:
    #             print(tree_position)
    #             tree[tree_position] += increment
    #             mid = (arr_lo + arr_hi) // 2
    #             if arr_lo != arr_hi:
    #                 update(arr_index, increment, arr_lo, mid, 2 * tree_position)
    #                 update(arr_index, increment, mid + 1, arr_hi, 2 * tree_position + 1)
    #
    #     # construct_tree(1, len(freq), 1)
    #     out = []
    #     for num in reversed(nums):
    #         freq[num + MAX_SIZE] += 1
    #         update(num + MAX_SIZE, 1)
    #         out.append(get_sum(num - 1 + MAX_SIZE))
    #
    #     return list(reversed(out))


    # # Accepted Solution : Derived from the genius of my own brain.
    # def countSmaller(self, nums):
    #     sorted_nums = sorted(nums)
    #     a = SortedList()
    #     out = []
    #
    #     for num in nums:
    #         out.append(bisect.bisect_left(sorted_nums, num) - a.bisect_left(num))
    #         a.add(num)
    #
    #     return out

if __name__ == '__main__':
    # print(Solution().countSmaller(nums=[-1,-1]))
    # print(Solution().countSmaller(nums=[-1]))
    # print(Solution().countSmaller(nums=[1]))
    # print(Solution().countSmaller(nums=[5, 2, 6, 1]))
    print(Solution().countSmaller([26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41]))

