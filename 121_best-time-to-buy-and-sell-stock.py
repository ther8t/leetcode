class Solution:
    def maxProfit(self, prices) -> int:
        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - min_price)
            min_price = min(min_price, prices[i])

        return max_profit

    # def maxProfit(self, prices) -> int:
    #     n = len(prices)
    #     maximums = [-1] * (n + 1)
    #
    #     for i in range(n - 1, -1, -1):
    #         maximums[i] = max(maximums[i + 1], prices[i])
    #     maximums.pop()
    #     m, p = max(zip(maximums, prices), key=lambda x: x[0] - x[1])
    #     return m - p


if __name__ == '__main__':
    print(Solution().maxProfit(prices = [7,1,5,3,6,4]))
    print(Solution().maxProfit(prices = [7,6,4,3,1]))
