import collections


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats) -> int:
        # 0 - reserved, 1 - vacant
        row_reserved_map = collections.defaultdict(list)
        for row, col in reservedSeats:
            row_reserved_map[row].append(col)

        def get_row_vacancy(row):
            vacancy_num = 0
            for col in row_reserved_map[row]:
                vacancy_num += 1 << 10 - col

            return pow(2, 10) - 1 & ~vacancy_num

        # vacancies = [pow(2, 10) - 1] * (n + 1)
        # for row, col in reservedSeats:
        #     vacancies[row] &= (pow(2, 10) - 1 & ~ (1 << (10 - col)))

        ans = 2 * n
        for row in row_reserved_map.keys():
            vacancy = get_row_vacancy(row)
            left = vacancy & 0b0111100000 == 0b0111100000
            centre = vacancy & 0b0001111000 == 0b0001111000
            right = vacancy & 0b0000011110 == 0b0000011110

            if not left and not right and not centre:
                ans -= 2
                continue

            if left and right:
                continue

            if left or right or centre:
                ans -= 1
                continue

        return ans

    def decimalToBinary(self, n):
        return bin(n).replace("0b", "")

    # def maxNumberOfFamilies(self, n: int, reservedSeats) -> int:
    #     reservedSeats = {tuple(i) for i in reservedSeats}
    #     ans = 0
    #     for row in range(1, n + 1):
    #         left_aisle, centre, right_aisle = True, True, True
    #         for i in range(2, 6):
    #             if (row, i) in reservedSeats:
    #                 left_aisle = False
    #                 break
    #
    #         for i in range(4, 8):
    #             if (row, i) in reservedSeats:
    #                 centre = False
    #                 break
    #
    #         for i in range(6, 10):
    #             if (row, i) in reservedSeats:
    #                 right_aisle = False
    #                 break
    #
    #         if left_aisle and right_aisle:
    #             ans += 2
    #             continue
    #
    #         if left_aisle or right_aisle or centre:
    #             ans += 1
    #             continue
    #
    #     return ans


if __name__ == '__main__':
    print(Solution().maxNumberOfFamilies(n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]))
    print(Solution().maxNumberOfFamilies(n = 2, reservedSeats = [[2,1],[1,8],[2,6]]))
    print(Solution().maxNumberOfFamilies(n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]))