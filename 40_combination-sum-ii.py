import bisect
import functools


class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        return self.combinationSumRec(candidates, target)

    def combinationSumRec(self, candidates, target):
        if not candidates or target <= 0:
            return []
        iterator = 0
        sum = []
        while iterator < len(candidates) and candidates[iterator] <= target:
            sumIncludingCurrentCandidate = self.combinationSumRec(candidates[iterator + 1:],
                                                                  target - candidates[iterator])
            for i in range(len(sumIncludingCurrentCandidate)):
                sum.append([candidates[iterator]] + sumIncludingCurrentCandidate[i])
            if candidates[iterator] == target:
                sum.append([target])
            while iterator + 1 < len(candidates) and candidates[iterator] == candidates[iterator + 1]:
                iterator += 1
            iterator+=1
        return sum


    """
    Revision 2:
    
    """
    def combinationSum2(self, candidates, target):
        candidates.sort()
        ans = []

        def combinationSumRec(index, arr_sum, arr):
            nonlocal ans
            if arr_sum == target:
                ans.append(arr)
                return
            ptr = index
            while ptr < len(candidates):
                current_value = candidates[ptr]
                if arr_sum + current_value > target:
                    break
                combinationSumRec(ptr + 1, arr_sum + current_value, arr + [current_value])
                while ptr < len(candidates) and candidates[ptr] == current_value:
                    ptr += 1

        combinationSumRec(0, 0, [])

        return ans


if __name__ == '__main__':
    print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    print(Solution().combinationSum2([2,5,2,1,2], 5))
