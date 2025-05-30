class Solution:
    def matrixSum(self, nums) -> int:
        sorted_mat = [sorted(nums[i]) for i in range(len(nums))]

        ans = 0
        for i in range(len(nums[0])):
            max_num = -1
            for j in range(len(nums)):
                max_num = max(max_num, sorted_mat[j].pop())
            ans += max_num

        return ans


if __name__ == '__main__':
    print(Solution().matrixSum(nums = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]))
    print(Solution().matrixSum(nums = [[1]]))
