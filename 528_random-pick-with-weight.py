import bisect
import collections
import random


class Solution:

    # def __init__(self, w):
    #     self.indexWeightMap = collections.defaultdict(int)
    #     for index, weight in enumerate(w):
    #         self.indexWeightMap[index] += weight
    #     self.iterationMap = collections.defaultdict(int)
    #     pass
    #
    # def pickIndex(self) -> int:
    #     if not self.iterationMap:
    #         self.iterationMap = self.indexWeightMap.copy()
    #
    #     keys = list(self.iterationMap.keys())
    #     randomIndex = random.choice(keys)
    #     if self.iterationMap[randomIndex] == 1:
    #         del self.iterationMap[randomIndex]
    #     else:
    #         self.iterationMap[randomIndex] -= 1
    #     return randomIndex

    def __init__(self, w):
        self.sum = 0
        self.sumLine = []
        for index, occurance in enumerate(w):
            self.sum += occurance
            self.sumLine.append(self.sum)

    def pickIndex(self) -> int:
        randomNumber = random.random() * self.sum
        """
        Revision 2 : 
        The phrasing of the question is flawed, deeply flawed. In a just world the probability dictates that for [1, 3] weights there is a possibility of drawing 1, 1, 1, 1.
        The question phrases itself as if this is not wanted. However the real intention of the question is to simulate the real life where the probability tends to be as per the weights.
        The question then becomes much simpler.
        For the first case where we need to force the probability, the above solution is valid.
        For the case where we need to simulate the real life, the below solution is valid.
        The line commented below is a binary search in itself and is equivalent to the rest of the uncommented code below it. The question thus can be summed up in two lines.
        """
        # return bisect.bisect_left(self.sumLine, randomNumber)
        low, high = 0, len(self.sumLine)

        while low<high:
            mid = (low + high) // 2
            if randomNumber == self.sumLine[mid]:
                return mid
            elif randomNumber < self.sumLine[mid]:
                high = mid
            else:
                low = mid + 1
        return low

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

if __name__ == '__main__':
    s = Solution([1, 3])
    print(s.pickIndex())
    print(s.pickIndex())
    print(s.pickIndex())
    print(s.pickIndex())
