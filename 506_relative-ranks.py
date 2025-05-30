import collections


class Solution:
    def findRelativeRanks(self, score):
        rank = collections.defaultdict(str)
        for i, s in enumerate(sorted(score, reverse=True)):
            r = str(i + 1)
            if i in {0, 1, 2}:
                r = ["Gold Medal", "Silver Medal", "Bronze Medal"][i]
            rank[s] = r

        return [rank[s] for s in score]


if __name__ == '__main__':
    print(Solution().findRelativeRanks([5,4,3,2,1]))
    print(Solution().findRelativeRanks([10,3,8,9,4]))
