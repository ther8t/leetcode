class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        return self.combinationSumRec(candidates, target)

    def combinationSumRec(self, candidates, target):
        if not candidates or target <= 0:
            return []
        iterator = 0
        sum = []
        while iterator < len(candidates) and candidates[iterator] <= target:
            sumIncludingCurrentCandidate = self.combinationSumRec(candidates[iterator:], target - candidates[iterator])
            for i in range(len(sumIncludingCurrentCandidate)):
                sum.append([candidates[iterator]] + sumIncludingCurrentCandidate[i])
            if candidates[iterator] == target:
                sum.append([target])
            iterator += 1
        return sum


if __name__ == '__main__':
    print(Solution().combinationSum([2, 3, 5, 6], 8))
