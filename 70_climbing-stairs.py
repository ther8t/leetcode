import functools


class Solution:
    """
    Although this question is marked Easy and it is. There is a slight complication with this which I at first failed to understand.
    I came about this question from 837_new-21-game. These both questions are similar to each other and fibonacci sequence.
    The question is straight forward f(n) = f(n-1) + f(n-2).

    BUT
    This solution to this question can also be written as:
    def f(n):
        if n <= 1:
            return 1
        return f(n-1) + f(n-2)
    n == 1 I understand, but how can f(0) be 1?
    This troubled me a lot.
    The answer is that f(0) doesn't mean anything. There can't be any ways to reach 0, being the starting point!
    So we need to calculate f(1) and f(2), just like in fibonacci series.
    Although there exist a solution which does n <= 1, just like above but this has been extrapolated from the solutions ahead of it.
    It's like asking 1-indexed fibonacci sequence what the 0th term is. Of course you can find it, you might also find f(-1), f(-2) but it's meaningless.

    There was another thing which troubled me, but it was my error in understanding the question. This is more from a reverse solution to the question.
    I had tried.
    def f(i):
        if i == n:
            return 0
        steps = 0
        if i + 1 <= n:
            steps += f(i+1)
        if i + 2 <= n:
            steps += f(i+2)
        return steps
    My idea being that once I reach n, the steps I would need to take would be 0. I had confused myself with the number of steps and number of ways.
    I don't need to calculate the number of steps. I need to calculate the number of ways. Once I reach n. I have found 1 way of solving it. All I have to do in this question is to change return 0 to return 1.

    """
    def climbStairs(self, n: int) -> int:

        @functools.lru_cache(None)
        def f(step_on):
            if step_on == 2:
                return 2
            if step_on == 1:
                return 1

            return f(step_on - 1) + f(step_on - 2)

        return f(n)

    """
    This is a much understandable solution to the question. At the end if I reach n only then there is a way, so return 1.
    < n continue with the recursion.
    > n stop because there is not a way ahead and this is not one of the ways so return 0.
    This is similar to what I was trying in 837_new_21_game.
    """
    def climbStairs(self, n: int) -> int:

        @functools.lru_cache(None)
        def f(step_on):
            if step_on > n:
                return 0
            if step_on == n:
                return 1

            return f(step_on + 1) + f(step_on + 2)

        return f(0)

    def climbStairs(self, n: int) -> int:
        dp = [0] * max(3, n + 1)
        dp[1], dp[2] = 1, 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


if __name__ == '__main__':
    print(Solution().climbStairs(1))
    print(Solution().climbStairs(3))
    print(Solution().climbStairs(4))
