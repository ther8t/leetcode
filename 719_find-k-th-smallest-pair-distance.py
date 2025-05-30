import collections

import sortedcontainers


class Solution:
    def smallestDistancePair(self, nums, k: int) -> int:
        nums.sort()
        n = len(nums)

        def distance_count(distance):
            count = 0
            i, j = 0, 0
            while i < n:
                while j < n and nums[j] - nums[i] <= distance:
                    j += 1
                count += (j - i - 1)
                i += 1
            return count

        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if distance_count(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left


    # # TLE
    # def smallestDistancePair(self, nums, k: int) -> int:
    #     nums_counter = collections.Counter(nums)
    #     unique_nums = list(nums_counter.keys())
    #     diff_map = collections.defaultdict(list)
    #
    #     for i in range(len(unique_nums)):
    #         for j in range(i, len(unique_nums)):
    #             if i!=j or (i == j and nums_counter[unique_nums[i]] > 1):
    #                 diff_map[abs(unique_nums[i] - unique_nums[j])].append((unique_nums[i], unique_nums[j]))
    #
    #     counter = 0
    #     for diff in sorted(diff_map.keys()):
    #         for num1, num2 in diff_map[diff]:
    #             if num1 == num2:
    #                 counter += nums_counter[num1] * (nums_counter[num1] - 1) // 2
    #             else:
    #                 counter += nums_counter[num1] * nums_counter[num2]
    #             if k <= counter:
    #                 return diff
    #     return -1

    # # TLE
    # def smallestDistancePair(self, nums, k: int) -> int:
    #     nums_counter = collections.Counter(nums)
    #     nums_max = max(nums)
    #
    #     diff = 0
    #     counter = 0
    #     while diff < nums_max:
    #         for n in nums_counter:
    #             if (n + diff) in nums_counter:
    #                 counter += nums_counter[n] * nums_counter[n + diff] if diff > 0 else nums_counter[n] * (nums_counter[n] - 1) // 2
    #                 if k <= counter:
    #                     return diff
    #         diff += 1
    #
    #     return -1


if __name__ == '__main__':
    print(Solution().smallestDistancePair(nums = [1,3,1], k = 1))
    print(Solution().smallestDistancePair(nums = [1,1,1], k = 2))
    print(Solution().smallestDistancePair(nums = [1,6,1], k = 3))
    print(Solution().smallestDistancePair([221238,427286,829789,601893,358469,46342,598804,666075,725560,842824,261672,391778,964604,53621,533121,755551,807344,597092,774256,63098,948199,579547,3196,909877,95910,965027,411050,532303,362036,248585,389213,926908,139846,642116,527660,735487,787738,978186,545605,595011,705832,788214,407493,856161,947455,114342,459338,744156,179687,348085,724897,694016,170072,797188,194673,987604,748362,124575,101059,588749,515935,846183,783882,752572,984672,299643,474986,42219,914392,699717,862520,146910,156305,269341,268361,19009,292092,663200,349590,296229,194323,667426,751544,139621,339144,979848,895018,432652,524214,697568,946806,378351,536203,315145,567426,212742,871720,419529,340374,869276,865407,603396,609939,616585,590359,21031,813301,154998,592050,679203,535025,94441,193548,618901,170094,996902,981372,129574,272754,762181,746001,525671,398300,912121,682153,5904,473065,729188,727720,183096,851216,848578,908443,532556,369537,800932,713898,919800,350740,851358,734571,674194,624352,862486,254700,127824,705571,61267,335237,377466,124085,542898,263565,867445,570415,909045,947063,167541,113129,897668,402701,287017,87703,233079,67973,689618,433223,164387,627387,472038,97781,148808,263578,28836,226968,476149,778104,404041,300170,319580,355689,713032,92394,739268,614862,716425,260673,449432,607545,987946,243679,147202,111207,598535,676528,107358,372982,190321,217552,501122], 10000))
