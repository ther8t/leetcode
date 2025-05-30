import collections


class Solution:
    def totalFruit(self, fruits) -> int:
        if not fruits:
            return 0
        a = collections.defaultdict(int)
        lo, hi = 0, 0
        max_len = 0
        while hi < len(fruits):
            a[fruits[hi]] += 1
            while len(a) > 2:
                a[fruits[lo]] -= 1
                if a[fruits[lo]] == 0:
                    del a[fruits[lo]]
                lo += 1
            max_len = max(max_len, hi - lo + 1)
            hi += 1

        return max_len


if __name__ == '__main__':
    print(Solution().totalFruit([1,2,1]))
    print(Solution().totalFruit([0,1,2,2]))
    print(Solution().totalFruit(fruits = [1,2,3,2,2]))

