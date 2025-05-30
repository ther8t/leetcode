class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        high = str(int(high) + 1)
        strobogrammatic_numbers = [0, 1, 6, 8, 9]

        # calculates all the possible numbers of the length
        def get_all_numbers(length):
            if length % 2 == 0:
                return 4 * pow(5, (length - 2) // 2)
            else:
                return pow(4, 1 if length > 1 else 0) * pow(5, (length - 2) // 2) * 3

        # calculates all the strobogrammatic numbers strictly greater than. Although it's an overkill, you could write this in code itself.
        def all_strobogrammatic_strictly_greater_than(number):
            number = int(number)
            counter = 0
            for n in strobogrammatic_numbers:
                if n > number:
                    counter += 1
            return counter

        # Calculates all the numbers which are greater than the given argument but only of the same length. So even though 1111 > 809, it won't be included.
        def get_all_numbers_greater_than(number):
            if len(number) == 0:
                return 1
            if len(number) == 1:
                counter = 0
                for n in [0, 1, 8]:
                    if n >= int(number):
                        counter += 1
                return counter

            power_strictly_greater = all_strobogrammatic_strictly_greater_than(number[0])
            if len(number) > 2:
                length_remaining = len(number) - 2
                if length_remaining % 2 == 0:
                    power_strictly_greater *= (pow(5, (length_remaining) // 2))
                else:
                    power_strictly_greater *= (pow(5, (length_remaining) // 2) * 3)

            same_power_place = 0
            if int(number[0]) in strobogrammatic_numbers:
                same_power_place += get_all_numbers_greater_than(number[1:len(number) - 1])

                # last digit must agree with the first one.
                same_power_place += 0 if (int(number[0]) in [0, 1, 8] and number[len(number) - 1] <= number[0]) or (
                        number[0] == '6' and number[len(number) - 1] <= '9') or (
                                                 number[0] == '9' and number[len(number) - 1] <= '6') else -1

            return power_strictly_greater + same_power_place

        if len(low) < len(high):
            middle_numbers = 0
            for i in range(len(low) + 1, len(high)):
                middle_numbers += get_all_numbers(i)

            return get_all_numbers_greater_than(low) + middle_numbers + (
                        get_all_numbers(len(high)) - get_all_numbers_greater_than(high))
        else:
            return get_all_numbers_greater_than(low) - get_all_numbers_greater_than(high)


if __name__ == '__main__':
    print(Solution().strobogrammaticInRange("0", "9"))
