import collections


class Solution:
    def canJump(self, nums) -> bool:
        can_jump = [False] * len(nums)
        can_jump[-1] = True
        for i in range(len(nums) - 1, -1, -1):
            current_can_jump = False
            for j in range(i, min(len(nums), i + nums[i] + 1), 1):
                if can_jump[j]:
                    current_can_jump = True
                    break
            can_jump[i] = current_can_jump

        return can_jump[0]


if __name__ == '__main__':
    print(Solution().canJump([2,3,1,1,4]))
    print(Solution().canJump([3,2,1,0,4]))
