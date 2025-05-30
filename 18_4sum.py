import collections


class Solution:
    # def fourSum(self, nums, target):
    #
    #     def kSum(nums, target: int, k: int):
    #         res = []
    #
    #         # If we have run out of numbers to add, return res.
    #         if not nums:
    #             return res
    #
    #         # There are k remaining values to add to the sum. The
    #         # average of these values is at least target // k.
    #         average_value = target // k
    #
    #         # We cannot obtain a sum of target if the smallest value
    #         # in nums is greater than target // k or if the largest
    #         # value in nums is smaller than target // k.
    #         if average_value < nums[0] or nums[-1] < average_value:
    #             return res
    #
    #         if k == 2:
    #             return twoSum(nums, target)
    #
    #         for i in range(len(nums)):
    #             if i == 0 or nums[i - 1] != nums[i]:
    #                 for subset in kSum(nums[i + 1:], target - nums[i], k - 1):
    #                     res.append([nums[i]] + subset)
    #
    #         return res
    #
    #     def twoSum(nums, target: int):
    #         res = []
    #         lo, hi = 0, len(nums) - 1
    #
    #         while (lo < hi):
    #             curr_sum = nums[lo] + nums[hi]
    #             if curr_sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
    #                 lo += 1
    #             elif curr_sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
    #                 hi -= 1
    #             else:
    #                 res.append([nums[lo], nums[hi]])
    #                 lo += 1
    #                 hi -= 1
    #
    #         return res
    #
    #     nums.sort()
    #     return kSum(nums, target, 4)


    """
    Revision 2:
    This is a good question which I had left incomplete. The idea is to use two sums twice.
    The only problem is that in the case of [1, -1, 1] and target 0, there exist two pairs of [-1, 1] which add to target, 0.
    But there is only one -1 which is common between the two pairs. We need to make sure. This can be done by counter.

    but this question can be generalised to k sum. The solution given in the question suggests we use reducing k by selecting unique numbers from a sorted order.
    Why unique? So there may not be a repetition for the same iteration.
    Why Sorted? so you can have unique numbers.
    When the problem is reduced down to k = 2, use two sums, so the time complexity then becomes O(n^(k-1)).
    """
    def fourSum(self, nums, target):
        counter = collections.Counter(nums)
        two_sum_map = collections.defaultdict(list)
        out = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                two_sum_map[nums[i] + nums[j]].append((nums[i], nums[j]))

        visited = set()
        for two_sums in two_sum_map:
            for a, b in two_sum_map[two_sums]:
                if (a, b) in visited:
                    continue
                visited.add((a, b))
                visited.add((b, a))
                if target - two_sums not in two_sum_map:
                    continue
                for c, d in two_sum_map[target - two_sums]:
                    sum_counter = collections.Counter([c, d, a, b])
                    is_valid = True
                    for k in sum_counter:
                        if sum_counter[k] > counter[k]:
                            is_valid = False
                            break
                    if is_valid:
                        out.add(tuple(sorted([c, d, a, b])))

        return list(out)

    # def fourSum(self, nums, target):
    #     nums.sort()
    #     return self.fourSumRecursive(nums, target, 4)
    #
    # def fourSumRecursive(self, nums, target, level):
    #     if level == 0:
    #         if target == 0:
    #             return [[]]
    #         else:
    #             return None
    #     output = []
    #     left = 0
    #     right = len(nums) - 1
    #     if target > nums[right] or target < nums[left]:
    #         return output
    #     while left <= right:
    #         # if (nums[left] + nums[right]) > target:
    #         #     right -= 1
    #         #     continue
    #         # elif (nums[left] + nums[right]) < target:
    #         #     left += 1
    #         #     continue
    #         subFourSum = self.fourSumRecursive(nums[left + 1:], target - nums[left], level - 1)
    #         if subFourSum is not None and len(subFourSum) > 0:
    #             # found atleast one solution
    #             for j in range(len(subFourSum)):
    #                 output.append([nums[left]] + subFourSum[j])
    #             while left + 1 < len(nums) and nums[left] == nums[left + 1]:
    #                 left += 1
    #         left += 1
    #     return output


    """
    Attempt #2:
    Accepted 82%
    Ok so this is interesting.
    The problem statement demands that we take two sums and then find two sums over that.
    The problem is overlapping index, which I solved by checking indexes.
    But since we dont have to put all the unique indexes in the final answer, we put unique numbers,
    we need to optimize by checking if a particular combination of numbers has been done or not.
    """
    def fourSum(self, nums, target):
        sum_index_map = collections.defaultdict(set)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sum_index_map[nums[i] + nums[j]].add((i, j))

        ans = set()
        visited = set()
        for sum1 in sum_index_map.keys():
            if target - sum1 in sum_index_map:
                for sum1_member in sum_index_map[sum1]:
                    if (nums[sum1_member[0]], nums[sum1_member[1]]) in visited:
                        continue
                    visited.add((nums[sum1_member[0]], nums[sum1_member[1]]))
                    visited.add((nums[sum1_member[1]], nums[sum1_member[0]]))
                    for sum2_member in sum_index_map[target - sum1]:
                        if sum1_member[0] not in sum2_member and sum1_member[1] not in sum2_member:
                            a = []
                            for m in sum1_member:
                                a.append(nums[m])
                            for m in sum2_member:
                                a.append(nums[m])

                            ans.add(tuple(sorted(a)))

        return ans


if __name__ == '__main__':
    # print(Solution().fourSum(nums = [1,0,-1,0,-2,2], target = 0))
    # print(Solution().fourSum(nums = [2,2,2,2,2], target = 8))
    print(Solution().fourSum([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90], 200))
    print(Solution().fourSum([-476,-471,-457,-449,-444,-444,-423,-419,-417,-404,-398,-392,-382,-382,-369,-358,-352,-352,-344,-305,-300,-297,-291,-272,-271,-268,-266,-253,-249,-222,-172,-161,-126,-124,-106,-104,-101,-101,-89,-71,-68,-67,-45,-37,-26,-23,-18,-17,-15,7,17,29,73,77,84,84,106,118,122,128,140,146,191,201,214,220,234,240,257,264,296,301,314,320,332,336,339,363,396,422,435,457,477,478,478,485,487]
, -6401))
    # a = [[]]
    # print(a)
    # [-5, -4, -3, -2, 1, 3, 3, 5]
