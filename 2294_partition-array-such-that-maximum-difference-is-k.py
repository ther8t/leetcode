class Solution:
    def partitionArray(self, nums, k: int) -> int:
        nums.sort()
        n = len(nums)
        ptr1, ptr2 = 0, 0

        count = 0
        while ptr1 < n and ptr2 < n:
            ptr2 = ptr1 + 1
            while ptr2 < n and nums[ptr2] - nums[ptr1] <= k:
                ptr2 += 1
            count += 1
            ptr1 = ptr2

        return count


if __name__ == '__main__':
    print(Solution().partitionArray(nums = [2,2,4,5], k = 0))
