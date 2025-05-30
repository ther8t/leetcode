class Solution:

    # TLE
    def maxScore(self, cardPoints, k: int) -> int:
        def summation(start, end):  # end not included
            sum = 0
            for i in range(start, end):
                sum += cardPoints[i]
            return sum

        totalSum = summation(0, len(cardPoints))
        if k == len(cardPoints):
            return totalSum

        slidingWindowSize = len(cardPoints) - k
        if slidingWindowSize<k:
            maxSum = 0
            windowSum = -1
            for i in range(0, len(cardPoints) - slidingWindowSize + 1):
                if windowSum == -1:
                    windowSum = summation(i, i + slidingWindowSize)
                else:
                    windowSum = windowSum + (cardPoints[i + slidingWindowSize - 1]) - cardPoints[i - 1]
                maxSum = max(maxSum, totalSum - windowSum)
            return maxSum
        else:
            maxSum = 0
            sum = -1
            for i in range(0, k + 1):
                if sum == -1:
                    sum = summation(0, i) + summation(len(cardPoints) - (k - i), len(cardPoints))
                else:
                    sum += (-cardPoints[len(cardPoints) - k + i - 1] + cardPoints[i - 1])
                maxSum = max(maxSum, sum)
            return maxSum

    # TLE
    # def maxScore(self, cardPoints, k: int) -> int:
    #     def summation(start, end):  # end not included
    #         sum = 0
    #         for i in range(start, end):
    #             sum += cardPoints[i]
    #         return sum
    #
    #     totalSum = summation(0, len(cardPoints))
    #     if k == len(cardPoints):
    #         return totalSum
    #
    #     slidingWindowSize = len(cardPoints) - k
    #     if slidingWindowSize<k:
    #         maxSum = 0
    #         for i in range(0, len(cardPoints) - slidingWindowSize + 1):
    #             windowSum = summation(i, i + slidingWindowSize)
    #             maxSum = max(maxSum, totalSum - windowSum)
    #         return maxSum
    #     else:
    #         maxSum = 0
    #         for i in range(0, k + 1):
    #             sum = summation(0, i) + summation(len(cardPoints) - (k - i), len(cardPoints))
    #             if sum > maxSum:
    #                 maxSum = sum
    #         return maxSum

    # def maxScore(self, cardPoints, k: int) -> int:
    #     def summation(start, end):  # end not included
    #         sum = 0
    #         for i in range(start, end):
    #             sum += cardPoints[i]
    #         return sum
    #
    #     totalSum = summation(0, len(cardPoints))
    #     if k == len(cardPoints):
    #         return totalSum
    #
    #     slidingWindowSize = len(cardPoints) - k
    #
    #     maxSum = 0
    #     windowSum = -1
    #     for i in range(0, len(cardPoints) - slidingWindowSize + 1):
    #         if windowSum == -1:
    #             windowSum = summation(i, i + slidingWindowSize)
    #         else:
    #             windowSum = windowSum + (cardPoints[i + slidingWindowSize - 1]) - cardPoints[i - 1]
    #         maxSum = max(maxSum, totalSum - windowSum)
    #     return maxSum

    # TLE
    # def maxScore(self, cardPoints, k: int) -> int:
    #     def summation(start, end):  # end not included
    #         sum = 0
    #         for i in range(start, end):
    #             sum += cardPoints[i]
    #         return sum
    #
    #     if k == 0:
    #         return 0
    #     if k == len(cardPoints):
    #         return summation(0, len(cardPoints))
    #     maxSum = 0
    #     for i in range(0, k + 1):
    #         sum = summation(0, i) + summation(len(cardPoints) - (k - i), len(cardPoints))
    #         if sum > maxSum:
    #             maxSum = sum
    #     return maxSum

    # TLE
    # def maxScore(self, cardPoints, k: int) -> int:
    #     if k == 0:
    #         return 0
    #     return max(cardPoints[0] + self.maxScore(cardPoints[1:], k - 1),
    #                cardPoints[-1] + self.maxScore(cardPoints[0: -1], k - 1))


if __name__ == '__main__':
    print(Solution().maxScore(
        [96, 90, 41, 82, 39, 74, 64, 50, 30]
        , 8))
