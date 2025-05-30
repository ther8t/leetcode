class Solution:
    """
    This solution is the same implemented in 41_first-missing-positive.
    This works only because there is no 0 and the numbers are positive contineous [1, n] only.
    Since there is no 0, the number at index 0 is misplaced. That number is sent to its correct place, then the number it replaces is placed in its correct position. This goes on.
    Had it been a 1 indexed array or 0 been included, there would be a case where in [0, 3, 2, 1] 0 is placed in the correct place and it returns 0 as the duplicate number.
    """
    def findDuplicate(self, nums) -> int:
        def find(current):
            if current == nums[current]:
                return current
            next = nums[current]
            nums[current] = current

            return find(next)

        return find(0)

    def findDuplicate(self, nums) -> int:
        n = len(nums) - 1
        return sum(nums) - n * (n + 1) // 2


if __name__ == '__main__':
    print(Solution().findDuplicate(nums = [1,3,4,2,2]))
    print(Solution().findDuplicate(nums = [3,1,3,4,2]))
