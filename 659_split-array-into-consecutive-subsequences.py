import collections


class Solution:
    def isPossible(self, nums) -> bool:
        if not nums:
            return False
        a = collections.defaultdict(list)

        for n in nums:
            if n - 1 in a and len(a[n - 1]) > 0:
                b = min(a[n - 1], key=lambda x:len(x))
                a[n - 1].remove(b)
                if len(a[n - 1]) == 0:
                    del a[n - 1]
                a[n].append(b + [n])
            else:
                a[n].append([n])

        for n in a:
            if len(min(a[n], key=lambda x:len(x))) < 3:
                return False

        return True


if __name__ == '__main__':
    print(Solution().isPossible(nums = [1,2,3,3,4,5]))
    print(Solution().isPossible(nums = [1,2,3,3,4,4,5,5]))
    print(Solution().isPossible(nums = [1,2,3,4,4,5]))

