class Solution:
    """
    Accepted 84%
    """
    def findNthDigit(self, n: int) -> int:
        number_counter = [0, 9, 90, 900, 9000, 90000, 900000, 9000000, 90000000,  900000000, 9000000000, 90000000000, 900000000000]

        def get_range(num):
            digit_count = 0
            for i in range(11):
                if num // (10 ** i) == 0:
                    digit_count = i
                    break
            smaller_count = 0
            for i in range(1, digit_count):
                smaller_count += number_counter[i] * i

            until_number_counter = (num // (10 ** (digit_count - 1)) - 1) * (10 ** (digit_count - 1)) * digit_count + (num % (10 ** (digit_count - 1))) * digit_count

            return smaller_count + until_number_counter + 1, smaller_count + until_number_counter + digit_count

        lo, hi = 1, 2 ** 31 - 1
        number_found = 1
        range_start, range_end = 1, 2 ** 31 - 1
        while lo < hi:
            mid = (lo + hi) // 2
            start, end = get_range(mid)
            if start <= n <= end:
                number_found = mid
                range_start, range_end = start, end
                break
            if n < start:
                hi = mid
            if n > end:
                lo = mid

        print(number_found, range_start, range_end)
        return int(str(number_found)[n - range_start])


if __name__ == '__main__':
    # print(Solution().findNthDigit(11))
    print(Solution().findNthDigit(2147483647))
