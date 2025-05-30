class Solution:
    def subsets(self, nums):
        n = len(nums)

        def a(index):
            if index == n:
                return [[]]
            out = []
            subsets = a(index + 1)
            for subset in subsets:
                out.append(subset)
                out.append(subset + [nums[index]])
            return out

        return a(0)

    # def subsets(self, nums):
    #     count = len(nums)
    #     all_subsets = []
    #
    #     def gen_subsets(level, stack):
    #         if level == count:
    #             all_subsets.append(stack)
    #             return
    #         gen_subsets(level + 1, stack)
    #         gen_subsets(level + 1, stack + [nums[level]])
    #
    #     gen_subsets(0, [])
    #     return all_subsets


if __name__ == '__main__':
    print(Solution().subsets([1,2,3]))
