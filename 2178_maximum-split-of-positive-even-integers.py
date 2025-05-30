import math


class Solution:
    def maximumEvenSplit(self, finalSum: int):
        if finalSum%2!=0:
            return []
        # array = []
        # arrayMax = 0
        # arraySum = 0
        #
        # for number in range(2, finalSum+1, 2):
        #     if arraySum + number<=finalSum:
        #         array.append(number)
        #         arraySum+=number
        #     else:
        #         break
        n = int((-1 + math.sqrt(1 + 4 * finalSum)) // 2)
        # justUnder *= (justUnder + 1)
        diff = (finalSum - n*(n+1))
        a = [i*2 for i in range(1, n+1)]
        a[-1]+=diff
        return a
        #
        # diff = (finalSum - arraySum)
        # array[-1]+=diff
        # return array

if __name__ == '__main__':
    print(Solution().maximumEvenSplit(20))
