import collections
import datetime
import functools


class Solution:

    """
    Attempt #2
    TLE
    """
    def makesquare(self, matchsticks: list) -> bool:
        perimeter = sum(matchsticks)
        if perimeter % 4 != 0:
            return False
        side = perimeter // 4
        counter = collections.Counter(matchsticks)


        def canMake(square_side, current_side_length):
            if square_side == 4 and len(counter) == 0:
                return True

            can_make = False
            keys = counter.keys()
            for length in keys:
                if can_make:
                    return True
                if current_side_length + length > side:
                    continue
                if current_side_length + length <= side:
                    length_count = counter[length]
                    counter[length] = length_count - 1
                    if counter[length] == 0:
                        counter.pop(length)
                    if current_side_length + length == side:
                        can_make = canMake(square_side + 1, 0)
                    else:
                        can_make = canMake(square_side, current_side_length + length)
                    counter[length] = length_count

            return can_make

        return canMake(0, 0)


    """
    Attempt #2
    Accepted 91%
    This one was a bit tricky. I had to run through multiple permutation of methods to make sure, I arrive at the solution.
    The major issue with this was the terminal condition. I had to ensure that even in the terminal condition, a check for the sum was present.
    """
    def makesquare(self, matchsticks: list) -> bool:
        perimeter = sum(matchsticks)
        if perimeter % 4 != 0:
            return False
        side = perimeter // 4
        counter = collections.Counter(matchsticks)
        available_lengths = sorted(counter.keys())
        sums = set()

        def k_sum(arr, arr_sum, index):
            if arr_sum == side:
                sums.add(tuple(sorted(arr)))
                return
            if index >= len(matchsticks):
                return
            if arr_sum > side:
                return

            k_sum(arr + [matchsticks[index]], arr_sum + matchsticks[index], index + 1)
            k_sum(arr, arr_sum, index + 1)
            # for m_len in range(index, len(matchsticks)):
            #     pass

        def is_available(arr):
            temp_counter = collections.Counter(arr)
            for i in temp_counter.keys():
                if counter[i] < temp_counter[i]:
                    return False
            return True

        def can_square(side_index):
            if side_index == 4:
                return True

            can_form = False
            for side_sticks in sums:
                if can_form:
                    return True
                if is_available(side_sticks):
                    for sticks in side_sticks:
                        counter[sticks] -= 1
                    can_form = can_square(side_index + 1)
                    for sticks in side_sticks:
                        counter[sticks] += 1

            return can_form

        k_sum([], 0, 0)
        return can_square(0)


    # def makesquare(self, matchsticks: list) -> bool:
    #     n = len(matchsticks)
    #     perimeter = sum(matchsticks)
    #     if perimeter % 4 != 0:
    #         return False
    #     side = perimeter // 4
    #
    #     square_sides = {0:[], 1:[], 2:[], 3:[]}
    #
    #     def can_square(index):
    #         if index == n:
    #             for i in range(4):
    #                 if sum(square_sides[i]) != side:
    #                     return False
    #             return True
    #
    #         is_possible = False
    #         for i in range(4):
    #             if is_possible:
    #                 return True
    #             if sum(square_sides[i]) > side:
    #                 continue
    #             square_sides[i].append(matchsticks[index])
    #             is_possible = can_square(index + 1)
    #             square_sides[i].pop()
    #
    #         return is_possible
    #
    #     return can_square(0)

    """
    Attempt: Fired
    Accepted: 78%
    """
    def makesquare(self, matchsticks: list) -> bool:
        perimeter = sum(matchsticks)
        if perimeter % 4 != 0:
            return False
        side = perimeter // 4
        sticks_count_map = collections.Counter(matchsticks)
        all_sides = set()

        def sides(index, current_sum, stack):
            if index >= len(matchsticks) or current_sum > side:
                return
            if current_sum == side:
                all_sides.add(tuple(stack))

            sides(index + 1, current_sum, stack)
            sides(index + 1, current_sum + matchsticks[index], stack + [matchsticks[index]])

        # def match(sides_done, available, current_sum):
        #     if sides_done == 4 and len(available) == 0:
        #         return True
        #
        #     does_match = False
        #     for i, stick in enumerate(available):
        #         if does_match:
        #             return True
        #         if current_sum + stick > side:
        #             continue
        #         elif current_sum + stick == side:
        #             does_match = match(sides_done + 1, available[:i] + available[i + 1:], 0)
        #         else:
        #             does_match = match(sides_done, available[:i] + available[i + 1:], current_sum + stick)
        #
        #     return does_match

        def gather_sides(sides_completed):
            if sides_completed == 4:
                return True
            for permutation in all_sides:
                current_permutation_map = collections.Counter(permutation)
                can_use_side = True
                for s in current_permutation_map.keys():
                    if sticks_count_map[s] < current_permutation_map[s]:
                        can_use_side = False
                        break
                if can_use_side:
                    for s in current_permutation_map:
                        sticks_count_map[s] -= current_permutation_map[s]
                    can_form_square = gather_sides(sides_completed + 1)
                    if can_form_square:
                        return True
                    for s in current_permutation_map:
                        sticks_count_map[s] += current_permutation_map[s]
            return False


        sides(-1, 0, [])
        return gather_sides(0)




if __name__ == '__main__':
    print(Solution().makesquare([1,1,2,2,2]))
    print(Solution().makesquare([3, 3, 3, 3, 4]))
    print(Solution().makesquare([2,2,2,3,4,4,4,5,6]))
    print(Solution().makesquare([5,5,5,5,16,4,4,4,4,4,3,3,3,3,4]))
    print(Solution().makesquare([97,13,66,41,9,22,1,93,11,65,61,12,41,1,59])) #True
    print(Solution().makesquare([4,13,1,1,14,15,1,3,13,1,3,5,2,8,12])) #False
    print(Solution().makesquare([4,8,12,16,20,24,28,32,36,40,44,48,52,56,60])) #True
