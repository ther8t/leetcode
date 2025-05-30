import functools


class Solution:
    def maxProfit(self, prices) -> int:
        return sum([prices[i] - prices[i - 1] if prices[i] > prices[i - 1] else 0 for i in range(1, len(prices))])
        # total_profit = 0
        # l, r = 0, 1
        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         total_profit += prices[r] - prices[l]
        #     l = r
        #     r += 1
        # return total_profit


if __name__ == '__main__':
    print(Solution().maxProfit(prices = [7,1,5,3,6,4]))
    print(Solution().maxProfit(prices = [1,2,3,4,6]))
    print(Solution().maxProfit(prices = [7,6,4,3,1]))
