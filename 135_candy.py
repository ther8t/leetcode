class Solution:
    """
    Revision 2 : This was a question I was able to do in just a single go then. I was in the flow for monotonic arrays and this question just struck.
    This time however I found it a bit difficult to figure out. My solution was to find a slope and add n(a+l)/2 for a single slope. This eliminates the use of the storage array.
    Though this is a better solution than the one I have implemented but this one is much simpler and the beauty of this solution is to change the value of the adjacent indexes based on the value of the current index.
    """
    def candy(self, ratings) -> int:
        n = len(ratings)
        candy = [1] * n

        for i in range(n-1):
            if ratings[i + 1] > ratings[i] and candy[i + 1] <= candy[i]:
                candy[i + 1] = candy[i] + 1

        for i in range(n-1, 0, -1):
            if ratings[i - 1] > ratings[i] and candy[i - 1] <= candy[i]:
                candy[i - 1] = candy[i] + 1

        return sum(candy)

    """
    Attempt : Fire
    This is interesting because I didn't put a check for candies this time and it worked.
    But this is about the same as the attempt #2 because the max condition is the same check as the candies check.
    """
    def candy(self, ratings) -> int:
        n = len(ratings)
        candies = [1 for _ in range(n + 1)]

        for i in range(1, n):
            if ratings[i - 1] < ratings[i]:
                candies[i] = candies[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies[0:-1])



if __name__ == '__main__':
    print(Solution().candy(ratings = [1,0,2]))
    print(Solution().candy(ratings = [1,2,2]))
    print(Solution().candy(ratings = [10, 5, 0, 2, 1, 2, 1, 6]))
