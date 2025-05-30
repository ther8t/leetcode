class Solution:
    def getMaxLen(self, nums) -> int:
        ptr1, ptr2 = 0, 0
        max_range = 0
        while ptr1 < len(nums) and ptr2 < len(nums):
            negative_count = 0
            first_negative_index = -1
            last_negative_index = -1
            while ptr2 < len(nums) and nums[ptr2] != 0:
                if nums[ptr2] < 0:
                    last_negative_index = ptr2
                    negative_count += 1
                    if first_negative_index == -1:
                        first_negative_index = last_negative_index
                ptr2 += 1

            s, t = ptr1, ptr2 - 1
            if negative_count % 2 == 0:
                max_range = max(max_range, t - s + 1)
            else:
                max_range = max(max_range, t - (first_negative_index + 1) + 1, last_negative_index - 1 - s + 1)

            while ptr2 < len(nums) and nums[ptr2] == 0:
                ptr2 += 1

            ptr1 = ptr2

        return max_range


if __name__ == '__main__':
    print(Solution().getMaxLen(nums = [1,-2,-3,4]))
    print(Solution().getMaxLen(nums = [0,1,-2,-3,-4]))
    print(Solution().getMaxLen(nums = [-1,-2,-3,0,1]))
