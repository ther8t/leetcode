import heapq


class Solution:
    def connectSticks(self, sticks) -> int:
        h = []
        for l in sticks:
            heapq.heappush(h, l)

        cost = 0
        while len(h) > 1:
            a, b = heapq.heappop(h), heapq.heappop(h)
            current_cost = (a + b)
            cost += current_cost
            heapq.heappush(h, current_cost)

        return cost

    # # Wrong Answer
    # def connectSticks(self, sticks) -> int:
    #     if len(sticks) <= 1:
    #         return 0
    #     sticks.sort()
    #
    #     weight = 1
    #     score = 0
    #     for i in range(len(sticks) - 1, 1, -1):
    #         score += sticks[i] * weight
    #         weight += 1
    #
    #     score += weight * (sticks[0] + sticks[1])
    #     return score


if __name__ == '__main__':
    print(Solution().connectSticks(sticks = [2,4,3]))
    print(Solution().connectSticks(sticks = [1,8,3,5]))
    print(Solution().connectSticks(sticks = [5]))
    print(Solution().connectSticks([3354,4316,3259,4904,4598,474,3166,6322,8080,9009]))
