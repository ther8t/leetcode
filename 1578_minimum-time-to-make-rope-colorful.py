import functools


class Solution:
    def minCost(self, colors: str, neededTime) -> int:
        lo, hi = 0, 0
        n = len(colors)
        score = 0

        while lo < n and hi < n:
            hi = lo
            max_time = -float('inf')
            total_time = 0
            while hi < n and colors[hi] == colors[lo]:
                total_time += neededTime[hi]
                max_time = max(max_time, neededTime[hi])
                hi += 1
            score += total_time - max_time
            lo = hi

        return score


    # def minCost(self, colors: str, neededTime) -> int:
    #
    #     @functools.lru_cache(None)
    #     def cost(index):
    #         if index >= len(colors):
    #             return 0
    #         for i in range(index, len(colors)):
    #             if i + 1 < len(colors) and colors[i] == colors[i + 1]:
    #                 return min(neededTime[i] + cost(i + 1), neededTime[i + 1] + cost(i + 2))
    #         return 0
    #
    #     return cost(0)


if __name__ == '__main__':
    print(Solution().minCost(colors = "abaac", neededTime = [1,2,3,4,5]))
    print(Solution().minCost(colors = "abc", neededTime = [1,2,3]))
    print(Solution().minCost(colors = "aabaa", neededTime = [1,2,3,4,1]))
    print(Solution().minCost("bbbaaa", [4,9,3,8,8,9]))
