import collections


class Solution:

    # # same solution but cleaner
    # def canReorderDoubled(self, arr) -> bool:
    #     hagrid = collections.Counter(arr)
    #
    #     arr.sort(key=lambda x: abs(x))
    #     for i in sorted(arr, key=lambda x: abs(x)):
    #         if hagrid[i] == 0: continue
    #         if hagrid[2 * i] == 0: return False
    #         hagrid[i] -= 1
    #         hagrid[2 * i] -= 1
    #     return True

    """
    Revision 2:
    I wanted to check why we sort. I thought the algo would work without sorting, but I failed to recognise that 2,4,1,8. cannot be because they are grouped like 2,4 and 1,8 so it returns false.
    We need to go in order so that each element can have a chance to find its partner in order.
    The below algo works after adding sorted keyword.
    """
    def canReorderDoubled(self, arr) -> bool:
        counter = collections.Counter(arr)
        for i in sorted(counter.keys()):
            if i == 0:
                if counter[i] % 2 == 1:
                    return False
                else:
                    del counter[i]
                continue

            """
            Interestingly, this line has two purposes.
            1. In the case where there are multiple occurances of same number, it removes multiple at the same time. [2, 2, 4, 4, 4, 8]
            2. In the case where there are negative numbers and sorted list would give us 2x before x, it helps us with such a case.
               [-4, -2, 2, 4], For x - -4, it will search for 2x = -8 and thus reduction will be 0, therefore it can't remove -4.
            """
            reduction = min(counter[i], counter[2 * i])
            counter[i] -= reduction
            if 2 * i in counter: counter[2 * i] -= reduction
            if counter[i] == 0: del counter[i]
            if counter[2 * i] == 0: del counter[2 * i]

        return len(counter) == 0


    # def canReorderDoubled(self, arr) -> bool:
    #     hagrid = collections.defaultdict(int)
    #     for i in arr:
    #         hagrid[i] += 1
    #
    #     arr.sort(key = lambda x: abs(x))
    #     ptr = len(arr) - 1
    #     while ptr >= 0:
    #         if hagrid[arr[ptr]] == 0:
    #             ptr -= 1
    #             continue
    #         if arr[ptr] % 2 == 1:
    #             return False
    #         if arr[ptr] // 2 in hagrid.keys() and hagrid[arr[ptr] // 2] != 0:
    #             hagrid[arr[ptr]] -= 1
    #             hagrid[arr[ptr] // 2] -= 1
    #         else:
    #             return False
    #         ptr -= 1
    #     return True


if __name__ == '__main__':
    print(Solution().canReorderDoubled([4, -2, 2, -4]))
    print(Solution().canReorderDoubled(arr = [3,1,3,6]))
    print(Solution().canReorderDoubled(arr = [2,1,2,6]))
