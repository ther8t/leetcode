class Solution:
    def minimumSwaps(self, nums) -> int:
        minimum_num, maximum_num = float('inf'), -float('inf')
        min_index, max_index = 0, 0
        for i, num in enumerate(nums):
            if num < minimum_num:
                minimum_num = num
                min_index = i
            if num >= maximum_num:
                maximum_num = num
                max_index = i

        moves = len(nums) - max_index - 1 + min_index
        if min_index > max_index:
            moves -= 1
        return moves


if __name__ == '__main__':
    print(Solution().minimumSwaps(nums = [3,4,5,5,3,1]))
    print(Solution().minimumSwaps(nums = [9]))
