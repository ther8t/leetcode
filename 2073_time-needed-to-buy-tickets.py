class Solution:
    def timeRequiredToBuy(self, tickets, k: int) -> int:
        return sum([min(tickets[i] if i > k else tickets[i] - 1, tickets[k] - 1) for i in range(len(tickets))]) + k + 1


if __name__ == '__main__':
    print(Solution().timeRequiredToBuy(tickets = [2,3,2], k = 2))
    print(Solution().timeRequiredToBuy(tickets = [5,1,1,1], k = 0))
