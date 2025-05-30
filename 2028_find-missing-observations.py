class Solution:
    def missingRolls(self, rolls, mean: int, n: int):
        m = len(rolls)
        total_sum = mean * (n + m)
        sum_n = total_sum - sum(rolls)
        average_dice_number = sum_n // n
        if average_dice_number < 1 or average_dice_number > 6:
            return []
        ans = [average_dice_number] * n
        sum_n -= average_dice_number * n

        for i in range(len(ans)):
            if sum_n:
                ans[i] += 1
                sum_n -= 1
                if ans[i] > 6:
                    return []

        return ans

    """
    Attempt #2
    Accepted 96%
    A simple enough change. At first I used to check with average dice number for n remaining. But now I check for sum as a whole.
    """
    def missingRolls(self, rolls, mean: int, n: int):
        m = len(rolls)
        total_sum = mean * (n + m)
        sum_n = total_sum - sum(rolls)
        average_dice_number = sum_n // n
        if sum_n < n or sum_n > 6 * n:
            return []
        ans = [average_dice_number] * n
        sum_n -= average_dice_number * n

        for i in range(len(ans)):
            if sum_n:
                ans[i] += 1
                sum_n -= 1

        return ans


    def missingRolls(self, rolls, mean: int, n: int):
        m = len(rolls)
        total_sum = mean * (n + m)
        sum_n = total_sum - sum(rolls)
        average_dice_number = sum_n // n
        if sum_n < n or sum_n > 6 * n:
            return []
        a = [average_dice_number] * n
        sum_n -= average_dice_number * n
        for i in range(n):
            if sum_n == 0:
                break
            a[i] += 1
            sum_n -= 1

        return a

if __name__ == '__main__':
    print(Solution().missingRolls(rolls = [3,2,4,3], mean = 4, n = 2))
    print(Solution().missingRolls(rolls = [1,5,6], mean = 3, n = 4))
    print(Solution().missingRolls(rolls = [1,2,3,4], mean = 6, n = 4))
    print(Solution().missingRolls([6,3,4,3,5,3], 1, 6))
    print(Solution().missingRolls([3,5,3], 5, 3))
    print(Solution().missingRolls([4,5,6,2,3,6,5,4,6,4,5,1,6,3,1,4,5,5,3,2,3,5,3,2,1,5,4,3,5,1,5], 4, 40))
