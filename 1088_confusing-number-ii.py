import collections


class Solution:
    def resolve_number(self, number):
        resolved_number = 0
        for i in range(len(number) - 1, -1, -1):
            resolved_number += (int(number[i]) * pow(10, len(number) - 1 - i))
        return resolved_number

    def remove_trailing_zeros(self, number):
        non_zero_ptr = -1
        for i in range(len(number)):
            if number[i] == 0:
                non_zero_ptr += 1
            else:
                break
        return number[non_zero_ptr + 1:]

    def rotated_number(self, number):
        map = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        reversed_number = []
        for i in range(len(number) - 1, -1, -1):
            reversed_number.append(map[number[i]])
        return reversed_number

    def is_confusing(self, number):
        number = self.remove_trailing_zeros(number)

        reversed_number = self.rotated_number(number)
        reversed_number = self.remove_trailing_zeros(reversed_number)

        return not self.resolve_number(number) == self.resolve_number(reversed_number)

    def confusingNumberII(self, n: int) -> int:
        valid_digits = [0, 1, 6, 8, 9]

        rank = 0
        n_temp = n
        n_split = []
        for i in range(10):
            if n_temp > 0:
                n_split.append(n_temp % 10)
                rank += 1
            else:
                break
            n_temp //= 10
        n_split.reverse()

        def how_many_numbers_before(number):
            if len(number) == 0:
                return 1
            digits_allowed_at_index = 0
            for i in valid_digits:
                if i < number[0]:
                    digits_allowed_at_index += 1
            if number[0] not in valid_digits:
                return digits_allowed_at_index * pow(len(valid_digits), len(number) - 1)
            else:
                return digits_allowed_at_index * pow(len(valid_digits), len(number) - 1) + how_many_numbers_before(
                    number[1:])

        def how_many_numbers_not_before(number, index, rank):
            if rank == 0:
                return 0
            if rank < len(number) and index == -1:
                # everything is allowed
                # calculate every possible rotatable number of length rank or below
                return (3 * pow(4, rank // 2) if rank % 2 == 1 else pow(4, rank // 2)) + how_many_numbers_not_before(
                    number, index, rank - 1)
            digits_allowed_at_index = []
            for i in valid_digits:
                if i < number[index]:
                    digits_allowed_at_index.append(i)
            if index == 0:
                # 0 not allowed at first position
                if 0 in digits_allowed_at_index:
                    digits_allowed_at_index.remove(0)

            if len(number) % 2 == 1 and index == len(number) // 2:
                if 6 in digits_allowed_at_index: digits_allowed_at_index.remove(6)
                if 9 in digits_allowed_at_index: digits_allowed_at_index.remove(9)

            remaining = 1
            if len(number) > 2:
                remaining = 3 * pow(4, (len(number) // 2 - 1)) if len(number) % 2 == 1 else pow(4,
                                                                                                (len(
                                                                                                    number) // 2 - 1))

            all_lower_numbers = len(digits_allowed_at_index) * remaining + how_many_numbers_not_before(number, -1, rank - 1)

            if number[0] not in valid_digits:
                # fill the remaining
                return all_lower_numbers
            else:
                return all_lower_numbers + how_many_numbers_not_before(number, index + 1, rank - 2)

        return how_many_numbers_before(n_split) - how_many_numbers_not_before(n_split, 0, rank)

    # # TLE
    # def confusingNumberII(self, n: int) -> int:
    #     valid_digits = [0, 1, 6, 8, 9]
    #
    #     total_count = 0
    #
    #     def digit_maker():
    #         digit_array = []
    #         level = 9
    #         counter = pow(len(valid_digits), level)
    #         ptrs = []
    #         confusing_count = 0
    #         for i in range(level):
    #             ptrs.append(0)
    #         while counter > 0:
    #             for _ in range(len(valid_digits)):
    #                 # create a number
    #                 number = []
    #                 for ptr in ptrs:
    #                     number.append(valid_digits[ptr])
    #                 if self.resolve_number(number) > n:
    #                     return confusing_count
    #                 if self.is_confusing(number):
    #                     confusing_count += 1
    #                 counter -= 1
    #                 ptrs[-1] += 1
    #
    #             # update the pointers
    #             carry = 0
    #             for j in range(len(ptrs) - 1, 0, -1):
    #                 # carry = (carry + ptrs[j])%(len(valid_digits))
    #                 # ptrs[j] = (carry + ptrs[j])//(len(valid_digits))
    #                 if ptrs[j] == len(valid_digits):
    #                     ptrs[j] = 0
    #                     ptrs[j - 1] += 1
    #
    #         return confusing_count
    #
    #     return digit_maker()

    # # TLE
    # def confusingNumberII(self, n: int) -> int:
    #     valid_digits = [0, 1, 6, 8, 9]
    #     total_count = 0
    #
    #     max_level = 1
    #     n_temp = n
    #     for i in range(10):
    #         if n_temp > 0:
    #             max_level += 1
    #         else:
    #             break
    #         n_temp //= 10
    #
    #     def dfs(stack, level):
    #         nonlocal total_count
    #         if level == max_level:
    #             if self.resolve_number(stack) > n:
    #                 return True
    #             if self.is_confusing(stack):
    #                 total_count += 1
    #         elif level < max_level:
    #             for i in valid_digits:
    #                 stack.append(i)
    #                 is_over = dfs(stack, level + 1)
    #                 if is_over:
    #                     return True
    #                 stack.pop()
    #
    #     dfs([], 1)
    #     return total_count

    """
    Revision 2:
    This is a BFS question it turns out. Like most of the problem Google asks this was a BFS/DFS too.
    Aside from solving this particular problem, it taught me something else more important as well.
    I had the habit of using queue.pop(0) while popping. The thing is that pop() is an O(1) operation because it aims at the last element.
    pop(0) on the other hand is O(N) each time, which makes it a really bad choice. Use collections.deque instead.
    
    This question is kind of similar to 818_race-car. In the sense that they both begin from a certain point and progress further incrementally.
    In the case of race car problem. The car progresses by one command and we need to calculate the minimum command. Each step is like progressing, one step down into a tree.
    In the case of this problem. The numbers start from a certain non-zero digit and adding a number is like progressing one step down into a tree.
    This is an important observation. Keep this in mind and see if the question requires some incremental progression.
    """
    def confusingNumberII(self, n: int) -> int:
        number_inverse_map = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        queue = collections.deque([(1, 1, 10), (6, 9, 10), (8, 8, 10), (9, 6, 10)])
        count = 0

        while queue:
            number, inverse_number, unit = queue.popleft()
            if number <= n and number != inverse_number:
                count += 1

            for i in number_inverse_map:
                if number * 10 + i <= n:
                    queue.append((number * 10 + i, number_inverse_map[i] * unit + inverse_number, unit * 10))
                else:
                    break

        return count





if __name__ == '__main__':
    # print(Solution().confusingNumberII(20))  # 389627
    # print(Solution().confusingNumberII(100))  # 389627
    print(Solution().confusingNumberII(10**9))  # 389627
    # print(Solution().confusingNumberII(195))  # 389627
    # print(Solution().confusingNumberII(555))  # 389627
    # print(Solution().confusingNumberII(642))  # 389627
    # print(Solution().confusingNumberII(666))  # 389627
