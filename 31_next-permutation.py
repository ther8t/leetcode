class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find the first decreasing sequence from the end. (x,y)
        # sort the remaining array from y including y, which is basically reading the array in the reverse order.
        # find the first number JUST greater than x I can exchange x with
        # swap the x with that number and return the array
        firstDecreasingPair = len(nums) - 2
        while firstDecreasingPair >= 0 and nums[firstDecreasingPair + 1] <= nums[firstDecreasingPair]:
            firstDecreasingPair -= 1

        for i in range(0, (len(nums) - 1 - firstDecreasingPair) // 2):
            temp = nums[firstDecreasingPair + i + 1]
            nums[firstDecreasingPair + i + 1] = nums[len(nums) - 1 - i]
            nums[len(nums) - 1 - i] = temp

        if firstDecreasingPair >= 0:
            exchange1 = firstDecreasingPair
            iterator = firstDecreasingPair + 1
            while nums[iterator] <= nums[exchange1]:
                iterator += 1

            # swap
            temp = nums[exchange1]
            nums[exchange1] = nums[iterator]
            nums[iterator] = temp


if __name__ == '__main__':
    print(Solution().nextPermutation([1, 3, 4, 2]))
    # nums = [4, 6, 5, 3, 2, 1]
    # print(nums[-1])
    # alphabets = nums[3:]
    # alphabets.sort()
    # nums = nums[0:3] + alphabets
    # print(nums)
