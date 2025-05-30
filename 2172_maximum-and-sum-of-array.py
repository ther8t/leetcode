import collections
from functools import lru_cache


class Solution:
    # # TLE
    # def maximumANDSum(self, nums, numSlots):
    #     slots = {i: [] for i in range(1, numSlots + 1)}
    #     and_sum_exact_match = 0
    #     for i in range(1, numSlots + 1):
    #         try:
    #             while len(slots[i]) < 2 and nums.index(i):
    #                 slots[i].append(i)
    #                 nums.remove(i)
    #                 and_sum_exact_match += i
    #         except:
    #             pass
    #
    #     nums.sort(reverse=True)
    #
    #     num_possible_slot_map = {}
    #     scores_nums_map = collections.defaultdict(list)
    #     for num in nums:
    #         possible_slots = []
    #         for i in slots:
    #             if len(slots[i]) == 2:
    #                 continue
    #             possible_slots.append((num & i, i))
    #             scores_nums_map[num & i].append((num, i))
    #         num_possible_slot_map[num] = sorted(possible_slots, reverse=True)
    #
    #     def backtrack(nums, slots):
    #         if len(nums) == 0:
    #             return 0
    #         max_and_sum = -1
    #         for and_sum, slot in num_possible_slot_map[nums[0]]:
    #             if len(slots[slot]) == 2:
    #                 continue
    #             slots[slot].append(nums[0])
    #             current_and_sum = and_sum + backtrack(nums[1:], slots)
    #             max_and_sum = max(max_and_sum, current_and_sum)
    #             slots[slot].remove(nums[0])
    #         return max_and_sum
    #
    #     return and_sum_exact_match + backtrack(nums, slots)

    # def maximumANDSum(self, nums, numSlots):
    #     slots = {i: [] for i in range(1, numSlots + 1)}
    #     and_sum_exact_match = 0
    #     for i in range(1, numSlots + 1):
    #         try:
    #             while len(slots[i]) < 2 and nums.index(i):
    #                 slots[i].append(i)
    #                 nums.remove(i)
    #                 and_sum_exact_match += i
    #         except:
    #             pass
    #
    #     nums.sort(reverse=True)
    #
    #     all_possible_score_num_slot = []
    #     for num in nums:
    #         for i in slots:
    #             if len(slots[i]) == 2:
    #                 continue
    #             all_possible_score_num_slot.append((num & i, num, i))
    #
    #     all_possible_score_num_slot.sort(reverse=True)
    #
    #     max_score = 0
    #     for i in range(len(all_possible_score_num_slot)):
    #         temp_nums = nums.copy()
    #         temp_slots = {i: slots[i].copy() for i in slots}
    #         score = 0
    #         ptr = i
    #         while len(temp_nums) > 0 and ptr < len(all_possible_score_num_slot):
    #             current_score, number, slot = all_possible_score_num_slot[ptr]
    #             if number in temp_nums and len(temp_slots[slot]) < 2:
    #                 temp_nums.remove(number)
    #                 score += current_score
    #                 temp_slots[slot].append(number)
    #             ptr += 1
    #
    #         if not temp_nums:
    #             max_score = max(max_score, score)
    #     print(slots)
    #     return and_sum_exact_match + max_score

    # def maximumANDSum(self, nums, numSlots):
    #
    #     @lru_cache(None)
    #     def fill_slots(pos, conf):
    #         if pos == len(nums):
    #             return 0
    #         score = 0
    #         for slot in range(1, numSlots + 1):
    #             base = 10 ** (slot - 1)
    #             left = conf // base % 10
    #             if left > 0:
    #                 score = max(score, (nums[pos] & slot) + fill_slots(pos + 1, conf - base))
    #         return score
    #
    #     slots = {i: [] for i in range(1, numSlots + 1)}
    #     and_sum_exact_match = 0
    #     conf = int('2' * numSlots)
    #     for i in range(1, numSlots + 1):
    #         try:
    #             while len(slots[i]) < 2 and nums.index(i):
    #                 slots[i].append(i)
    #                 nums.remove(i)
    #                 conf = conf - (10 ** (i - 1))
    #                 and_sum_exact_match += i
    #         except:
    #             pass
    #     return and_sum_exact_match + fill_slots(0, conf)


    """
    Revision 2:
    I solved this question almost without looking at the solution. Almost because I started with the same line of thought which I did when I did this question for the first time.
    However, @lru_cache was the biggest hint. I knew at that point that I could do a backtrack. I could use dp/cache to store the function call.
    I remembered it from last time that I had to do something about the conf because python's string conversion is O(n).
    """
    def maximumANDSum(self, nums, numSlots):
        n = len(nums)
        BASE = 10

        @lru_cache(None)
        def fill_slot(num_index, conf):
            if num_index == n:
                return 0

            score = 0
            for slot in range(1, numSlots + 1):
                slot_position = slot - 1
                left = (conf // BASE ** slot_position) % BASE
                if left:
                    score = max(score, (slot & nums[num_index]) + fill_slot(num_index + 1, conf - BASE ** slot_position))
            return score

        return fill_slot(0, int('2' * numSlots))


if __name__ == '__main__':
    print(Solution().maximumANDSum(nums = [1,2,3,4,5,6], numSlots = 3))  # 9
    print(Solution().maximumANDSum([14, 7, 9, 8, 2, 4, 11, 1, 9], 8))  # 40
    print(Solution().maximumANDSum([15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15], 9)) #90
    print(Solution().maximumANDSum([7, 6, 13, 13, 13, 6, 3, 12, 6, 4, 10, 3, 2], 7)) #54
