class Solution:
    def maximumHappinessSum(self, happiness, k: int) -> int:
        return sum([max(0, h - i) for i, h in enumerate(sorted(happiness, reverse=True)[:k])])


if __name__ == '__main__':
    print(Solution().maximumHappinessSum(happiness = [1,2,3], k = 2))
    print(Solution().maximumHappinessSum(happiness = [1,1,1,1], k = 2))
    print(Solution().maximumHappinessSum(happiness = [2,3,4,5], k = 1))
