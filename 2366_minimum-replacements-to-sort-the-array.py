import math


class Solution:
    # Not my solution but it works and is a bit easier to put the head around, if that is such a thing with this question.
    def minimumReplacement(self, nums) -> int:
        ans = 0
        divisor = nums[-1]

        index = len(nums) - 2
        for n in reversed(nums[:-1]):
            dividend = n
            final_broken_elements_count = dividend // divisor
            if dividend % divisor != 0:
                final_broken_elements_count += 1
                divisor = dividend // final_broken_elements_count
            ans += final_broken_elements_count - 1
            print(index, dividend, final_broken_elements_count, divisor)
            index -= 1
        return ans


    def minimumReplacement(self, nums) -> int:
        ans = 0
        divisor = nums[-1]

        for n in reversed(nums[:-1]):
            dividend = n
            final_broken_elements_count = math.ceil(dividend / divisor)
            divisor = dividend // final_broken_elements_count
            quotient = final_broken_elements_count - 1
            """
            Turns out that I had the solution all along. What I failed to recognize was that I don't need remainder for the next iteration. I need the last element if I break the series.
            For example. [346,22]
            346/22 = 15.72 = 15 * 22 + 16
            This means there would be 15 elements of 22 and 1 element of 16.
            15 + 1 = 16 elements in total. 346 breaks into 16 elements in total.
            ceiling(346/22) = 16 * 21 + 10. I could have 17 elements(16-21 and 1-10), BUT
            I could also distribute the 10 among 10-21s to make them 22. The final elements would then become 16(10-22 and 6-21)
            346 = 22*10 + 21*6 = 21, 21, 21, 21, 21, 21, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22
            Then what is the next number for the next iteration? Ans : 21
            This does two things:
            First, it leaves the last number, NOT THE REMAINDER, a number which is higher than the reaminder, were I to consider 15 + 1 parts.
            Two, produces a number which is closest to the next number.
            
            The question thus is how do I come up with this?
            If I divide a number n by another number a, it is guaranteed to produce numbers <= a.
            What I have to find out really is an EQUITABLE distribution of numbers.
            Take [...,13,5] can be written as 4,4,5 or 3,5,5. Which one would you prefer?
            How do you then calculate 4?
            ceil(13/5) = 3 -> This means we can distribute 13 into MIN of 3 parts.
            13 = 2 * d + r (3 parts) OR
            13 = 3 * d + 0 (3 parts)
            d would then be 13 // 3 = 4
            Although this result works but I still don't have a good feel for the question.
            """
            # remainder = dividend - divisor * quotient
            # if remainder == 0:
            #     quotient -= 1
            #     remainder = divisor
            # divisor = remainder
            ans += quotient
        return ans


    # # Wrong Answer: Althought the logic is correct but somehow the solution fails at large array. I'm trying iterative approach.
    # def minimumReplacement(self, nums) -> int:
    #
    #     @lru_cache(None)
    #     def compute(index, next_value):
    #         if index <= 0:
    #             return max(math.ceil(nums[index] / next_value) - 1, 0)
    #         if nums[index] > next_value:
    #             dividend = nums[index]
    #             min_steps = float('inf')
    #
    #             """
    #             It took a lot of time to figure out what the divisor could be. The key idea was that divisor should be less than or equal to the next value, because of the question.
    #             Also it should be greater than or equal to the remainder, so that it can help create further series, otherwise it can be split further.
    #             """
    #             for divisor in range(next_value, 0 if nums[index - 1] >= next_value else nums[index - 1] - 1, -1):
    #                 quotient = nums[index] // divisor
    #                 remainder = dividend % divisor
    #                 if remainder > divisor:
    #                     break
    #                 if remainder == 0:
    #                     remainder = divisor
    #                     quotient -= 1
    #                 min_steps = min(min_steps, quotient + compute(index - 1, remainder))
    #                 divisor -= 1
    #
    #             return min_steps
    #         else:
    #             return compute(index - 1, nums[index])
    #
    #     return compute(len(nums) - 2, nums[-1])


if __name__ == '__main__':
    print(Solution().minimumReplacement(nums = [3,9,3])) #2
    print(Solution().minimumReplacement(nums = [1,2,3,4,5])) #0
    print(Solution().minimumReplacement([11,5])) #2
    print(Solution().minimumReplacement([6, 8, 2])) #5
    print(Solution().minimumReplacement([12,9,7,6])) #6
    print(Solution().minimumReplacement([5,14,12])) #1
    print(Solution().minimumReplacement([1,13,15,2,5,14,12])) #20
    print(Solution().minimumReplacement([1])) #0
    print(Solution().minimumReplacement([50,150,27])) #6
    print(Solution().minimumReplacement([242,260,346,22])) #39
    print(Solution().minimumReplacement([368,112,2,282,349,127,36,98,371,79,309,221,175,262,224,215,230,250,84,269,384,328,118,97,17,105,342,344,242,160,394,17,120,335,76,101,260,244,378,375,164,190,320,376,197,398,353,138,362,38,54,172,3,300,264,165,251,24,312,355,237,314,397,101,117,268,36,165,373,269,351,67,263,332,296,13,118,294,159,137,82,288,250,131,354,261,192,111,16,139,261,295,112,121,234,335,256,303,328,242,260,346,22,277,179,223])) #17748
