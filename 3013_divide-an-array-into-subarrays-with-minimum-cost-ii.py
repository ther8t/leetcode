import sortedcontainers


class Solution:
    def minimumCost(self, nums, k: int, dist: int) -> int:
        n = len(nums)
        min_sum = float('inf')
        window = sortedcontainers.SortedList(nums[n - dist:n])
        for i in range(len(nums) - 1, -1, -1):
            second_index, k_index = i - dist, i
            window.remove(nums[k_index])
            if second_index > 0:
                window.add(nums[second_index])
            if len(window) < k - 2:
                break
            min_sum = min(min_sum, nums[0] + nums[k_index] + sum(window[:k - 2]))

        return min_sum


if __name__ == '__main__':
    print(Solution().minimumCost(nums = [1,3,2,6,4,2], k = 3, dist = 3))
    print(Solution().minimumCost(nums = [10,1,2,2,2,1], k = 4, dist = 3))
    print(Solution().minimumCost(nums = [10,8,18,9], k = 3, dist = 1))
    print(Solution().minimumCost([1,5,3,6], 3, 2))
