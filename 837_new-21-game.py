class Solution:
    """
    Let's consider a game of Blackjack.
    You have cards of score 1 to 10. You have decided that you would not draw a card if the score goes over 17 because it might risk you getting over 21. The goal is to reach a sum of 21.

    What is the probability of picking up a single card? 1/10 = 0.1

    Q : What is the probability of getting a score exactly equal to 12?
    P(12) = P(11) * (Prob of picking up a 1) + P(10) * (Prob of picking up a 2) + ... + P(2) * (Prob of picking up 10)

    So what do we really need?
    We need the sum of all those numbers less than n which are possible with these cards of max limit m and limit k.
    Q : If we need the sum of all the numbers less than n, do we include 12?
    No, because for 12 the game isn't over yet. We would draw another card so the sum reaches the limit k or above. Ok, so the sum should be for all the probabilities of scores between k and n, including k and excluding n.

    Q : What if n = infinity?
    Think about it. what is the probability that the score would be less than infinity once you stop drawing card after k? Probability = 1.0
    What then is the probability if n >= k + m? Probability = 1.0

    And most important of all. Remember.
    Winner Winner Chicken Dinner!!
    """
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts:
            return 1
        dp = [1.0] + [0] * n
        window = 1

        for i in range(1, n + 1):
            dp[i] = window / maxPts
            if i - maxPts >= 0: window -= dp[i - maxPts]
            if i < k: window += dp[i]

        return sum(dp[k:])



    # """
    # I give up on solving this with recursion. It gets too complicated. It's similar to the fibonacci series and it is similar to 70_climbing-stairs.
    # I have an understanding of how and why we use dp or array. It's just that solving with recursion is my preferred way an I would have wanted a solution, just because fib sequence and climbing stairs are solved by recursion as well.
    # """
    # def new21Game(self, n: int, k: int, maxPts: int) -> float:
    #     prob_one_card = 1 / maxPts
    #
    #     def prob(target, current_sum):
    #         if current_sum == target or current_sum >= k:
    #             return 1
    #         if current_sum > target:
    #             return 0
    #
    #         p = 0
    #         for i in range(1, maxPts + 1):
    #             # probability of drawing one card of value i * probability of remainder
    #             p += prob_one_card * prob(target, current_sum + i)
    #         return p
    #
    #     p_sum = 0
    #     for i in range(1, n + 1):
    #         p_sum += prob(i, 0)
    #
    #     return p_sum
    #     # return prob(1, 0)

    # def new21Game(self, n: int, k: int, maxPts: int) -> float:
    #     dp = [0.0 for _ in range(n + 1)]
    #     for i in range(k, n + 1):
    #         dp[i] = 1.0
    #
    #     for i in range(k, 0, -1):
    #         dp[i - 1] = dp[i] - (dp[min(i + maxPts + 1, len(dp) - 1)] - dp[i])/maxPts
    #
    #     return dp[0]


if __name__ == '__main__':
    print(Solution().new21Game(n = 21, k = 17, maxPts = 10))
    print(Solution().new21Game(n = 10, k = 1, maxPts = 10))
    print(Solution().new21Game(n = 6, k = 1, maxPts = 10))
