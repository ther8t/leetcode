class Solution:
    def maxProduct(self, nums: list) -> int:
        if len(nums) == 1:
            return nums[0]

        num_splits = []
        previous_split = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                if previous_split + 1 != i:
                    num_splits.append(nums[previous_split + 1:i])
                previous_split = i

        if previous_split + 1 != len(nums):
            num_splits.append(nums[previous_split + 1:len(nums)])

        ans = 0
        for a in num_splits:
            counter = 0
            first, last = -1, len(a)
            first_product, last_product = 1, 1
            product = 1
            for i in range(len(a)):
                product *= a[i]
                last_product *= a[i]
                if first == -1:
                    first_product *= a[i]
                if a[i] < 0:
                    counter += 1
                    if first == -1:
                        first = i
                    last = i
                    last_product = a[i]
            if counter % 2 == 0:
                ans = max(ans, product)
            else:
                ans = max(ans, max(product / first_product, product / last_product) if len(a) > 1 else 0)

        return int(max(ans, 0 if len(num_splits) > 1 else -float('inf')))

    def maxProduct(self, nums: list) -> int:
        if len(nums) == 0:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

            max_so_far = temp_max

            result = max(max_so_far, result)

        return result


    def maxProduct(self, nums: list) -> int:
        if len(nums) == 0:
            return 0

        product = 1
        max_product = -float('inf')
        for n in nums:
            product *= n
            max_product = max(max_product, product)
            if product == 0:
                product = 1

        product = 1
        for n in reversed(nums):
            product *= n
            max_product = max(max_product, product)
            if product == 0:
                product = 1

        return max_product



if __name__ == '__main__':
    print(Solution().maxProduct([2,3,-2,4]))
    print(Solution().maxProduct([-2,0,-1]))
    print(Solution().maxProduct([-2,0]))
    print(Solution().maxProduct([0,-2,0]))
