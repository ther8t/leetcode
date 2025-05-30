import collections
import heapq


class Solution:
    def minOperations(self, nums1, nums2) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        if sum1 == sum2:
            return 0
        if sum1 > sum2:
            nums1, nums2 = nums2, nums1
            sum1, sum2 = sum2, sum1
        n1, n2 = len(nums1), len(nums2)

        lo1, hi1, lo2, hi2 = n1, 6 * n1, n2, 6 * n2

        if hi1 < lo2 or hi2 < lo1:
            return -1

        q1 = []
        for num in nums1:
            heapq.heappush(q1, num)
        q2 = []
        for num in nums2:
            heapq.heappush(q2, -num)

        diff = sum2 - sum1
        res = 0

        while q1 or q2:
            if diff == 0:
                return res
            if not q2 or (q1 and q2 and 6 - q1[0] > -q2[0] - 1):
                popped = heapq.heappop(q1)
                diff -= min(diff, 6 - popped)
                res += 1
            elif not q1 or (q1 and q2 and 6 - q1[0] <= -q2[0] - 1):
                popped = heapq.heappop(q2)
                diff -= min(diff, -popped - 1)
                res += 1
        return res



# # Accepted :5%
    # def minOperations(self, nums1, nums2) -> int:
    #     if len(nums1) > len(nums2):
    #         nums1, nums2 = nums2, nums1
    #     n1, n2 = len(nums1), len(nums2)
    #
    #     lo1, hi1, lo2, hi2 = n1, 6 * n1, n2, 6 * n2
    #
    #     if hi1 < lo2:
    #         return -1
    #
    #     def get_sum(counter):
    #         s = 0
    #         for k in counter:
    #             s += k * counter[k]
    #         return s
    #
    #     counter1, counter2 = collections.Counter(nums1), collections.Counter(nums2)
    #     sum1, sum2 = get_sum(counter1), get_sum(counter2)
    #     if sum1 == sum2:
    #         return 0
    #
    #     limit1, limit2 = max(lo2, min(sum1, sum2)), min(hi1, max(sum1, sum2))
    #
    #     def reach(counter, current_sum, target_sum):
    #         replace_count = 0
    #         if current_sum > target_sum:
    #             # reduce the sum from counter
    #             diff = current_sum - target_sum
    #             for num in range(6, 1, -1):
    #                 if num not in counter:
    #                     continue
    #                 if (num - 1) * counter[num] < diff:
    #                     replace_count += counter[num]
    #                     diff -= (num - 1) * counter[num]
    #                 else:
    #                     replace_count += diff // (num - 1) + (1 if diff % (num - 1) != 0 else 0)
    #                     break
    #         elif current_sum < target_sum:
    #             # increase the sum of counter
    #             diff = target_sum - current_sum
    #             for num in range(1, 6):
    #                 if num not in counter:
    #                     continue
    #                 if (6 - num) * counter[num] < diff:
    #                     replace_count += counter[num]
    #                     diff -= (6 - num) * counter[num]
    #                 else:
    #                     replace_count += diff // (6 - num) + (1 if diff % (6 - num) != 0 else 0)
    #                     break
    #         return replace_count
    #
    #     min_moves = float('inf')
    #     for target_sum in range(limit1, limit2 + 1):
    #         min_moves = min(min_moves, reach(counter1, sum1) + reach(counter2, sum2))
    #     return min_moves


if __name__ == '__main__':
    print(Solution().minOperations(nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]))
    print(Solution().minOperations(nums1 = [1,1,1,1,1,1,1], nums2 = [6]))
    print(Solution().minOperations(nums1 = [6,6], nums2 = [1]))
    print(Solution().minOperations([5,2,1,5,2,2,2,2,4,3,3,5], [1,4,5,5,6,3,1,3,3]))
