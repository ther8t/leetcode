import bisect
import collections

from sortedcontainers import SortedList


class Solution:

    """
    Revision 2:
    The idea is to segregate the numbers into half. It doesn't matter in what order.
    Then permute each of them and store the count and the sum of all permutations of those numbers.
    By selecting each permutation of one set, say x count, we require (n - x) from the other set. we calculate their sum and thus the final difference.
    We thus calculate the minimum difference.
    """
    def minimumDifference(self, nums) -> int:
        n, n2 = len(nums), len(nums) // 2

        def permute(arr, i, k, current_sum, sum):
            if i == len(arr):
                sum[k].append(current_sum)
                return
            permute(arr, i + 1, k, current_sum, sum)
            permute(arr, i + 1, k + 1, current_sum + arr[i], sum)

        a1, a2 = nums[:n2], nums[n2:]
        s1 = [[] for _ in range(n2 + 1)]
        permute(a1, 0, 0, 0, s1)
        s2 = [[] for _ in range(n2 + 1)]
        permute(a2, 0, 0, 0, s2)

        s1 = [sorted(s1[k]) for k in range(len(s1))]
        s2 = [sorted(s2[k]) for k in range(len(s2))]

        sum1, sum2 = sum(a1), sum(a2)
        target = (sum1 + sum2) // 2

        min_diff = float('inf')
        for k in range(n2 + 1):
            for s1k in s1[k]:
                compliment = target - (sum1 - s1k)
                pos = bisect.bisect_left(s2[k], compliment)
                if pos == len(s2[k]) or (pos != 0 and abs(compliment - s2[k][pos - 1]) < abs(compliment - s2[k][pos])):
                    # select pos - 1
                    s2k = s2[k][pos - 1]
                else:
                    s2k = s2[k][pos]
                new_sum1 = sum1 - s1k + s2k
                new_sum2 = sum2 - s2k + s1k
                min_diff = min(min_diff, abs(new_sum1 - new_sum2))

        return min_diff


# def minimumDifference(self, nums) -> int:
    #     n = len(nums)
    #     all_sum = sum(nums)
    #     diff = float('inf')
    #
    #     def permute(available, i, current_sum):
    #         nonlocal diff
    #         if available == 0:
    #             diff = min(diff, abs(all_sum - 2 * current_sum))
    #             return
    #         if current_sum > i >= n or n - i < available:
    #             return
    #         permute(available, i + 1, current_sum)
    #         permute(available - 1, i + 1, current_sum + nums[i])
    #
    #     permute(n // 2, 0, 0)
    #     return int(diff)

    """
    This is so stupid. The order of the problem statement is still O(2^n) if only O(2^(n/2)). 
    """
    def minimumDifference(self, nums) -> int:
        all_sum = sum(nums)
        target = all_sum // 2
        n = len(nums)

        def permute(arr, index, count, current_sum, permutation_count_sum_map):
            if index == n // 2:
                permutation_count_sum_map[count].add(current_sum)
                return
            permute(arr, index + 1, count, current_sum, permutation_count_sum_map)
            permute(arr, index + 1, count + 1, current_sum + arr[index], permutation_count_sum_map)

        n1, n2 = nums[:n // 2], nums[n // 2:]
        map1, map2 = collections.defaultdict(SortedList), collections.defaultdict(SortedList)
        permute(n1, 0, 0, 0, map1)
        permute(n2, 0, 0, 0, map2)

        diff = float('inf')
        for s1k in map1:
            for cs1 in map1[s1k]:
                cs2_index = map2[n // 2 - s1k].bisect_left(target - cs1)
                if cs2_index < len(map2[n // 2 - s1k]):
                    cs2 = map2[n // 2 - s1k][cs2_index]
                    diff = min(diff, abs(all_sum - 2 * (cs1 + cs2)))
                if cs2_index > 0:
                    cs2 = map2[n // 2 - s1k][cs2_index - 1]
                    diff = min(diff, abs(all_sum - 2 * (cs1 + cs2)))

        return diff

    # def minimumDifference(self, nums) -> int:
    #     n = len(nums) // 2
    #     all_sum = sum(nums)
    #
    #     def permute(index, ns):




if __name__ == '__main__':
    print(Solution().minimumDifference(nums = [3,9,7,3]))
    print(Solution().minimumDifference(nums = [-36,36]))
    print(Solution().minimumDifference(nums = [2,-1,0,4,-2,-9]))
    print(Solution().minimumDifference([34,23,30,77,85,47,96,94]))
    print(Solution().minimumDifference([7772197,4460211,-7641449,-8856364,546755,-3673029,527497,-9392076,3130315,-5309187,-4781283,5919119,3093450,1132720,6380128,-3954678,-1651499,-7944388,-3056827,1610628,7711173,6595873,302974,7656726,-2572679,0,2121026,-5743797,-8897395,-9699694]))

    [1, 1, 0]

