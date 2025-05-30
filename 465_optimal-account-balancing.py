import collections


class Solution:

    def min_transfers(self, positives, negatives, negative_index):
        if negative_index == len(negatives):
            return 0
        min_transactions = float('inf')
        for i in range(len(positives)):
            if positives[i] == 0:
                continue
            if positives[i] + negatives[negative_index] == 0:
                earlier_positive_value = positives[i]
                earlier_negative_value = negatives[negative_index]
                positives[i] = 0
                negatives[negative_index] = 0
                transactions = self.min_transfers(positives, negatives, negative_index + 1) + 1
                min_transactions = min(min_transactions, transactions)
                positives[i] = earlier_positive_value
                negatives[negative_index] = earlier_negative_value
            elif positives[i] + negatives[negative_index] < 0:
                earlier_positive_value = positives[i]
                earlier_negative_value = negatives[negative_index]
                negatives[negative_index] += positives[i]
                positives[i] = 0
                transactions = self.min_transfers(positives, negatives, negative_index) + 1
                min_transactions = min(min_transactions, transactions)
                positives[i] = earlier_positive_value
                negatives[negative_index] = earlier_negative_value
            else:
                earlier_positive_value = positives[i]
                earlier_negative_value = negatives[negative_index]
                positives[i] += negatives[negative_index]
                negatives[negative_index] = 0
                transactions = self.min_transfers(positives, negatives, negative_index + 1) + 1
                min_transactions = min(min_transactions, transactions)
                positives[i] = earlier_positive_value
                negatives[negative_index] = earlier_negative_value
        return min_transactions

    def minTransfers(self, transactions) -> int:
        account = collections.defaultdict(int)
        for (sender, receiver, amount) in transactions:
            account[sender] -= amount
            account[receiver] += amount

        positives = []
        negatives = []

        for people in account:
            if account[people] < 0:
                negatives.append(account[people])
            elif account[people] > 0:
                positives.append(account[people])

        return self.min_transfers(positives, negatives, 0)







if __name__ == '__main__':
    # print(Solution().minTransfers([[0,1,10],[2,0,5]])) #2
    # print(Solution().minTransfers([[0,1,5],[2,3,1],[2,0,1],[4,0,2]])) #4
    # print(Solution().minTransfers([[1,5,8],[8,9,8],[2,3,9],[4,3,1]])) #4
    # print(Solution().minTransfers([[0,1,5],[0,2,5],[3,4,5],[3,5,5]])) #4
    # print(Solution().minTransfers([[0,1,10],[1,0,1],[1,2,5],[2,0,5]])) #1
    print(Solution().minTransfers([[5,6,2],[3,1,3],[9,0,9],[7,1,2],[3,5,8],[8,6,10],[9,2,8]])) #6
