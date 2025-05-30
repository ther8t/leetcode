import functools
import heapq
from functools import lru_cache


class Solution:

    """
    Revision 2:
    The BEST algo among them all.
    This is a brilliant piece of algorithm which I couldn't think of.
    The idea is that since the sum of array elements is monotonic in nature we could use binary search guess the number. It's much like the binary search algos I have used earlier for distances and such questions.
    """
    def splitArray(self, nums, m: int) -> int:
        def splits(max_array_sum):
            splits_required = 0
            current_sum = 0

            for i in range(len(nums)):
                if current_sum + nums[i] <= max_array_sum:
                    current_sum += nums[i]
                else:
                    current_sum = nums[i]
                    splits_required += 1

            return splits_required + 1

        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2

            if splits(mid) <= m:
                right = mid
            else:
                left = mid + 1

        return left


    """
    Revision 2:
    This is a simple backtrack + memorization technique. Effective in some cases but TLE in this.
    """
    def splitArray(self, nums, m: int) -> int:
        current_sum = 0
        prefix_sum = [0]
        for i in nums:
            current_sum += i
            prefix_sum.append(current_sum)

        @lru_cache(None)
        def split_a(start_index, k):
            if k == 1:
                return prefix_sum[len(nums)] - prefix_sum[start_index]

            min_largest_sum = float('inf')
            for i in range(start_index, len(nums)):
                current_sum = prefix_sum[i + 1] - prefix_sum[start_index]
                largest_sub_sum = max(current_sum, split_a(i + 1, k - 1))
                min_largest_sum = min(min_largest_sum, largest_sub_sum)
                if current_sum >= largest_sub_sum:
                    break

            return min_largest_sum

        return split_a(0, m)


    """
    Revision 2:
    This is same as the backtrack + memorization technique.
    """
    def splitArray(self, nums, m: int) -> int:
        dp = [[None] * (m + 1) for _ in range(len(nums))]

        sum = 0
        for n in range(len(dp) - 1, -1, -1):
            sum += nums[n]
            dp[n][1] = sum

        for group_size in range(2, m + 1):
            for i in range(len(nums) - group_size, -1, -1):
                minimized_for_group_size = float('inf')
                number = 0
                for j in range(i, len(nums) - group_size + 1):
                    number += nums[j]
                    minimized_for_group_size = min(minimized_for_group_size, max(number, dp[j + 1][group_size - 1]))
                    if minimized_for_group_size == 0 or number > dp[j + 1][group_size - 1]:
                        break
                dp[i][group_size] = minimized_for_group_size

        return dp[0][m]


    def splitArray(self, nums, m: int) -> int:
        h = []

        for i in range(1, len(nums) + 1):
            heapq.heappush(h, (sum(nums[:i]), m - 1, i, 1))

        while h:
            max_sum, k, starting, partitions = heapq.heappop(h)
            if k == 0 and partitions == m and starting == len(nums):
                return max_sum

            for i in range(starting + 1, len(nums) + 1):
                heapq.heappush(h, (max(max_sum, sum(nums[starting:i])), k - 1, i, partitions + 1))

        return -1

    """
    Attempt: Fired
    Accepted: 5%
    """
    def splitArray(self, nums, m: int) -> int:
        prefix_sum = [0 for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        def getSum(start, end):
            return prefix_sum[end - 1] - prefix_sum[start - 1]

        @functools.lru_cache(None)
        def dfs(starting, k):
            if k == 1:
                return getSum(starting, len(nums))

            current_min_max = float('inf')
            for i in range(starting + 1, len(nums)):
                current_min_max = min(current_min_max, max(getSum(starting, i), dfs(i, k - 1)))

            return current_min_max

        return dfs(0, m)







    # def splitArray(self, nums, m: int) -> int:
    #     prefix_sums = [0]
    #     current_sum = 0
    #     for num in nums:
    #         current_sum += num
    #         prefix_sums.append(current_sum)
    #
    #     all_sum = sum(nums)
    #     average = all_sum // m
    #     nums_max = max(nums)
    #
    #     def get_sum(f, t):
    #         return prefix_sums[t - 1] - prefix_sums[f - 1]
    #
    #     def can_split(starting_position, max_value, remaining):
    #         if remaining == 0 and starting_position == len(nums):
    #             return True
    #         if remaining > len(nums) - starting_position:
    #             return False
    #         if starting_position >= len(nums):
    #             return False
    #
    #         for end_position in range(starting_position + 1, len(nums)):
    #             if get_sum(starting_position, end_position) > max_value:
    #                 return False
    #             if can_split(end_position, max_value, m-1):
    #                 return True
    #
    #         return False
    #
    #     left, right = max(average, nums_max), all_sum
    #     while left < right:
    #         mid = (left + right) // 2
    #         if can_split(1, mid, m):
    #             right = mid
    #         else:
    #             left = mid + 1
    #
    #     return right

    # # TLE 23/30
    # def splitArray(self, nums, m: int) -> int:
    #     all_sum = sum(nums)
    #     average = all_sum // m
    #     nums_max = max(nums)
    #
    #     def can_split(starting_position, max_value, remaining):
    #         if remaining == 0 and starting_position == len(nums):
    #             return True
    #         if remaining > len(nums) - starting_position:
    #             return False
    #         if starting_position >= len(nums):
    #             return False
    #
    #         ptr = starting_position
    #         current_sum = nums[ptr]
    #         while ptr + 1 < len(nums) and current_sum + nums[ptr + 1] <= average:
    #             current_sum += nums[ptr + 1]
    #             ptr += 1
    #
    #         while ptr < len(nums) and current_sum <= max_value:
    #             if remaining == len(nums) - starting_position:
    #                 return True
    #             if can_split(ptr + 1, max_value, remaining - 1):
    #                 return True
    #             elif ptr + 1 < len(nums):
    #                 current_sum += nums[ptr + 1]
    #                 ptr += 1
    #             else:
    #                 break
    #
    #         return False
    #
    #     left, right = max(average, nums_max), all_sum
    #     while left < right:
    #         mid = (left + right) // 2
    #         if can_split(0, mid, m):
    #             right = mid
    #         else:
    #             left = mid + 1
    #
    #     return right





    # # Wrong Answer : 29/30, but this is a wrong solution. I never considers the possibility of that numbers much below the current max can be a part of the solution.
    # def splitArray(self, nums, m: int) -> int:
    #     all_sum = sum(nums)
    #     average = all_sum // m
    #
    #     def min_sum_split(sum_limit):
    #         ptr1, ptr2 = 0, 0
    #         sums = []
    #         while ptr1 < len(nums) and ptr2 < len(nums):
    #             current_sum = nums[ptr1]
    #             ptr2 = ptr1
    #             while ptr2 + 1 < len(nums) and current_sum + nums[ptr2 + 1] <= sum_limit:
    #                 current_sum += nums[ptr2 + 1]
    #                 ptr2 += 1
    #             sums.append(current_sum)
    #             ptr1 = ptr2 + 1
    #
    #         return sums
    #
    #     global_sum_min = float('inf')
    #     for starting in range(len(nums)):
    #         ptr = starting
    #         current_sum_max = 0
    #         while ptr < len(nums) and (current_sum_max < average):
    #             current_sum_max += nums[ptr]
    #             ptr += 1
    #
    #         if current_sum_max < global_sum_min:
    #             split = min_sum_split(current_sum_max)
    #             if len(split) != m:
    #                 continue
    #             global_sum_min = max(split)
    #
    #     return global_sum_min


    # # TLE
    # def splitArray(self, nums, m: int) -> int:
    #     all_sum = sum(nums)
    #     average = all_sum // m
    #     dp = {}
    #
    #     def min_sum_split(starting_position, sums, remaining):
    #         if starting_position >= len(nums):
    #             if remaining == 0 and max(sums) == 28:
    #                 print(sums)
    #             return max(sums) if len(sums) == m else float('inf')
    #
    #         if (starting_position, len(sums)) in dp:
    #             return dp[(starting_position, len(sums))]
    #
    #         ptr = starting_position
    #         current_sum = nums[ptr]
    #         while ptr + 1 < len(nums) and (nums[ptr + 1] + current_sum <= average or remaining == 1):
    #             current_sum += nums[ptr + 1]
    #             ptr += 1
    #
    #         min_sum = float('inf')
    #         while current_sum < 2 * average:
    #             min_sum = min(min_sum, min_sum_split(ptr + 1, sums + [current_sum], remaining - 1))
    #             if ptr + 1 < len(nums):
    #                 current_sum += nums[ptr + 1]
    #                 ptr += 1
    #             else:
    #                 break
    #
    #         dp[(starting_position, len(sums))] = min_sum
    #         return min_sum
    #
    #     return min_sum_split(0, [], m)


    # # Wrong Answer : 23/30 I knew it would be the wrong answer because in my case it's the extremes which have to carry the burden of the remaining in the average.
    # def splitArray(self, nums, m: int) -> int:
    #     all_sum = sum(nums)
    #     average = all_sum//m
    #
    #     starting = 0
    #     max_sum1 = -float('inf')
    #     for i in range(m-1):
    #         current_sum = nums[starting]
    #         ptr = starting
    #         while ptr + 1 < len(nums) and nums[ptr + 1] + current_sum <= average:
    #             current_sum += nums[ptr + 1]
    #             ptr += 1
    #         starting = ptr + 1
    #         max_sum1 = max(max_sum1, current_sum)
    #     max_sum1 = max(max_sum1, sum(nums[starting:]))
    #
    #     starting = len(nums) - 1
    #     max_sum2 = -float('inf')
    #     for i in range(m-1):
    #         current_sum = nums[starting]
    #         ptr = starting
    #         while ptr - 1 >= 0 and nums[ptr - 1] + current_sum <= average:
    #             current_sum += nums[ptr - 1]
    #             ptr -= 1
    #         starting = ptr - 1
    #         max_sum2 = max(max_sum2, current_sum)
    #     max_sum2 = max(max_sum2, sum(nums[:starting + 1]))
    #
    #     return min(max_sum1, max_sum2)


if __name__ == '__main__':
    print(Solution().splitArray(nums = [7,2,5,10,8], m = 2)) #18
    print(Solution().splitArray(nums = [1,2,3,4,5], m = 2)) #9
    print(Solution().splitArray(nums = [3,3,4], m = 2)) #6
    print(Solution().splitArray(nums = [1,4,4], m = 3)) #4
    print(Solution().splitArray([10,5,13,4,8,4,5,11,14,9,16,10,20,8], 8)) #25
    print(Solution().splitArray([2,3,1,2,4,3], 5)) #4
    print(Solution().splitArray([2,3,1,1,1,1,1], 5)) #3
    print(Solution().splitArray([5334,6299,4199,9663,8945,3566,9509,3124,6026,6250,7475,5420,9201,9501,38,5897,4411,6638,9845,161,9563,8854,3731,5564,5331,4294,3275,1972,1521,2377,3701,6462,6778,187,9778,758,550,7510,6225,8691,3666,4622,9722,8011,7247,575,5431,4777,4032,8682,5888,8047,3562,9462,6501,7855,505,4675,6973,493,1374,3227,1244,7364,2298,3244,8627,5102,6375,8653,1820,3857,7195,7830,4461,7821,5037,2918,4279,2791,1500,9858,6915,5156,970,1471,5296,1688,578,7266,4182,1430,4985,5730,7941,3880,607,8776,1348,2974,1094,6733,5177,4975,5421,8190,8255,9112,8651,2797,335,8677,3754,893,1818,8479,5875,1695,8295,7993,7037,8546,7906,4102,7279,1407,2462,4425,2148,2925,3903,5447,5893,3534,3663,8307,8679,8474,1202,3474,2961,1149,7451,4279,7875,5692,6186,8109,7763,7798,2250,2969,7974,9781,7741,4914,5446,1861,8914,2544,5683,8952,6745,4870,1848,7887,6448,7873,128,3281,794,1965,7036,8094,1211,9450,6981,4244,2418,8610,8681,2402,2904,7712,3252,5029,3004,5526,6965,8866,2764,600,631,9075,2631,3411,2737,2328,652,494,6556,9391,4517,8934,8892,4561,9331,1386,4636,9627,5435,9272,110,413,9706,5470,5008,1706,7045,9648,7505,6968,7509,3120,7869,6776,6434,7994,5441,288,492,1617,3274,7019,5575,6664,6056,7069,1996,9581,3103,9266,2554,7471,4251,4320,4749,649,2617,3018,4332,415,2243,1924,69,5902,3602,2925,6542,345,4657,9034,8977,6799,8397,1187,3678,4921,6518,851,6941,6920,259,4503,2637,7438,3893,5042,8552,6661,5043,9555,9095,4123,142,1446,8047,6234,1199,8848,5656,1910,3430,2843,8043,9156,7838,2332,9634,2410,2958,3431,4270,1420,4227,7712,6648,1607,1575,3741,1493,7770,3018,5398,6215,8601,6244,7551,2587,2254,3607,1147,5184,9173,8680,8610,1597,1763,7914,3441,7006,1318,7044,7267,8206,9684,4814,9748,4497,2239], 9)) #25
    print(Solution().splitArray([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,150,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,200,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,250,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,300,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,350,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,400,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,450,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,500,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,550,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,600,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,650,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,700,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,750,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,800,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,850,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,900,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,950,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 50)) #950
    print(Solution().splitArray([499,498,497,496,495,494,493,492,491,490,489,488,487,486,485,484,483,482,481,480,479,478,477,476,475,474,473,472,471,470,469,468,467,466,465,464,463,462,461,460,459,458,457,456,455,454,453,452,451,450,449,448,447,446,445,444,443,442,441,440,439,438,437,436,435,434,433,432,431,430,429,428,427,426,425,424,423,422,421,420,419,418,417,416,415,414,413,412,411,410,409,408,407,406,405,404,403,402,401,400,399,398,397,396,395,394,393,392,391,390,389,388,387,386,385,384,383,382,381,380,379,378,377,376,375,374,373,372,371,370,369,368,367,366,365,364,363,362,361,360,359,358,357,356,355,354,353,352,351,350,349,348,347,346,345,344,343,342,341,340,339,338,337,336,335,334,333,332,331,330,329,328,327,326,325,324,323,322,321,320,319,318,317,316,315,314,313,312,311,310,309,308,307,306,305,304,303,302,301,300,299,298,297,296,295,294,293,292,291,290,289,288,287,286,285,284,283,282,281,280,279,278,277,276,275,274,273,272,271,270,269,268,267,266,265,264,263,262,261,260,259,258,257,256,255,254,253,252,251,250,249,248,247,246,245,244,243,242,241,240,239,238,237,236,235,234,233,232,231,230,229,228,227,226,225,224,223,222,221,220,219,218,217,216,215,214,213,212,211,210,209,208,207,206,205,204,203,202,201,200,199,198,197,196,195,194,193,192,191,190,189,188,187,186,185,184,183,182,181,180,179,178,177,176,175,174,173,172,171,170,169,168,167,166,165,164,163,162,161,160,159,158,157,156,155,154,153,152,151,150,149,148,147,146,145,144,143,142,141,140,139,138,137,136,135,134,133,132,131,130,129,128,127,126,125,124,123,122,121,120,119,118,117,116,115,114,113,112,111,110,109,108,107,106,105,104,103,102,101,100,99,98,97,96,95,94,93,92,91,90,89,88,87,86,85,84,83,82,81,80,79,78,77,76,75,74,73,72,71,70,69,68,67,66,65,64,63,62,61,60,59,58,57,56,55,54,53,52,51,50,49,48,47,46,45,44,43,42,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0], 50)) #
