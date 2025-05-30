import collections


class Solution:
    # # TLE 44/60
    # def isPossibleDivide(self, nums, k: int) -> bool:
    #     n = len(nums)
    #     if n % k != 0:
    #         return False
    #     nums.sort()
    #     while nums:
    #         count = 1
    #         ptr = 0
    #         current_num = nums[0]
    #         nums.remove(nums[0])
    #         while ptr < len(nums) and count < k:
    #             if nums[ptr] == current_num + 1:
    #                 count += 1
    #                 current_num = nums[ptr]
    #                 nums.remove(nums[ptr])
    #             else:
    #                 ptr += 1
    #         if count != k:
    #             return False
    #     return True

    def isPossibleDivide(self, nums, k: int) -> bool:
        n = len(nums)
        if n % k != 0:
            return False

        num_map = collections.Counter(nums)

        while num_map:
            current_num = min(num_map.keys())
            for i in range(k):
                if current_num + i in num_map:
                    num_map[current_num + i] -= 1
                    if num_map[current_num + i] == 0:
                        del num_map[current_num + i]
                else:
                    return False
        return True


if __name__ == '__main__':
    print(Solution().isPossibleDivide(nums = [1,2,3,3,4,4,5,6], k = 4))
    print(Solution().isPossibleDivide(nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3))
    print(Solution().isPossibleDivide(nums=[1, 2, 3, 4], k=3))
